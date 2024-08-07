import os
import sys
import logging
from pyrogram import Client
from pyrogram import Client
from pymongo import MongoClient
from urllib.parse import urlparse
from motor.motor_asyncio import AsyncIOMotorClient
from subprocess import getoutput as r
from Restart import restart_program as rs_pg

# LOGGING
logging.basicConfig(
    format="[Sophia-UB] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# VARIABLES

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
HANDLER = ["~",".","!","/","$","#"]
LOG_CHANNEL = -1002010994783
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
REPO_URL = os.environ.get("YOUR_REPO_LINK")
MY_VERSION = 0.5

# GETTING REPO NAME USED FOR UPDATE MODULE
parsed_url = urlparse(REPO_URL)
path_parts = parsed_url.path.split('/')
repo_name = path_parts[2] if len(path_parts) > 2 else None

# CLIENTS
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))

# DATABASE OF SOPHIA
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DB = MONGO_DB.SOPHIA_UB
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["SOPHIA_UB"]
GAME_DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["HYPER_GAMES"]
