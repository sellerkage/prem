import os

DEVS = [
    6528348225,
]

API_ID = int(os.getenv("API_ID", "26477680"))

API_HASH = os.getenv("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6760468989:AAFWj-F-CbveMXRRJVsUxneAfCpxRnhB7x4")

OWNER_ID = int(os.getenv("OWNER_ID", "6528348225"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002040006265"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002127258037").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://thomasshelby:thomasshelby@cluster0.essubfs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)


