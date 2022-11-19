from BanAllBot import app,START_IMG,BOT_USERNAME,BOT_NAME
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

START_MSG=f"""
ʜᴇʏ **{}*** , ɪ ᴀᴍ {},
ɪ ʜᴀᴠᴇ sᴏᴍᴇ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴘʟᴜɢɪɴs ʏᴏᴜ sʜᴏᴜʟᴅ ᴛʀʏ ɪᴛ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.
ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴛʜᴇʀs ɢʀᴏᴜᴘ ᴛᴏ ᴅᴇsᴛʀᴏʏ ɪᴛ.
"""
START_BUTTONS=InlineKeyboardMarkup (
      [
      [
         InlineKeyboardButton (text="➕ ᴀᴅᴅ ᴍᴇ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
      ],
      [
         InlineKeyboardButton (text="ʜᴇʟᴘ",callback_data="help_back")
      ]
      ]

)

#HELP_MSG="""

#"""

#HELP_BUTTONS=


@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
     photo=START_IMG,
     caption=START_MSG.format(msg.from_user.mention,BOT_NAME),
     reply_markup=START_BUTTONS)

    



if __name__ == "__main__":
    print("started")
    app.run()
