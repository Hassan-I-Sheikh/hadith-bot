import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from typing import final 
from commands.start import start
from handlers.text import handle_text

load_dotenv()
TOKEN = os.getenv("TOKEN")

if __name__ == "__main__":
    print("Starting bot")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT, handle_text))

    app.run_polling()
