from BanAllBot import app
from pyrogram import filters
from pyrogram.types import ChatPermissions


@app.on_message(filters.command("mute"))
async def mute(_,msg):
    await app.restrict_chat_member(-1001547036942,5715447071,ChatPermissions(can_send_messages=False))
