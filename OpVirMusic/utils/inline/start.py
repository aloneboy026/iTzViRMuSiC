from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛦ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛦",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⛦ Hᴇʟᴩ ⛦",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⛦ Sᴇᴛᴛɪɴɢs ⛦", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛦ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛦",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⛦ Hᴇʟᴩ ⛦", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="⛦ Sᴜᴩᴩᴏʀᴛ ⛦", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="⛦ Oᴡɴᴇʀ ⛦", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="⛦ Sᴏᴜʀᴄᴇ ⛦", callback_data="gib_source"
            )
        ],
     ]
    return buttons
