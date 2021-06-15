import discord
import discord_slash
import discord_components
import typing

async def send(self,
                content: str = "", *,
                embed: discord.Embed = None,
                embeds: typing.List[discord.Embed] = None,
                tts: bool = False,
                file: discord.File = None,
                files: typing.List[discord.File] = None,
                allowed_mentions: discord.AllowedMentions = None,
                hidden: bool = False,
                components: typing.List[typing.Union[discord_components.Component, typing.List[discord_components.Component]]] = None,
                delete_after: float = None) -> discord_slash.model.SlashMessage:
    """
    Sends response of the slash command.

    .. warning::
        - Since Release 1.0.9, this is completely changed. If you are migrating from older version, please make sure to fix the usage.
        - You can't use both ``embed`` and ``embeds`` at the same time, also applies to ``file`` and ``files``.
        - If you send files in the initial response, this will defer if it's not been deferred, and then PATCH with the message

    :param content:  Content of the response.
    :type content: str
    :param embed: Embed of the response.
    :type embed: discord.Embed
    :param embeds: Embeds of the response. Maximum 10.
    :type embeds: List[discord.Embed]
    :param tts: Whether to speak message using tts. Default ``False``.
    :type tts: bool
    :param file: File to send.
    :type file: discord.File
    :param files: Files to send.
    :type files: List[discord.File]
    :param allowed_mentions: AllowedMentions of the message.
    :type allowed_mentions: discord.AllowedMentions
    :param hidden: Whether the message is hidden, which means message content will only be seen to the author.
    :type hidden: bool
    :param delete_after: If provided, the number of seconds to wait in the background before deleting the message we just sent. If the deletion fails, then it is silently ignored.
    :type delete_after: float
    :return: Union[discord.Message, dict]
    """
    if embed and embeds:
        raise discord_slash.error.IncorrectFormat("You can't use both `embed` and `embeds`!")
    if embed:
        embeds = [embed]
    if embeds:
        if not isinstance(embeds, list):
            raise discord_slash.error.IncorrectFormat("Provide a list of embeds.")
        elif len(embeds) > 10:
            raise discord_slash.error.IncorrectFormat("Do not provide more than 10 embeds.")
    if file and files:
        raise discord_slash.error.IncorrectFormat("You can't use both `file` and `files`!")
    if file:
        files = [file]
    if delete_after and hidden:
        raise discord_slash.error.IncorrectFormat("You can't delete a hidden message!")

    base = {
        **discord_components.DiscordComponents._get_components_json(None, components),
        "content": content,
        "tts": tts,
        "embeds": [x.to_dict() for x in embeds] if embeds else [],
        "allowed_mentions": allowed_mentions.to_dict() if allowed_mentions
        else self.bot.allowed_mentions.to_dict() if self.bot.allowed_mentions else {}
    }
    if hidden:
        base["flags"] = 64

    initial_message = False
    if not self.responded:
        initial_message = True
        if files and not self.deferred:
            await self.defer(hidden=hidden)
        if self.deferred:
            if self._deferred_hidden != hidden:
                self._logger.warning(
                    "Deferred response might not be what you set it to! (hidden / visible) "
                    "This is because it was deferred in a different state."
                )
            resp = await self._http.edit(base, self._token, files=files)
            self.deferred = False
        else:
            json_data = {
                "type": 4,
                "data": base
            }
            await self._http.post_initial_response(json_data, self.interaction_id, self._token)
            if not hidden:
                resp = await self._http.edit({}, self._token)
            else:
                resp = {}
        self.responded = True
    else:
        resp = await self._http.post_followup(base, self._token, files=files)
    if files:
        for file in files:
            file.close()
    if not hidden:
        smsg = discord_slash.model.SlashMessage(state=self.bot._connection,
                                  data=resp,
                                  channel=self.channel or discord.Object(id=self.channel_id),
                                  _http=self._http,
                                  interaction_token=self._token)
        if delete_after:
            self.bot.loop.create_task(smsg.delete(delay=delete_after))
        if initial_message:
            self.message = smsg
        return smsg
    else:
        return resp

old_init = discord_slash.SlashContext.__init__

def init(self, _http: discord_slash.http.SlashCommandRequest, _json: dict, _discord: typing.Union[discord.Client, discord.ext.commands.Bot], logger):
  self._token = _json["token"]
  old_init(self, _http, _json, _discord, logger)

discord_slash.SlashContext.__init__ = init
discord_slash.SlashContext.send = send
