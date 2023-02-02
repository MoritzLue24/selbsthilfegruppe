import sys, os, json, asyncio, logging, discord, PloudosAPI
from logging.config import dictConfig
from discord.ext import commands, tasks


if __name__ == "__main__":
    with open("config.cfg", "r") as f:
        cfg = json.loads(f.read())
    dictConfig(cfg["logging"])

    logger = logging.getLogger("bot")
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot("!", intents=intents)

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def reload(ctx: commands.Context):
        for ext in os.listdir("src/ext"):
            if ext.endswith(".py"):
                logger.info(f"Reloading extension: '{ext[:-3]}'")
                await bot.reload_extension(f"ext.{ext[:-3]}")

        embed = discord.Embed(
            title="Alle Erweiterungen wurden neu geladen.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
 
    # Load extensions 
    for ext in os.listdir("src/ext"):
        if ext.endswith(".py"):
            logger.info(f"Loading extension: '{ext[:-3]}'")
            asyncio.run(bot.load_extension(f"ext.{ext[:-3]}"))

    bot.run(cfg["discord"]["token"], root_logger=True)

