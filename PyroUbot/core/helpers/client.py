from pyrogram import filters

from PyroUbot import *


class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user(OWNER_ID)
    ME_GROUP = filters.me & filters.group
    ME_USER = filters.me & filters.user(USER_ID)
    # ME_DEVS = filters.me & filters.user(DEVS)


class PY:
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, sudo=False):
        def wrapper(func):
            sudo_command = anjay(command) if sudo else anjay(command) & filters.me

            @ubot.on_message(filters.command(command, "^") & FILTERS.ME_USER)
            @ubot.on_message(sudo_command)
            async def wrapped_func(client, message):
                if sudo:
                    sudo_id = await ambil_list_var(client.me.id, "SUDO_USER", "ID_NYA")
                    if client.me.id not in sudo_id:
                        sudo_id.append(client.me.id)
                    if message.from_user.id in sudo_id:
                        return await func(client, message)
                else:
                    return await func(client, message)

            return wrapped_func

        return wrapper

    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def AFK(afk_no):
        def wrapper(func):
            afk_check = (
                (filters.mentioned | filters.private)
                & ~filters.bot
                & ~filters.me
                & filters.incoming
                if afk_no
                else filters.me & ~filters.incoming
            )

            @ubot.on_message(afk_check)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def LOGS_PRIVATE():
        def wrapper(func):
            @ubot.on_message(
                filters.private
                & ~filters.me
                & ~filters.bot
                & ~filters.service
                & filters.incoming,
                group=6,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def LOGS_GROUP():
        def wrapper(func):
            @ubot.on_message(
                filters.group & filters.incoming & filters.mentioned & ~filters.bot,
                group=8,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
