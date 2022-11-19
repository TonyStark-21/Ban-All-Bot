from BanAllBot import app
from pyrogram import filters


@app.on_message(filters.command("mute"))
async def mute(_,msg):
    await app.restrict_chat_member(-1001547036942,5715447071)
