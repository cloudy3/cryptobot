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
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"
    )
    kid_price = response.json()["data"]["attributes"]["token_prices"]["EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"]
    kid_price = kid_price[:8]

    # Determine the alert condition
    # if float(kid_price) < 0.000415:
    #     message_body = f"KID is below 0.000415, current price: {kid_price}"
    #     last_alert_time = current_time  # Update last alert time
    #     asyncio.run(send_telegram_message(message_body))
    if float(kid_price) > 0.0007:
        message_body = f"KID is above 0.0007, current price: {kid_price}"
        asyncio.run(send_telegram_message(message_body))

    # Track $Ruri price
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/DDij7Dp8updt3XSCzeHCaAoDoFTSE5Y27i2EQ9qjMQtr"
    )
    ruri_price = response.json()["data"]["attributes"]["token_prices"]["DDij7Dp8updt3XSCzeHCaAoDoFTSE5Y27i2EQ9qjMQtr"]
    ruri_price = ruri_price[:8]

    if float(ruri_price) < 0.005:
        message_body = f"Ruri is below 0.005, current price: {ruri_price}"
        asyncio.run(send_telegram_message(message_body))

    if float(ruri_price) > 0.012:
        message_body = f"Ruri is above 0.012, current price: {ruri_price}"
        asyncio.run(send_telegram_message(message_body))

    # Track $PONKE price
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC"
    )
    ponke_price = response.json()["data"]["attributes"]["token_prices"]["5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC"]
    ponke_price = ponke_price[:6]

    if float(ponke_price) < 0.51:
        message_body = f"PONKE is less than 0.51, current price: {ponke_price}"
        asyncio.run(send_telegram_message(message_body))

    if float(ponke_price) > 0.7:
        message_body = f"PONKE is above 0.7, current price: {ponke_price}"
        asyncio.run(send_telegram_message(message_body))

    # Track $BARSIK price
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/7ZqzGzTNg5tjK1CHTBdGFHyKjBtXdfvAobuGgdt4pump"
    )
    barsik_price = response.json()["data"]["attributes"]["token_prices"]["7ZqzGzTNg5tjK1CHTBdGFHyKjBtXdfvAobuGgdt4pump"]
    barsik_price = barsik_price[:6]

    if float(barsik_price) > 0.042:
        message_body = f"BARSIK is above 0.042, current price: {barsik_price}"
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
