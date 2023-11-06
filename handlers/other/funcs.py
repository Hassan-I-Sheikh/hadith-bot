from telegram import Update
from telegram.ext import ContextTypes

async def send_hadith(hadith: dict, update: Update, context: ContextTypes):
    message = []

    for key in hadith.keys():
        message.append(f"{key}: {hadith[key]}\n")
    
    # adding a new line for looks
    message[1] = f"\n{message[1]}"
    message = "".join(message)

    try:
        await update.message.reply_text(message)
    except:
        # send half the message at a time
        mid = len(message) // 2
        await update.message.reply_text(message[: mid])
        await update.message.reply_text(message[mid :])