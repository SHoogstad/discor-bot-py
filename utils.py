from discord.utils import get
from config import settings

async def send_reaction_role_message(bot):
    channel = bot.get_channel(settings["CHANNEL_ID"])
    if not channel:
        print("Channel not found")
        return

    try:
        message = await channel.fetch_message(settings["MESSAGE_ID"])
    except Exception as e:
        print(f"Failed to fetch message: {e}")
        return

    emoji_obj = bot.get_emoji(settings["EMOJI_ID"])
    if emoji_obj:
        await message.add_reaction(emoji_obj)
        print(f"✅ Added emoji to message {message.id}")
    else:
        # fallback: raw emoji string, only works if emoji is public and bot has access
        emoji_str = f"<:{settings['EMOJI_NAME']}:{settings['EMOJI_ID']}>"
        try:
            await message.add_reaction(emoji_str)
            print(f"✅ Added emoji string to message {message.id}")
        except Exception as e:
            print(f"❌ Failed to react with emoji: {e}")

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
