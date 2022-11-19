from BanAllBot import app
from pyrogram import filters


@app.on_message(filters.command("banall"))
async def ban_all(_,msg):
    chat_id=msg.chat.id
    bot=await app.get_chat_member(chat_id,BOT_ID)
    permission=bot.privileges.can_restrict_members==True
    async for member in app.get_chat_members(chat_id):
        print(member.user.id)
    
