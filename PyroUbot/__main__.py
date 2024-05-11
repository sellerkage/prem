import asyncio

from pyrogram import idle

from PyroUbot import *
from PyroUbot.core.function.expired import *


async def handle_timeout_error(user_id):
    await remove_ubot(user_id)
    await add_prem(user_id)
    await rm_all(user_id)
    await rem_pref(user_id)
    await rem_uptime(user_id)
    for chat_id in await get_chat(user_id):
        await remove_chat(user_id, chat_id)
    await sending_user(user_id)
    print(f"[INFO] - ({user_id}) TIMEOUT ERROR - BOT REMOVED")


async def handle_general_error(user_id, error):
    await remove_ubot(user_id)
    await rm_all(user_id)
    await rem_pref(user_id)
    await rem_uptime(user_id)
    await rem_expired_date(user_id)
    for chat_id in await get_chat(user_id):
        await remove_chat(user_id, chat_id)
    print(f"✅ {user_id} BOT ERROR: {error}")


async def start_user_bot(user_id, userbot_data):
    ubot = Ubot(**userbot_data)
    try:
        await asyncio.wait_for(ubot.start(), timeout=30)
        chat_list = ["suportkage", "kagestore69"]
        for chat_name in chat_list:
            await ubot.join_chat(chat_name)
    except asyncio.TimeoutError:
        await handle_timeout_error(user_id)
    except Exception as e:
        await handle_general_error(user_id, e)


async def main():
    tasks = [
        asyncio.create_task(start_user_bot(int(userbot_data["name"]), userbot_data))
        for userbot_data in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), expiredUserbots(), idle())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
