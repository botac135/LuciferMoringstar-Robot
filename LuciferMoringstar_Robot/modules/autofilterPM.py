# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE

import re, random, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from LuciferMoringstar_Robot import temp, PICS, REQUEST_MOVIE, SINGLE_BUTTON, MOVIE_TEXT
from LuciferMoringstar_Robot.functions import get_size, split_list, get_settings
from database.autofilter_mdb import get_filter_results

async def pm_filters(client, update):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", update.text):
        return
    if 2 < len(update.text) < 100:    
        btn = []
        search = update.text
        settings = await get_settings(update.chat.id)
        MOVIE_TEXT = settings["template"]
        files = await get_filter_results(query=search)
        if not files:
            if settings["spellmode"]:
                try:
                    reply = search.replace(" ", '+')  
                    buttons = [[ InlineKeyboardButton("𝑮𝒐𝒐𝒈𝒍𝒆 𝑺𝒆𝒂𝒓𝒄𝒉 🔎", url=f"https://www.google.com/search?q={reply}") ],[ InlineKeyboardButton("𝑮𝒆𝒕 𝑺𝒆𝒓𝒊𝒆𝒔 𝑶𝒏𝒍𝒚🍃", url=f"https://t.me/FF_Series_Only") ],[ InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🗑️", callback_data="close") ]]
                    spell = await update.reply_text(text=settings["spelltext"].format(query=search, first_name=update.from_user.first_name, last_name=update.from_user.last_name, title=update.chat.title, mention=update.from_user.mention), disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))           
                    await asyncio.sleep(60)
                    await spell.delete()
                except:
                    pass
            return
        if files:
            for file in files:
                file_id = file.file_id
                filesize = f"[{get_size(file.file_size)}]"
                filename = f"{file.file_name}"
                if SINGLE_BUTTON:
                    btn.append(
                        [InlineKeyboardButton(text=f"{filename}", callback_data=f"luciferPM#{file_id}"),
                         InlineKeyboardButton(text=f"{filesize}", callback_data=f"luciferPM#{file_id}")]
                    )
                else:
                    btn.append(
                        [InlineKeyboardButton(text=f"{filesize}", callback_data=f"luciferPM#{file_id}"),
                         InlineKeyboardButton(text=f"{filename}", callback_data=f"luciferPM#{file_id}")]
                    )
        else:
            return

        if not btn:
            return

        if len(btn) > temp.filterBtns: 
            btns = list(split_list(btn, temp.filterBtns)) 
            keyword = f"{update.chat.id}-{update.id}"
            temp.BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📂 Pages 1/1",callback_data="pages"),
                 InlineKeyboardButton("𝘾𝙡𝙤𝙨𝙚 🗑️", callback_data="close")]
            )


            if REQUEST_MOVIE:
                Del = await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await Del.delete()
            else:
                Del = await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await Del.delete()
            return

        data = temp.BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
    
        buttons.append(
            [InlineKeyboardButton(text=f"📂 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("🗑️", callback_data="close"),
             InlineKeyboardButton(text="𝙉𝙚𝙭𝙩👉",callback_data=f"nextbot_0_{keyword}")]
        )
        
        if REQUEST_MOVIE:
            Del = await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await Del.delete()
        else:
            Del = await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await Del.delete()
