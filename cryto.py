import os
import requests
from telegram import Bot
import asyncio


# Retrieve API keys from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Retrieve price of a specific crypto
def track_KID():
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"
    )
    # print(response.status_code)
    kid_price = response.json()["data"]["attributes"]["token_prices"]["EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"]
    kid_price = kid_price[:8]
    # print(kid_price)

    if float(kid_price) < 0.00055:
        message_body = f"KID is below 0.00055, current price: {kid_price}"
    if float(kid_price) > 0.00055:
        message_body = f"KID is above 0.00085, current price: {kid_price}"

    asyncio.run(send_telegram_message(message_body))

async def send_telegram_message(message):
    bot = Bot(token= bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

# Call the function once when the GitHub Actions job is triggered
track_KID()
