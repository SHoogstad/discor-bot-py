import discord
from discord.ext import commands
from config import settings
from handlers import setup_reaction_handlers
from utils import send_reaction_role_message

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    await send_reaction_role_message(bot)

setup_reaction_handlers(bot)

bot.run(settings["DISCORD_TOKEN"])
