
import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 RM MINES ANALYZER 2026\n\n"
        "Добро пожаловать!\n\n"
        "Доступные команды:\n"
        "/analyze — анализ вероятностей\n"
        "/help — помощь\n\n"
        "⚠️ Анализ не гарантирует выигрыш."
    )


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 RM MINES ANALYZER\n\n"
        "Для расчёта вероятности укажи:\n"
        "Количество клеток мин:\n"
        "Количество клеток для выбора:\n\n"
        "Важно: без проверяемых данных игры "
        "невозможно определить безопасные клетки."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команды бота:\n"
        "/start — запуск\n"
        "/analyze — анализ вероятностей\n"
        "/help — помощь"
    )


def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()


if __name__ == "__main__":
    main()
