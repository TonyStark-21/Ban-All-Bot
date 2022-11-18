import os
import logging 
from pyrogram import Client
from pyromod import listen
from config import Config

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


#ENV = bool(os.environ.get("ENV",False))

#if ENV:
API_ID=int(os.environ.get("API_ID","16191628"))
API_HASH=str(os.environ.get("API_HASH","7d5acccaf1df4f5b7a690b203fd1953e"))
TOKEN=str(os.environ.get("TOKEN","5651385902:AAFwigsgZLEETFCXutMjLyfMNgwuaUjMTIU"))
    

  
#else:
#    API_ID=Config.API_ID
#    API_HASH=Config.API_HASH
#    TOKEN=Config.TOKEN
    

app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="api/modules")
     )

LOG.info("starting the bot....")


