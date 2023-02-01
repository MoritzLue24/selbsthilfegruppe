import sys, threading, json, logging, discord, PloudosAPI
from discord.ext import commands


logger = logging.getLogger("bot")

class Management(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        with open("config.cfg", "r") as f:
            cfg = json.loads(f.read())

        session = PloudosAPI.login(cfg["ploudos"]["username"], cfg["ploudos"]["password"])
        servers = session.get_servers_with_name(cfg["ploudos"]["server-name"])
        try:
            self.server = servers[0]
        except IndexError:
            logger.critical("Server with name '{cfg['ploudos']['server-name']}' not found.")
            sys.exit(1)


    @commands.command()
    @commands.has_role("Server Minecraft")
    async def start(self, ctx: commands.Context):
        logger.info(f"'{ctx.message.author}' requested a server start")
        threading.Thread(target=self.server.start).start()
        embed = discord.Embed(
            title="Server wird gestartet",
            description="Das kann ca. eine Minute dauern  :hourglass:",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_role("Server Minecraft")
    async def stop(self, ctx: commands.Context):
        logger.info(f"'{ctx.message.author}' requested a server stop")
        threading.Thread(target=self.server.stop).start()
        embed = discord.Embed(
            title="Server wird gestoppt",
            description="Das kann ca. eine Minute dauern  :hourglass:",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    logger.info("Cog loaded: 'Management'")
    await bot.add_cog(Management(bot))
