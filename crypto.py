import os
import requests
from telegram import Bot
import asyncio
import time

# Retrieve API keys from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# In-memory cooldown mechanism
last_alert_time = 0  # Initialize the last alert time in seconds
alert_cooldown = 3600  # Cooldown period in seconds (1 hour)

# Retrieve price of a specific crypto
def track_KID():
    global last_alert_time
    current_time = time.time()  # Get current time in seconds

    # Check cooldown
    if current_time - last_alert_time < alert_cooldown:
        print("Cooldown active, skipping alert.")
        return

    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"
    )
    kid_price = response.json()["data"]["attributes"]["token_prices"]["EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"]
    kid_price = kid_price[:8]

    # Determine the alert condition
    if float(kid_price) < 0.000415:
        message_body = f"KID is below 0.000415, current price: {kid_price}"
        last_alert_time = current_time  # Update last alert time
        asyncio.run(send_telegram_message(message_body))
    elif float(kid_price) > 0.0007:
        message_body = f"KID is above 0.0007, current price: {kid_price}"
        last_alert_time = current_time  # Update last alert time
        asyncio.run(send_telegram_message(message_body))

# Send Telegram message
async def send_telegram_message(message):
    print(f"Sending message: {message}")
    bot = Bot(token=bot_token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Run the script
track_KID()
