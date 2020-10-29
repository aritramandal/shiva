#credits to ROY

import time
from platform import python_version

from telethon import version

from userbot import ALIVE_NAME, CMD_HELP, StartTime, catdef, catversion

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
CAT_IMG = Config.ALIVE_PIC


@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    hmm = bot.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if DEX_IMG:
        dex_caption = f"**✮ MY BOT IS RUNNING SUCCESFULLY ✮**\n\n"
        dex_caption += f"**✧ Database :** `{check_sgnirts}`\n"
        dex_caption += f"**✧ Telethon version :** `{version.__version__}\n`"
        dex_caption += f"**✧ Python Version :** `{python_version()}\n`"
        dex_caption += f"**✧ Uptime :** `{uptime}\n`"
        dex_caption += f"**✧ My Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
        await borg.send_file(
            alive.chat_id, DEX_IMG, caption=dex_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**✮ MY BOT IS RUNNING SUCCESFULLY ✮**\n\n"
            f"**✧ Database :** `{check_sgnirts}`\n"
            f"**✧ Telethon Version :** `{version.__version__}\n`"
            f"**✧ Python Version :** `{python_version()}\n`"
            f"**✧ Uptime :** `{uptime}\n`"
            f"**✧ My Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n",
        )


@borg.on(admin_cmd(outgoing=True, pattern="ialive$"))
@borg.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    hmm = bot.uid
    dex_caption = f"**Dextro_userbot is Up and Running**\n"
    dex_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    dex_caption += f"**  -Python Version :** `{python_version()}\n`"
    dex_caption += f"**  -My peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
    results = await bot.inline_query(tgbotusername, dex_caption) 
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()

def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n**Syntax : **`.alive` \
      \n**Usage : ** status of bot.\
      \n\n**Syntax : **`.ialive` \
      \n**Usage : ** inline alive."
    }
)
