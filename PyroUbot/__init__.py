import asyncio
import logging
import os
import re

from aiohttp import ClientSession
from pyrogram import *
from pyrogram.enums import *
from pyrogram.handlers import *
from pyrogram.types import *
from pyromod import listen

from PyroUbot.config import *

aiosession = ClientSession()

import logging
from os import execvp
from sys import executable


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSError"]:
            if X in record.getMessage():
                execvp(executable, [executable, "-m", "PyroUbot"])


logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)


class Ubot(Client):
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    # _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.device_model = "kageimuet"

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[self.me.id] = prefix

    async def start(self):
        await super().start()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = ["."]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = {"negara": "id"}
        print(f"Starting Userbot ({self.me.id}|{self.me.first_name})")

    async def stop(self):
        await super().stop()


async def get_prefix(user_id):
    return ubot._prefix.get(user_id, ".")


def anjay(cmd):
    command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

    async def func(_, client, message):
        if message.text and message.from_user:
            text = message.text.strip()
            username = client.me.username or ""
            prefixes = await get_prefix(client.me.id)

            if not text:
                return False

            for prefix in prefixes:
                if not text.startswith(prefix):
                    continue

                without_prefix = text[len(prefix) :]

                for command in cmd.split("|"):
                    if not re.match(
                        rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                        without_prefix,
                        flags=re.IGNORECASE | re.UNICODE,
                    ):
                        continue

                    without_command = re.sub(
                        rf"{command}(?:@?{username})?\s?",
                        "",
                        without_prefix,
                        count=1,
                        flags=re.IGNORECASE | re.UNICODE,
                    )
                    message.command = [command] + [
                        re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                        for m in command_re.finditer(without_command)
                    ]

                    return True

        return False

    return filters.create(func)


ubot = Ubot(name="ubot", api_id=API_ID, api_hash=API_HASH, device_model="kage")


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            name="bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=20,
            device_model="KageLoveyou",
        )

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


bot = Bot()


from PyroUbot.core.database import *
from PyroUbot.core.function.plugins import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
