import os

class Config():
  # Bot Token (Use @BotFather)
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6076322205:AAE6oPAceDbkFdPx4Pk5jEm_I48h2fv9dnw")

  # Bot Updates Channel Username (without @)
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "rainbowmoviechannel")

  # PostgresSQL DB URL (Use ElephantSQL)
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://mqabrbpk:Azt6duncFNbKQrz4mBU4czCOcvlrZzxy@floppy.db.elephantsql.com/mqabrbpk")

  # API & HASH (Use my.telegram.org)
  APP_ID = os.environ.get("APP_ID", "6691216")
  API_HASH = os.environ.get("API_HASH", "56170666b4adfa400f7ef9f18f1fe6f3")

  # Sudo users (Put your User ID)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1661916733").split()))
  SUDO_USERS.append(5524391658)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**🤖 RMC - Force Subscribe Bot**\n\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**⚙️ Setup**\n\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**🎲 Commmands**\n\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**👨‍💻 Developed By @nas0055**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
