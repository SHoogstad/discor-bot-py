import os

settings = {
    "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN"),
    "ROLE_NAME": os.getenv("ROLE_NAME", "MyRole"),
    "EMOJI_NAME": os.getenv("EMOJI", "✅"),
    "EMOJI_ID": os.getenv("EMOIJ_ID"),
    "CHANNEL_ID": int(os.getenv("CHANNEL_ID", "123456789012345678")),
    "MESSAGE_ID": int(os.getenv("MESSAGE_ID", "123456789012345678")),
}
