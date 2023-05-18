# Aditya Halder

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("**✅ 𝑫𝒆𝒍𝒆𝒕𝒆𝒅 𝑨𝒍𝒍 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒅\n 𝑱𝒖𝒏𝒌 𝑭𝒊𝒍𝒆𝒔 ✨...**")
    else:
        await message.reply_text("**✅ 𝑨𝒍𝒓𝒆𝒂𝒅𝒚 𝑪𝒍𝒆𝒂𝒏𝒆𝒅 ✨...**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("**✅ 𝑫𝒆𝒍𝒆𝒕𝒆𝒅 𝑨𝒍𝒍 𝑹𝒂𝒘\n 𝑳𝒐𝒈 𝑭𝒊𝒍𝒆𝒔 ✨...**")
    else:
        await message.reply_text("**✅ 𝑨𝒍𝒓𝒆𝒂𝒅𝒚 𝑪𝒍𝒆𝒂𝒏𝒆𝒅 ✨...**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("**✅ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝑪𝒍𝒆𝒂𝒏𝒆𝒅\n 𝑱𝒖𝒏𝒌 𝑰𝒎𝒂𝒈𝒆𝒔 ✨...**")
    else:
        await message.reply_text("**✅ 𝑨𝒍𝒓𝒆𝒂𝒅𝒚 𝑪𝒍𝒆𝒂𝒏𝒆𝒅 ✨...**")
