import requests


# Retrieve price of a specific crypto
def track_KID():
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/simple/networks/solana/token_price/EB8uJb7PfZhEGgLxzTURemxoXMHAEvAnbNi48JQhpump"
    )
    print(response.status_code)
    print(response.json())

track_KID()