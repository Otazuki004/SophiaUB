from Sophia import *
from pyrogram import filters

@Sophia.on_message(filters.command(['del', 'delete', 'd'], prefixes=HANDLER) & filters.me)
async def message_del(_, message):
  if message.reply_to_message:
    await Sophia.delete_messages(message.chat.id, message.reply_to_message.id)
    await Sophia.delete_messages(message.chat.id, message.id)
  else:
    message_id = " ".join(message.command[1:])
    if message_id.isdigit():
      await Sophia.delete_messages(message.chat.id, int(message_id), revoke=True)
      await Sophia.delete_messages(message.chat.id, message.id, revoke=True)
    else:
      await message.reply_text("Please reply to a message or enter a valid message id.")