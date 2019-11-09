from westwallet_api import WestWalletAPI
from configparser import ConfigParser
from pprint import pprint

config = ConfigParser()
config.read('./examples/config.ini')

def main():
    client = WestWalletAPI(config['secrets']['api_key'], config['secrets']['secret_key'], base_url=config['secrets']['base_url'])
    balance = client.wallet_balance("BTC")
    pprint(balance.__dict__)
    balances = client.wallet_balances()
    pprint(balances.__dict__)

if __name__ == '__main__':
    main()