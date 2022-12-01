# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "")

# Account
API_HASH = os.environ.get("API_HASH", "56ac06547b5d8af50493e104feed8053")
API_ID = os.environ.get("API_ID", "4011894")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5530408302:AAHGwD_ePg4yVRG9uBmgvYvJOYyu4erG_e0")
PICS = os.environ.get("PICS", "https://telegra.ph/file/78501ede09af36c54b3ed.jpg https://telegra.ph/file/9f5a7d04c67972b41e994.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://JD2021:JD2021@cluster0.zweu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COLLECTION_NAME = environ.get("COLLECTION_NAME ", "Telegram_files")

# Chats & Users
ADMINS = os.environ.get("ADMINS", "739667270")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "freakersmovie")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001528080426")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001704828885").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001555083458")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "3600"))
IMDB = is_enabled((environ.get('IMDB', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "ᴛɪᴛʟᴇ: <code>{file_name}</code>\n▬▬▬▬▬▬▬▬▬▬▬▬\n🍃<b><i>Movies Update Channel</b></i>🍃\n<i>@freakersmovie</i>\n🍃<b><i>Series Update Channel</b></i>🍃\n<i>@freakers_series</i>\n▬▬▬▬▬▬▬▬▬▬▬▬\n☘𝙅𝙤𝙞𝙣:-<b><i>https://t.me/freakersmovie</b></i>\n\n🧐𝙁𝙧𝙚𝙖𝙠𝙚𝙧𝙨🎭𝙁𝙞𝙡𝙢𝙮™🍿©\n100% ғᴀꜱᴛ & ϙᴜᴀʟɪᴛʏ\n▬▬▬▬▬▬▬▬▬▬▬▬ ")

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '739667270').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "5")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 

## EXTRA FEATURES ##
    
# URL Shortener

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'zagl.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'fd7b48e8dec726625b921cc5f44f582892246672')
