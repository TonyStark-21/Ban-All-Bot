import os
import logging 
from pyrogram import Client


# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID","16191628"))
    API_HASH=str(os.environ.get("API_HASH","7d5acccaf1df4f5b7a690b203fd1953e"))
    TOKEN=str(os.environ.get("TOKEN","5856070290:AAHi_fH5fu8pZX8fXvMazhMWqtNu7TFIdAs"))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "5264285143").split(" "))
    START_IMG="https://telegra.ph/file/143007829ff893579fae3.jpg"
    BOT_ID=int(os.environ.get("BOT_ID","5264285143"))
    BOT_USERNAME=str(os.environ.get("BOT_USERNAME","Ban_AllBot"))
    BOT_NAME=str(os.environ.get("BOT_NAME","BAN ALL"))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    TOKEN=Config.TOKEN
    SUDO=Config.SUDO
    START_IMG=Config.START_IMG
    BOT_ID=Config.BOT_ID
    BOT_USERNAME=Config.BOT_USERNAME
    BOT_NAME=Config.BOT_NAME



app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="BanAllBot/modules")
     )

LOG.info("starting the bot....")


