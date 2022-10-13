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
from LuciferMoringstar_Robot import temp, PICS, REQUEST_MOVIE, SINGLE_BUTTON, MOVIE_TEXT, MOVIE_TXT
from LuciferMoringstar_Robot.functions import get_size, split_list, get_settings
from database.autofilter_mdb import get_filter_results, get_poster


async def pm_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        settings = await get_settings(message.chat.id)
        MOVIE_TEXT = settings["template"]
        files = await get_filter_results(query=search)
        if not files:
            if settings["spellmode"]:
                try:
                    reply = search.replace(" ", '+')  
                    buttons = [[ InlineKeyboardButton("𝑮𝒐𝒐𝒈𝒍𝒆 𝑺𝒆𝒂𝒓𝒄𝒉 🔎", url=f"https://www.google.com/search?q={reply}") ],[ InlineKeyboardButton("𝑮𝒆𝒕 𝑺𝒆𝒓𝒊𝒆𝒔🍃", url=f"https://t.me/freakersfilmy") ],[ InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🗑️", callback_data="close") ]]
                    spell = await message.reply_text(text=settings["spelltext"].format(query=search, first_name=message.from_user.first_name, last_name=message.from_user.last_name, title=message.chat.title, mention=message.from_user.mention), disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))           
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
                        [InlineKeyboardButton(text=f"{filesize}", callback_data=f"luciferPM#{file_id}"),
                         InlineKeyboardButton(text=f"{filename}", callback_data=f"luciferPM#{file_id}")]
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
            keyword = f"{message.chat.id}-{message.id}"
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
                imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MOVIE_TEXT.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            elif imdb:
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MOVIE_TEXT.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            else:
                dell=await message.reply_photo(photo=random.choice(PICS), caption=MOVIE_TXT.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")

            return

        data = temp.BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
    
        buttons.append(
            [InlineKeyboardButton(text=f"📂 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("🗑️", callback_data="close"),
             InlineKeyboardButton(text="𝙉𝙚𝙭𝙩👉",callback_data=f"nextbot_0_{keyword}")]
        )
        
        if REQUEST_MOVIE:
            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MOVIE_TEXT.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            elif imdb:
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MOVIE_TEXT.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")
            else:
                dell=await message.reply_photo(photo=random.choice(PICS), caption=MOVIE_TXT.format(mention=message.from_user.mention, query=search, greeting=None, group_name = f"[{message.chat.title}](t.me/{message.chat.username})" or f"[{message.chat.title}](t.me/{message.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"⚙️ Filter For {search} Closed 🗑️")

