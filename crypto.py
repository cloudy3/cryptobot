import os
import requests
from telegram import Bot
import asyncio

# Retrieve API keys from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Retrieve price of a specific crypto
def track_crypto():
    # Track $KID price
    # response = requests.get(
    #     "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"
    # )
    # kid_price = response.json()["data"]["attributes"]["token_prices"]["EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"]
    # kid_price = kid_price[:8]

    # Determine the alert condition
    # if float(kid_price) < 0.000415:
    #     message_body = f"KID is below 0.000415, current price: {kid_price}"
    #     last_alert_time = current_time  # Update last alert time
    #     asyncio.run(send_telegram_message(message_body))
    # if float(kid_price) > 0.00036:
    #     message_body = f"KID is above 0.00036, current price: {kid_price}"
    #     asyncio.run(send_telegram_message(message_body))

    # Track $PONKE price
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC"
    )
    ponke_price = response.json()["data"]["attributes"]["token_prices"]["5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC"]
    ponke_price = ponke_price[:5]

    # if float(ponke_price) < 0.42:
    #     message_body = f"PONKE is less than 0.42, current price: {ponke_price}"
    #     asyncio.run(send_telegram_message(message_body))

    if float(ponke_price) > 0.53:
        message_body = f"PONKE is above 0.53, current price: {ponke_price}"
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
track_crypto()
