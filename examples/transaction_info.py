from westwallet_api import WestWalletAPI
from configparser import ConfigParser
from pprint import pprint

config = ConfigParser()
config.read('./examples/config.ini')

def main():
    client = WestWalletAPI(config['secrets']['api_key'])
    transaction = client.transaction_info(19)
    pprint(transaction.__dict__)

if __name__ == '__main__':
    main()