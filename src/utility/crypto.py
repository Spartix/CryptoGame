import requests
def get_ltc_data():
    response_ltc = requests.get('https://api.coingecko.com/api/v3/coins/litecoin/market_chart?vs_currency=usd&days=1')
    data_ltc = response_ltc.json()
    print(data_ltc)
def get_crypto_data():
    get_ltc_data()
    response_btc = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1')
    response_ltc = requests.get('https://api.coingecko.com/api/v3/coins/litecoin/market_chart?vs_currency=usd&days=1')
    response_sol = requests.get('https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=usd&days=1')

    data_btc = response_btc.json()
    data_ltc = response_ltc.json()
    data_sol = response_sol.json()

    prices_btc = [entry[1] for entry in data_btc['prices']]
    prices_ltc = [entry[1] for entry in data_ltc['prices']]
    prices_sol = [entry[1] for entry in data_sol['prices']]

    timestamps = [entry[0] for entry in data_btc['prices']]

    return timestamps, prices_btc, prices_ltc, prices_sol