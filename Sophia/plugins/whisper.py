from Sophia import HANDLER, SophiaBot, Sophia, qfilter
from pyrogram import *
import logging
from pyrogram.types import *
from config import OWNER_ID
import json
from Sophia import *

@Sophia.on_message(filters.command("whisper", prefixes=HANDLER) & filters.user(OWNER_ID) & ~filters.private & ~filters.bot)
async def whisper(_, message):
    await message.delete()
    if len(message.text.split()) < 2:
        return await message.reply("Please enter a text to whisper!")
    if not message.reply_to_message:
        return await message.reply('Please reply someone to whisper!')
    reply = message.reply_to_message
    data = {
        'n': reply.from_user.first_name,
        'i': reply.from_user.id,
        'm': " ".join(message.command[1:])
    }
    results = await Sophia.get_inline_bot_results(SophiaBot.me.username, f"whisper: {json.dumps(data)}")
    if results.results:
        await message.reply(results)
        await Sophia.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=results.query_id,
            result_id=results.results[0].id,
            reply_to_message=message.reply_to_message_id
        )
    else:
        await message.reply("Error: No result returned by the inline bot.")

@SophiaBot.on_inline_query(qfilter('whisper: '))
async def send_whisper(_, query):
    try:
        data = json.loads(str(query.query).replace('whisper: ', ''))
        logging.info(f'Received yeah data is: {data}')
        button = InlineKeyboardMarkup([[InlineKeyboardButton("View 🔓", callback_data=f"wh: {json.dumps(data)}")]])
        result = InlineQueryResultArticle(
            title="Whisper message",
            input_message_content=InputTextMessageContent(
                f"🔒 A whisper message to {data['n']}, Only he/she can open it."
            ),
            reply_markup=button
        )
        await query.answer([result])
    except Exception as e:
        logging.error(e)

MOD_NAME = 'Whisper'
MOD_HELP = "Beta module help updated soon!"
