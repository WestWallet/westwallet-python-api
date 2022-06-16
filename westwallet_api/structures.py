from dataclasses import dataclass

@dataclass
class Balance:
    balance: str
    currency: str


@dataclass
class Transaction:
    id: int
    amount: str
    address: str
    dest_tag: str
    currency: str
    status: str
    type: str
    blockchain_confirmations: int
    blockchain_hash: str
    fee: str


@dataclass
class GenerateAddressResponse:
    address: str
    dest_tag: str
    currency: str
    label: str
