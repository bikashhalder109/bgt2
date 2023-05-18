# 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫 // @𝐀𝐝𝐢𝐭𝐲𝐚𝐒𝐞𝐫𝐯𝐞𝐫

import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import SUDO_USERS, BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from modules.database.dbchat import (get_served_chats, is_served_chat, add_served_chat)

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    if not await is_served_chat(message.chat.id):
        await add_served_chat(message.chat.id)
    await message.reply_text(f"""**🥀 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐀𝐦 𝐀𝐧 📀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐀𝐧𝐝
𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐕𝐂 𝐏𝐥𝐚𝐲𝐞𝐫 » 𝐅𝐨𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦
𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐀𝐧𝐝 𝐆𝐫𝐨𝐮𝐩𝐬 ✨ ...

💐 𝐅𝐞𝐞𝐥 𝐅𝐫𝐞𝐞 𝐓𝐨 🕊️ 𝐀𝐝𝐝 𝐌𝐞 𝐢𝐧 𝐘𝐨𝐮𝐫
𝐆𝐫𝐨𝐮𝐩, 🌺 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 ❥︎ 𝐒𝐮𝐩𝐞𝐫 𝐇𝐢𝐠𝐡
𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐀𝐮𝐝𝐢𝐨 𝐀𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 🌷 ...

📡 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [𝐁 𝐆 𝐓](https://t.me/BikashGadgetsTech) 💞...**""",
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/BikashGadgetsTech"),

                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=f"https://t.me/Bgt_Chat"),
                ],
                [
                    InlineKeyboardButton(
                        text="🥀 ❰ 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/BikashHalder")
                ]
           ]
        ),
      disable_web_page_preview=True,
     )

    
@Client.on_message(commandpro(["/start", "/alive", "#bgt"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    if not await is_served_chat(message.chat.id):
        await add_served_chat(message.chat.id)
    await message.reply_text(f"""**✅ 𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐌𝐞 𝐈𝐧
𝐂𝐡𝐚𝐭 »  {message.chat.title}

🥀 𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 📀 𝐀𝐧𝐲 𝐐𝐮𝐞𝐫𝐢𝐞𝐬
𝐓𝐡𝐞𝐧 𝐄𝐱𝐩𝐥𝐚𝐢𝐧 💬 𝐓𝐨 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.

💐 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ‖ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
𝐅𝐨𝐫 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐍𝐞𝐰 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 💞...**""",
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 ❰ 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 ❱ ✨", url=f"https://youtube.com/@BikashGadgetsTech"),
                ],
                [
                    InlineKeyboardButton(
                        "📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/BikashGadgetsTech"),

                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=f"https://t.me/Bgt_Chat"),
                ],
                [
                    InlineKeyboardButton(
                        text="💥 ❰ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ❱ 💞", url=f"https://t.me/BikashHalder")
                ]
           ]
        ),
      disable_web_page_preview=True,
     )

welcome_group = 2

@Client.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client: Client, message: Message):
    if not await is_served_chat(message.chat.id):
        await add_served_chat(message.chat.id)
    for member in message.new_chat_members:
        try:
            if member.id == 5237980722:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text("**🥀 𝑷𝒍𝒆𝒂𝒔𝒆 𝑼𝒔𝒆 𝑺𝒖𝒑𝒆𝒓𝒈𝒓𝒐𝒖𝒑 ✨...**")
                    return await client.leave_chat(message.chat.id)
 
                await message.reply_text(f"""**✅ 𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐌𝐞 𝐈𝐧
𝐂𝐡𝐚𝐭 »  {message.chat.title}

🥀 𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 📀 𝐀𝐧𝐲 𝐐𝐮𝐞𝐫𝐢𝐞𝐬
𝐓𝐡𝐞𝐧 𝐄𝐱𝐩𝐥𝐚𝐢𝐧 💬 𝐓𝐨 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.

💐 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ‖ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
𝐅𝐨𝐫 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐍𝐞𝐰 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 💞...**""",
                reply_markup=InlineKeyboardMarkup(
                       [
                           [
                               InlineKeyboardButton(
                                   "🥀 ❰ 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 ❱ ✨", url=f"https://Youtube.com/@BikashGadgetstech"),
                           ],
                           [
                               InlineKeyboardButton(
                                   "📡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/BikashGadgetsTech"),

                               InlineKeyboardButton(
                                   "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💬", url=f"https://t.me/Bgt_Chat"),
                           ],
                           [
                               InlineKeyboardButton(
                                   text="💥 ❰ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ❱ 💞", url=f"https://t.me/BikashHalder")
                           ]
                       ]
                   ),
                 disable_web_page_preview=True,
                )
            if member.id in SUDO_USERS:
                return await message.reply_text(
                    "**🥀 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐎𝐰𝐧𝐞𝐫 𝐉𝐮𝐬𝐭\n𝐉𝐨𝐢𝐧𝐞𝐝 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭 ✨...**"
                )
        except:
            return
