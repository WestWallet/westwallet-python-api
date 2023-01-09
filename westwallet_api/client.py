import requests
from .structures import Balance, Transaction, GenerateAddressResponse
from .exceptions import *
import json
import hashlib
import hmac
import time

class WestWalletAPI:
    def __init__(self, api_key: str, secret_key: str, base_url: str = "https://api.westwallet.io"):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def _make_headers(self, data):
        timestamp = int(time.time())
        if data:
            dumped = json.dumps(data, ensure_ascii=False)
        else:
            dumped = ""
        sign = hmac.new(self.secret_key.encode('utf-8'),
                        "{}{}".format(timestamp, dumped)
                        .encode('utf-8'), hashlib.sha256).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
            "X-ACCESS-SIGN": sign,
            "X-ACCESS-TIMESTAMP": str(timestamp)
        }
        return headers

    def _make_get_request(self, method_url: str, params: dict = None):
        response = requests.get("{}{}".format(self.base_url, method_url),
                                params=params,
                                headers=self._make_headers(params))
        self._check_errors(response)
        return response

    def _make_post_request(self, method_url: str, data: dict):
        response = requests.post("{}{}".format(self.base_url, method_url),
                                 data=json.dumps(data, ensure_ascii=False),
                                 headers=self._make_headers(data))
        self._check_errors(response)
        return response

    def wallet_balance(self, currency: str) -> Balance:
        params = {
            "currency": currency
        }
        method_url = "/wallet/balance"

        response = self._make_get_request(method_url, params)

        response_json = response.json()
        response_json.pop('error')

        return Balance(**response_json)

    def wallet_balances(self):
        method_url = "/wallet/balances"
        response = self._make_get_request(method_url)

        response_json = response.json()
        response_json.pop('error')

        return response_json

    def create_withdrawal(self, currency: str, amount: str,
                          address: str, dest_tag: str = "",
                          description: str = "", priority: str = "medium") -> Transaction:
        data = {
            "currency": currency,
            "amount": amount,
            "address": address,
            "dest_tag": dest_tag,
            "description": description,
            "priority": priority
        }

        method_url = "/wallet/create_withdrawal"
        response = self._make_post_request(method_url, data)

        response_json = response.json()
        response_json.pop('error')

        transaction = Transaction(
            **response_json
        )
        return transaction

    def transaction_info(self, id: int) -> Transaction:
        data = {
            "id": id
        }

        method_url = "/wallet/transaction"
        response = self._make_post_request(method_url, data)

        response_json = response.json()
        response_json.pop('error')

        transaction = Transaction(
            **response_json
        )
        return transaction

    def generate_address(self, currency: str, ipn_url: str = "", label: str = "") -> GenerateAddressResponse:
        data = {
            "currency": currency,
            "ipn_url": ipn_url,
            "label": label
        }

        method_url = "/address/generate"
        response = self._make_post_request(method_url, data)

        response_json = response.json()
        response_json.pop('error')

        generate_address_response = GenerateAddressResponse(
            **response_json
        )
        return generate_address_response

    def _check_errors(self, response):
        if response.status_code == 401:
            raise WrongCredentialsException
        if response.status_code == 403:
            raise NotAllowedException
        response_json = response.json()
        error = response_json.get('error')
        if response_json.get('message'):
            raise NotAllowedException
        if error != 'ok':
            exception = exceptions.get(error)
            if exception:
                raise exception
            raise WestWalletAPIException(error)
