from discord.utils import get
from config import settings
from utils import get_member


def setup_reaction_handlers(bot):
    @bot.event
    async def on_raw_reaction_add(payload):
        member, role = get_member(bot, payload)

        if role and member and not member.bot:
            await member.add_roles(role)
            print(f"Added role to {member.name}")

    @bot.event
    async def on_raw_reaction_remove(payload):
        member, role = get_member(bot, payload)

        if role and member:
            await member.remove_roles(role)
            print(f"Removed role from {member.name}")
