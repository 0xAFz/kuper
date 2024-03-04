import time
from pyrogram import Client, filters
from pyrogram.types import Message
from configparser import ConfigParser

conf = ConfigParser()
conf.read("config.ini")

app = Client(
    name="kuper",
    api_id=conf.get("account", "api_id"),
    api_hash=conf.get("account", "api_hash"),
    phone_number=conf.get("account", "phone_number")
)

async def main():
    async with app:
        from_chat = "me"
        to_chat   = "another chat"

        messages  = []

        async for message in app.get_chat_history(from_chat):
            messages.append(message)

        messages.reverse()

        for message in messages:
            await app.forward_messages(to_chat, from_chat, message.id)
            time.sleep(2)


app.run(main())
