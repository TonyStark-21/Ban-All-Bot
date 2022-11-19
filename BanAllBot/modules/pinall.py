from BanAllBot import app,SUDO
from pyrogram import filters

@app.on_message(filters.command("unpinall") & filters.user(SUDO))
async def unpin_all(_,msg):
    chat_id=msg.chat.id
    await app.unpin_all_chat_messages(chat_id)
