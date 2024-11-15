# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
    "https://files.catbox.moe/kmlghn.jpg",
]

HEY_IMG = "https://files.catbox.moe/eekbgf.jpg"

ALIVE_ANIMATION = [
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
    "https://files.catbox.moe/eekbgf.jpg",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* {} . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ hinata, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Planetsadala"),
        ib(text="SUPPORT", url="https://t.me/lolpagalokigc"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *hinata-robot* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
