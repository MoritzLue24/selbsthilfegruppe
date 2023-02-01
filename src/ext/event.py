import sys, json, discord, logging, PloudosAPI
from discord.ext import commands, tasks


logger = logging.getLogger("bot")

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        with open("config.cfg", "r") as f:
            self.cfg = json.loads(f.read())
        self.session = PloudosAPI.login(self.cfg["ploudos"]["username"], self.cfg["ploudos"]["password"])
 

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"Logged in as {self.bot.user}")
        self.status.start()


    @tasks.loop(seconds=1)
    async def status(self):
        # Get server status
        servers = self.session.get_servers_with_name(self.cfg["ploudos"]["server-name"])
        try:
            server = servers[0]
        except IndexError:        
            logger.critical(f"Server with name '{self.cfg['ploudos']['server-name']}' not found.")
            sys.exit(1)
       
        # Change discord status
        if hasattr(server, "isRunning") and server.isRunning:
            players = server.onlineCount
            max_players = server.onlineMax
            activity = discord.Game(name=f"Online, {players}/{max_players}", type=3)
            await self.bot.change_presence(status=discord.Status.online, activity=activity)
        else:
            activity = discord.Game(name=f"Gestoppt", type=3)
            await self.bot.change_presence(status=discord.Status.dnd, activity=activity)


async def setup(bot: commands.Bot):
    logger.info("Cog loaded: 'Event'")
    await bot.add_cog(Event(bot))
