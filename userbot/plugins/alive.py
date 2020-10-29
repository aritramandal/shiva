#credits to ROY

import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Dextro Master"
DEX_IMG = ""
dex_caption = "🔱 **Your Dextro is ready to rock** 🔱\n\n"

dex_caption += f" My owner          :   {DEFAULTUSER}\n"

dex_caption += " Telethon version   :   1.16.0 \n"

dex_caption += " channel            :   [ᴊᴏɪɴ](https://t.me/Dextro_support)\n"

dex_caption += "support group       :   [ᴊᴏɪɴ](https://t.me/Dextro_support_group)\n"

dex_caption += "repo                :   [Dextro_userbot](https:github.com/suhaash02/Dextro_userbot)\n"

dex_caption += f"My Peru Master     : [{DEFAULTUSER}](tg://user?id={hmm})\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, DEX_IMG,caption=dex_caption)
    await alive.delete() 
