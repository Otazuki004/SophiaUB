from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
import requests

@bot.on_message(filters.command("ud", prefixes=HANDLER) & filters.user(OWNER_ID))
async def urban_dictionary(_, message):
        if len(message.command) < 2:
             return await bot.send_message(message.chat.id, "where you input the text?")         
        text = message.text.split(None, 1)[1]
        try:
          results = requests.get(
            f'https://api.urbandictionary.com/v0/define?term={text}').json()
          reply_text = f"""
**Results for**: {text}

**Defination**:
{results["list"][0]["definition"]}\n
**Example:**
{results["list"][0]["example"]}
"""
        except Exception as e:
              if str(e) == "list index out of range":
                  await message.reply("I can't find it in Urban dictionary.")
                  return
              return await bot.send_message(message.chat.id, f"Somthing wrong Happens:\n`{e}`")
        ud = await bot.send_message(message.chat.id, "Exploring....")
        await ud.edit_text(reply_text)

MOD_NAME = "UD"
MOD_HELP = ".ud <word> - To get definition of that word!"
