from dataclasses import dataclass
from typing import Optional

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
    blockchain_hash: str
    fee: str
    label: Optional[str] = None
    type: Optional[str] = "send"
    blockchain_confirmations: Optional[int] = 0


@dataclass
class GenerateAddressResponse:
    address: str
    dest_tag: str
    currency: str
    label: str
