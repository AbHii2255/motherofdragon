#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ιAм Jυѕт A Aυтo Fɪʟᴇ Sʜᴀʀᴇ Boт..!🤩 Tнιѕ Boαт ιѕ Mαde Eхclυѕιvely For Tнe👉 Mαllυ Hυв Movιeѕ</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('👉 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/Mallushubb'),
                        InlineKeyboardButton('👉 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/Malluhubbmovies')   
                    ],
                    [
                        InlineKeyboardButton('Dєνєℓσρєя', url='https://t.me//Abhii2255')
                        InlineKeyboardButton("🔒 Сʟоѕе", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
