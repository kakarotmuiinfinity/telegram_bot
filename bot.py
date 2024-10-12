import asyncio
from telegram.ext import Application, CommandHandler

# Add your bot token here
TOKEN = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"

# Your other imports and bot code...

async def start(update, context):
    await update.message.reply_text("Hello! The bot is working!")

async def main():
    # Your bot initialization and setup code here
    application = Application.builder().token(TTOKEN).build()

    # Add your command handlers here
    application.add_handler(CommandHandler("start", start))

    # Start the bot's polling
    await application.run_polling()

if __name__ == "__main__":
    try:
        # Check if an event loop is already running
        loop = asyncio.get_running_loop()
    except RuntimeError:  # No event loop is running
        loop = None

    if loop and loop.is_running():
        # If the loop is running, use create_task to run the main function
        print("Event loop is already running. Using create_task to run the bot.")
        asyncio.ensure_future(main())
    else:
        # Otherwise, run it normally
        asyncio.run(main())
        
