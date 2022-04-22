from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}, 
Welcome to {}

You Can Use This Bot To Generate Pyrogram & Telethon String Session. Use Below Buttons To Operate !

**Made With Love By @WarFade ❤️**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    saved_msg = [
        [InlineKeyboardButton("🔰 Click To Go To Saved Message 🔰", url="tg://openmessage?user_id={chat_id}")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("❣️ Contact Owner ❣️", url="https://t.me/WarFade")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/start - Start The Bot
/help - Help Message
/generate - Start Generating Session
/cancel - Cancel The Process
/about - About Bot
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram & Telethon String Sessions. 

Made With ❤ By @WarFade

Sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : [Click Here](https://t.me/WarFade)

Fʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

Lᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

Dᴇᴠᴇʟᴏᴘᴇʀ : @WarFade
    """
