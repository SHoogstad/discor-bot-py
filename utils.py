
from config import settings
from discord.utils import get

# You could store message ID in a database or a file if persistence is needed
reaction_message_id = None

async def send_reaction_role_message(bot):
    global reaction_message_id
    channel = bot.get_channel(settings["CHANNEL_ID"])
    if not channel:
        print("Channel not found")
        return

    message = await channel.send(settings["REACTION_MESSAGE_TEXT"])
    emoji = f'<:{settings["EMOJI_NAME"]}:{settings["EMOJI_ID"]}>'
    await message.add_reaction(emoji)
    reaction_message_id = message.id
    print(f"Sent reaction role message: {message.id}")


def get_member(bot, payload):
    if is_correct_emoji(payload):
        return

    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return

    role = get(guild.roles, name=settings["ROLE_NAME"])
    member = guild.get_member(payload.user_id)
    return member, role

def is_correct_emoji(payload):
    return (
        payload.emoji.name == settings["EMOJI_NAME"] and
        str(payload.emoji.id) == settings["EMOJI_ID"]
    )