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
            text = f"ιAм Jυѕт A Aυтo Fɪʟᴇ Sʜᴀʀᴇ Boт..!🤩 Tнιѕ Boαт ιѕ Mαde Eхclυѕιvely For Tнe Mαllυ Hυв Movιeѕ",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🎥 Channel', url='https://t.me/Mallushubb'),
                        InlineKeyboardButton('🎥 Group', url='https://t.me/Malluhubbmovies')   
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
