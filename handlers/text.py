import os
import requests
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

from hadith_related.extract_hadiths import extract_hadiths
from .other.funcs import send_hadith

load_dotenv()
USERNAME = os.getenv("BOT_USERNAME")
# USERNAME = "takhrij_bot"

def make_api_request(api):
    response = requests.get(api)
    html_content = response.json()["ahadith"]["result"]
    return html_content

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    skey = None
    message = None
    
    if update.message.chat.type == "private":
        skey = text
    else:
        if text.startswith(f"@{USERNAME}"):
            if len(text) == len(USERNAME) + 1:
                await update("يُرجى إدخال كلمات الحديث الذي تريدون البحث عنه")
            else:
                skey = text[len(USERNAME) + 1:]
    
    if skey:        
        api = f"https://dorar.net/dorar_api.json?skey={skey}"
        html_content = make_api_request(api)        
        hadiths = extract_hadiths(html_content)
        
        for hadith in hadiths[:-1]:
            await send_hadith(hadith, update, context)

        # the last item in the hadiths list is the dorar link
        await update.message.reply_text(hadiths[-1])



    


    
