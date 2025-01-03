from Sophia import *
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import OWNER_ID
import logging

@Sophia.on_message(filters.command("ban", prefixes=HANDLER) & filters.user("me"))
async def ban(_, message):
    me = await Sophia.get_chat_member(message.chat.id, "me")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == me.user.id:
            return await message.reply("You can't ban yourself!")
        if me.status == ChatMemberStatus.MEMBER or not me.privileges.can_restrict_members:
            return await message.reply("You don't have enough rights to do this 🚫")
        try:
            await Sophia.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply("✅ Successfully banned.")
        except Exception as e:
            logging.error(e)
            await message.reply(f"Error: {e}")
    else:
        if len(message.command) < 2:
            return await message.reply("Reply to a user or enter their user ID to ban!")
        user_id = str(message.text.split(None, 1)[1])
        try:
            target = await Sophia.get_chat_member(message.chat.id, user_id)
        except:
            return await message.reply("Invalid user ID. Please reply to a user or enter their ID correctly!")
        if me.status == ChatMemberStatus.MEMBER or not me.privileges.can_restrict_members:
            return await message.reply("You don't have enough rights to do this 🚫")
        if target.user.id == OWNER_ID:
            return await message.reply("You can't ban yourself!")
        try:
            await Sophia.ban_chat_member(message.chat.id, target.user.id)
            await message.reply("✅ Successfully banned.")
        except Exception as e:
            logging.error(e)
            await message.reply(f"Error: {e}")

@Sophia.on_message(filters.command("unban", prefixes=HANDLER) & filters.user("me"))
async def unban(_, message):
    me = await Sophia.get_chat_member(message.chat.id, "me")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == me.user.id:
            return await message.reply("You can't unban yourself!")
        if me.status == ChatMemberStatus.MEMBER or not me.privileges.can_restrict_members:
            return await message.reply("You don't have enough rights to do this 🚫")
        try:
            await Sophia.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply("✅ Successfully unbanned.")
        except Exception as e:
            logging.error(e)
            await message.reply(f"Error: {e}")
    else:
        if len(message.command) < 2:
            return await message.reply("Reply to a user or enter their user ID to unban!")
        user_id = str(message.text.split(None, 1)[1])
        try:
            user = await Sophia.get_users(user_id)
        except:
            return await message.reply("Invalid user ID. Please reply to a user or enter their ID correctly!")
        if me.status == ChatMemberStatus.MEMBER or not me.privileges.can_restrict_members:
            return await message.reply("You don't have enough rights to do this 🚫")
        if user.id == OWNER_ID:
            return await message.reply("You can't unban yourself!")
        try:
            await Sophia.unban_chat_member(message.chat.id, user.id)
            await message.reply("✅ Successfully unbanned.")
        except Exception as e:
            logging.error(e)
            await message.reply(f"Error: {e}")
            