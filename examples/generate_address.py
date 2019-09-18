from westwallet_api import WestWalletAPI
from configparser import ConfigParser

config = ConfigParser()
config.read('./examples/config.ini')

def main():
    client = WestWalletAPI(config['secrets']['api_key'], config['secrets']['secret_key'])
    generated_address = client.generate_address("BTC")
    print(generated_address.address)

if __name__ == '__main__':
    main()