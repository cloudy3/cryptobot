# Crypto Price Alert Telegram Bot

This project allows you to receive price alerts for cryptocurrencies directly on your Telegram using a custom Telegram bot. The bot tracks the price of cryptocurrencies using the CoinGecko API and sends notifications to your Telegram when specific price conditions are met.

## Features

- Monitors cryptocurrency prices via the CoinGecko API.
- Sends price alerts to your Telegram account.
- Fully automated tracking using a GitHub Workflow (.yml) file.
- Easy setup for different cryptocurrencies and price thresholds.

## Prerequisites

- A Telegram account and bot token (create a bot via BotFather on Telegram).
- GitHub repository with access to workflows.

## Setup Instructions

##### 1. Get Your Telegram Bot Token

- Create a bot on Telegram by chatting with BotFather.
- Obtain the API token for your bot.

##### 2. Set Up Secrets in GitHub

- In your GitHub repository, navigate to Settings > Secrets.
- Add the following secrets:
  - `TELEGRAM_API_TOKEN` – Your bot's API token.
  - `CHAT_ID` – Your Telegram chat ID (where the bot will send messages).

##### 3. Configure the Workflow

Customize the `.github/workflows/price-alert.yml` file to specify the cryptocurrencies you want to track and their target price thresholds.

##### 4. Run the Workflow

The GitHub workflow will automatically run based on the schedule you configure in the .yml file.
The bot will check the current price of the specified cryptocurrency and send a message to your Telegram if the price meets the set conditions.
