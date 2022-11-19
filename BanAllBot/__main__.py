from BanAllBot import app
from pyrogram import filters

@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_text("i am under creation by [ᏚᎢᎪᏒᏦ](https://t.me/NoobStark_21)")
async def main():
	async with app:
		administrators = []
        async for m in app. get_chat_members(-1001547036942, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        	 administrators.append(m)
        	 print(administrators)
   




if __name__ == "__main__":
    print("started")
    app.run(main())
