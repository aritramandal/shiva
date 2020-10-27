from userbot import ALIVE_NAME, AUTONAME, CMD_HELP, DEFAULT_BIO, bot

DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = (
    str(DEFAULT_BIO)
    if DEFAULT_BIO
    else "Dextro's life quote life isnt about finding yourself it is creating yourself "
)
DEFAULTUSERBIO = (
    str(DEFAULT_BIO)
    if DEFAULT_BIO
    else "life is valuable dont waste it by seeing my bio"
)
BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
BOTLOG = True
