#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25350365
API_HASH = "f4a2c0d9141b46f5f247b51dd7a27838"
BOT_TOKEN = "5670133858:AAFirg4XtIEOCVquohIHHWS5MWgYA1BxsDI"
SESSION = "BQB00ai1cQNzMo6-59p_XuhvGFMvhvJPoFJtpKPGDw3MC67WByyMXt7wmp62mqcXzP-2Eqmlp9yYWTY7gSaSrRQlBrI5UgtBSwttcxkEwD7KLJIhusC6FS4r7pRIy0t2ltRpXPvzyO-MQq4b_PZh3pzDb2_FLTrFTlLL-Ba8nt0BFNk4URHUvs1J4eLS3iOBFDFxOfE9DK3jqjA9hRKWQxF7sc0CAuJL8JP1TgD6bhiDR-fqq0e9LgxNzUQWwXTS2iR1EliitiLb_Y3FYLB-zciUfgNBsykoxhsLycQul_HISs-0nYjTDRrNgHt2GOaXzvrGw5E4Dj3EtQ7bNYF0OXE2cBkP_wA"
FORCESUB = "abczdde"
AUTH = "1880690687"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
