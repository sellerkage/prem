import os

DEVS = [
    5779185981,
]

API_ID = int(os.getenv("API_ID", "27778109"))

API_HASH = os.getenv("API_HASH", "6b0f4197f9f637e17a1466f4de587c07")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7068443168:AAEJ9utUdGe3kuqvbqVz0XfwqiU1vR7lbjg")

OWNER_ID = int(os.getenv("OWNER_ID", "5779185981"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002032983910"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002127258037").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dantesbot:wildan18@cluster0.fol5tml.mongodb.net/?retryWrites=true&w=majority",
)


