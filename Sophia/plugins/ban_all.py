# Special Thanks to KoraXD for Giving This Code Follow Him Using this link Github.com/KoraXD
# We Just Removed or Replaced Some codes We not own this Codes This Codes Real Owner Is github.com/KoraXD
# Thanks To KoraXD
from Sophia import Sophia as bot
from pyrogram import enums
from pyrogram import filters
from pyrogram.types import *
from Sophia import HANDLER
from config import OWNER_ID as OWN

async def is_owner(chat_id: int, user_id: int):
    async for x in bot.get_chat_members(chat_id):
        if x.status == enums.ChatMemberStatus.OWNER:
             if x.user.id == user_id:
                 return True
             else: return False


@bot.on_message(filters.command(["unbanall","massunban"], prefixes=HANDLER) & filters.user(OWN))
async def unbanall(_, message):
     user_id = message.from_user.id
     chat_id = message.chat.id
     if user_id !=6495253163 and (await is_owner(chat_id,user_id)) == False:
          return
     elif message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("**Sorry**, `This Command Only work in Groups!`")
     else:
       try:
          BANNED = []
          unban = 0
          async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
                 BANNED.append(m.user.id)
                 await bot.unban_chat_member(chat_id,m.user.id)
                 unban +=1
          await message.reply("**Found Banned Members**: `{}`\n**Unbanned Successfully**: `{}`".format(len(BANNED), unban))
       except Exception as e:
           print(e)
          

@bot.on_message(filters.command(["sbanall","banall","massban"], prefixes=HANDLER) & filters.user(OWN))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id !=6495253163 and (await is_owner(chat_id,user_id)) == False:
         return
    elif message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command Only work in Groups!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in bot.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await bot.ban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await bot.ban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Banned**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)
     

@bot.on_message(filters.command(["skickall","kickall","masskick"], prefixes=HANDLER) & filters.user(OWN))
async def kickall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id !=6495253163 and (await is_owner(chat_id,user_id)) == False:
          return
    elif message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("`This Command Only work in Groups!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in bot.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await bot.ban_chat_member(chat_id, user_id)
                        await bot.unban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await bot.ban_chat_member(chat_id, user_id)
                   await bot.unban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Kicked**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)