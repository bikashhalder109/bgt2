import asyncio
import speedtest

from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command
from modules.helpers.decorators import sudo_users_only


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**🥀 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝑺𝒑𝒆𝒆𝒅 ✨...**")
        test.download()
        m = m.edit("**🥀 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑼𝒑𝒍𝒐𝒂𝒅 𝑺𝒑𝒆𝒆𝒅 ✨...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**🥀 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 ✨...**")
    except Exception as e:
        return m.edit(e)
    return result


@Client.on_message(command("speedtest"))
@sudo_users_only
async def speedtest_function(client: Client, message: Message):
    m = await message.reply_text("**🥀 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 ✨...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**🥀 𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 ✨...**
    
<u>**𝐂𝐥𝐢𝐞𝐧𝐭:**</u>
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
<u>**𝐒𝐞𝐫𝐯𝐞𝐫:**</u>
**𝑵𝒂𝒎𝒆:** {result['server']['name']}
**𝑪𝒐𝒖𝒏𝒕𝒓𝒚:** {result['server']['country']}, {result['server']['cc']}
**𝑺𝒑𝒐𝒏𝒔𝒐𝒓:** {result['server']['sponsor']}
**𝑳𝒂𝒕𝒆𝒏𝒄𝒚:** {result['server']['latency']}  
**𝑷𝒊𝒏𝒈:** {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
