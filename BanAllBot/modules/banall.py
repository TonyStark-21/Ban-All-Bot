from BanAllBot import app
from pyrogram import filters


@app.on_message(filters.command("banall"))
async def ban_all(_,msg):
    chat_id=msg.chat.id
    administrators = []
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True
    admin_permision=administrators.privileges.can_restrict_members==True
    async for member in app.get_chat_members(chat_id):       
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            administrators.append(m.user.id)
            if permission and admin_permision:
                try:
                    await app.ban_chat_member(chat_id, member.user.id)
                    await msg.reply_text("fucking all members")
                except Exception:
                    pass
            else:
                msg.reply_text("don't have permissions")  
            
