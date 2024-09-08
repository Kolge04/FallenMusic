from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12210813"))
API_HASH = getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")

BOT_TOKEN = getenv("BOT_TOKEN", "6062022905:AAFjFdASrtYtMokfFwJwvtkgf0rhgG9Nlj0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5663585448"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b7939203c81ffee91e1a1.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c3166102f1c949f1ea0f3.jpg")

SESSION = getenv("SESSION", "AgC8aomShgbZSJVtRY4sTjZ-DxKpaXt3hXs9dutuYV3UhJ4dheFZ1hTSuH75QST6VPwKpmh8r4zzaXt4yYXCAUSLSImzmls6kc7cStIrekeSuAOq_Vq2zs2nh2hlcbBS15VCQB3htuxpgGoHOEXOVxgZDGCjlm3Pta0BsyhWj8nJRCXAGUmaX9Gvjr0BOlmPPfIWrkofhlVhM2yo8YygWqebOOu7yJuIVf3GuYkqGdsmudSq2tbNMVZ-SRoQqVISbOrhDo4SLbjL9Jpt5jpwM7R8Fye7Dj7-uF9JxltwbuVR7465dIr73-swxQm-9fGFrrlZHEEXLwZwlHHfGpLDPySuAAAAAX_r4P0A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kayfina")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XaosResmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5871660730").split()))


FAILED = "https://telegra.ph/file/c3166102f1c949f1ea0f3.jpg"
