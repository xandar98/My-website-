from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ✅ Your bot token (keep it private!)
TOKEN = "8122828014:AAGnor60SB0MlMm29XeANguLLRuiF3PI__A"

# ✅ Replace with your actual GitHub Pages link
GITHUB_CALC_URL = "https://yourusername.github.io/calculator-mini-app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧮 Mini Calculator:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Open Calculator", web_app=WebAppInfo(url=GITHUB_CALC_URL))
        ]])
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
