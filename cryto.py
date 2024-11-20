import os
import requests
from telegram import Bot
import asyncio
import time
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Retrieve API keys from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# File to persist last alert time
cooldown_file = "last_alert_time.json"
alert_cooldown = 3600  # Cooldown period in seconds (1 hour)

# Load last alert time from file
def load_last_alert_time():
    try:
        with open(cooldown_file, "r") as file:
            data = json.load(file)
            return data.get("last_alert_time", 0)
    except FileNotFoundError:
        return 0  # Default to 0 if the file doesn't exist

# Save last alert time to file
def save_last_alert_time(last_alert_time):
    with open(cooldown_file, "w") as file:
        json.dump({"last_alert_time": last_alert_time}, file)

# Retrieve price of a specific crypto
def track_KID():
    last_alert_time = load_last_alert_time()
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
    if float(kid_price) < 0.00063:
        message_body = f"KID is below 0.00063, current price: {kid_price}"
        save_last_alert_time(current_time)  # Update last alert time
        asyncio.run(send_telegram_message(message_body))
    elif float(kid_price) > 0.0014:
        message_body = f"KID is above 0.0014, current price: {kid_price}"
        save_last_alert_time(current_time)  # Update last alert time
        asyncio.run(send_telegram_message(message_body))

# Send Telegram message
async def send_telegram_message(message):
    logging.info(f"Sending message to Telegram: {message}")
    bot = Bot(token=bot_token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        logging.info("Message sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")

# Run the script
track_KID()
