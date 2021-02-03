# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = "c5dc866de8b2cc5d7fb136d237b44c84"
API_HASH = "2094259"

# Get this from @Botfather
TOKEN = "1638441687:AAGDX_kO5t58Y1m-Ort3SHLLF9GLsbAid1s" #check it 

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb+srv://dinesh:dinesh@vcpb.b6rws.mongodb.net/<dbname>?retryWrites=true&w=majority"

#mongodb+srv://dinesh:<password>@vcpb.b6rws.mongodb.

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    750058161,
    969558971,
    1474412633,
    1396811125,
    1063201961,
    1202955973,
    1303669398
]

# The ID of the group where your bot streams
GROUP = -1001337579514

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 60

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
