from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import bot as BotBase

PREFIX = "+"
OWNER_IDS = [193922557513170944]

class Bot(BotBase):
    def init(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().init(command_prefix = PREFIX, owner_ids = OWNER_IDS)
    def run(self, version):
        self.VERSION = version
        with open(".lib/bot/token", "r", encoding"utf-8) as tf:
            self.TOKEN = tf.read()
        print("Running bot...")
        super().run(self.TOKEN, reconnect = true)
    async def on_connect(self):
        print("Bot connected")
    async def on_disconnect(self):
        print("Bot disconnect")
    async def on_ready(self):
        if not self.ready:
            print("bot ready")
            self.ready = True
            self.guild = self.get_guild(722687809483440150)
        elif:
            print("Bot reconnected.")
    async def on_message(self, message):
        pass
    
    bot = Bot(BotBase) 