from westwallet_api import WestWalletAPI
from configparser import ConfigParser
from pprint import pprint

config = ConfigParser()
config.read('./examples/config.ini')

def main():
    base_url = config['secrets']['base_url']
    client = WestWalletAPI(config['secrets']['api_key'],
                           config['secrets']['secret_key'],
                           base_url=base_url)
    sent_transaction = client.create_withdrawal(
        "BCH", str(0.001), "1NWQxuJm8eNsSrv1KyhYgoAGdGKd7eYQVW"
    )
    pprint(sent_transaction.__dict__)

if __name__ == '__main__':
    main()