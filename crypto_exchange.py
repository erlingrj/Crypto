import requests


def get_custom_average(coin = 'ETH', market = 'Bitfinex'):
    url = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym=USD&e={}'.format(coin,market)
    return requests.get(url).json()

def get_change_24h(coin = 'ETH', market = 'Bitfinex'):
    url = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym=USD&e={}'.format(coin,market)

    r = requests.get(url).json()
    return float(r['RAW']['CHANGEPCT24HOUR'])


if __name__ == '__main__':
    print(get_custom_average('BTC','Coinbase'))

    print(get_change_24h())
