import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token
TOKEN = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"  # Replace with your actual bot token or use an environment variable

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_full_name = update.message.from_user.full_name
    bot_name = context.bot.first_name

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🔥")
    await asyncio.sleep(2)

    sticker_id = "CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA"
    sent_sticker = await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker_id)
    await asyncio.sleep(2)

    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=sent_sticker.message_id)
    await asyncio.sleep(2)

    progress_message = await context.bot.send_message(chat_id=update.effective_chat.id, text="▣☐☐")
    await asyncio.sleep(2)
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=progress_message.message_id, text="☐▣☐")
    await asyncio.sleep(2)
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=progress_message.message_id, text="☐☐▣")

    await asyncio.sleep(2)
    photo_url = "https://te.legra.ph/file/d05ac856c4a8659de29ce.jpg"
    caption = f"Hᴇʟʟᴏ {user_full_name}✨\nMʏsᴇʟғ {bot_name} Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ?\nI ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!"

    keyboard = [
        [InlineKeyboardButton("✇ Aɴɪᴍᴇ Gʀᴏᴜᴘ ✇", url="https://t.me/Cartoon_Heaven")],
        [InlineKeyboardButton("❁ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ ❁", url="https://t.me/Cartoon_Carnival")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup)

# Main function to run the bot
async def main():
    application = ApplicationBuilder().token(TOKEN).build()  # Use ApplicationBuilder

    # Add start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.run_polling()  # Correct way to start the bot

if __name__ == '__main__':
    asyncio.run(main())
    
