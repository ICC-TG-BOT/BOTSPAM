from os import getenv

from decouple import config

APP_ID = getenv("APP_ID", "13976276")

API_HASH = getenv("API_HASH", "7f024cbc744a2f44569c3641b5ccecb7")

HEROKU_APP_NAME = config("HEROKU_APP_NAME", "toxic-spam-bot")
HEROKU_API_KEY = config("HEROKU_API_KEY", "5df78882-53e8-4b19-b8af-fde77ba88782")

BOT_TOKEN = config("BOT_TOKEN", "5701196266:AAGe0hsTmosdgBpsluhfIp0Q_CIVoBsCrQY")
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
try:
    SUDO_USERS = str(getenv("SUDO_USERS", "6020570673")).split("5348648456")
except Exception:
    SUDO_USERS = str(getenv("SUDO_USERS", "5348648456"))

START_MESSAGE = getenv("START_MESSAGE", "🌹𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓🌹")

PING_PIC = getenv("PING_PIC", "https://te.legra.ph/file/12c085eae53b7faec8f1e.jpg")

START_PIC = getenv("START_PIC", "https://te.legra.ph/file/12c085eae53b7faec8f1e.jpg")


HELP_MSG = getenv("HELP_MSG", "𝐖𝐇𝐀𝐓 𝐓𝐘𝐏𝐄 𝐈 𝐇𝐄𝐋𝐏 𝐘𝐎𝐔")
HELP_PIC = getenv("HELP_PIC", "https://te.legra.ph/file/12c085eae53b7faec8f1e.jpg")
LOG_CHANNEL = getenv("LOG_CHANNEL", None)
HANDLER = getenv("HANDLER", "/")
