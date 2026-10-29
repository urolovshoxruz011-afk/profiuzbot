[Чт 29.10.26 22:50] Urolov Şoxruz: print("ProfiUz bot loyihasi boshlandi!")
[Чт 29.10.26 22:53] Urolov Şoxruz: import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("9291064655:AAErPVvgwdlnPkjMEk9lgEU3keLM6pBAavo")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🔎 Mutaxassis topish"],
        ["📝 Mutaxassis bo‘lib qo‘shilish"],
        ["ℹ️ Biz haqimizda"]
    ]
    await update.message.reply_text(
        "👋 ProfiUz botiga xush kelibsiz!\n\n"
        "Bu yerda kerakli mutaxassisni topishingiz yoki xizmatingizni taklif qilishingiz mumkin.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ℹ️ Biz haqimizda":
        await update.message.reply_text(
            "ProfiUz — O‘zbekistondagi mutaxassislar va mijozlarni birlashtiruvchi platforma."
        )
    elif text == "🔎 Mutaxassis topish":
        await update.message.reply_text(
            "Kerakli yo‘nalishni yozing:\n\n"
            "• SMM\n• Grafik dizayn\n• AI xizmatlari\n• Video montaj"
        )
    elif text == "📝 Mutaxassis bo‘lib qo‘shilish":
        await update.message.reply_text(
            "Mutaxassis sifatida ro‘yxatdan o‘tish tez orada qo‘shiladi."
        )
    else:
        await update.message.reply_text(
            "Menyudagi tugmalardan birini tanlang yoki /start buyrug‘ini yuboring."
        )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))
    app.run_polling()

if name == "main":
    main()
