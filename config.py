import os

settings = {
    "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN"),
    "ROLE_NAME": os.getenv("ROLE_NAME", "MyRole"),
    "EMOJI_NAME": os.getenv("EMOJI", "✅"),
    "EMOJi_ID": os.getenv("EMOIJ_ID"),
    "CHANNEL_ID": int(os.getenv("CHANNEL_ID", "123456789012345678")),
    "REACTION_MESSAGE_TEXT": os.getenv("REACTION_MESSAGE_TEXT", "React with ✅ to get the role!")
}
