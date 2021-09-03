from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**This Is A Video Player Bot Who Can Stream Videos In YOUR voice Chat\n\n**To use it:-** __ \n1) Add this Bot to your Group and Make it Admin \n2) Add__ @Video_Player_asisstant __to your Group__ \n3) **Commands** : \n`/stream` (IN REPLY TO A VIDEO) \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Phoenix", url="t.me/SOULxDED")
                                    ]]
                            ))
   else:
      await m.reply("**@Video_Player_Robot is Alive! ✨**")
