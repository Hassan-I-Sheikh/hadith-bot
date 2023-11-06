from telegram import Update
from telegram.ext import ContextTypes


start_text = """
أهلا بكم. 

قم بإرسال أي جملة تذكرها من الحديث وسيقوم البوت بإرسال لك الأحاديث المحتوية على لجملة التي أرسلتها.

يرجى تجنب الأخطاء الإملائية للحصول على نتائج دقيقة.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(start_text)