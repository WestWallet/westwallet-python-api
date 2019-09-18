class WestWalletAPIException(Exception):
    pass


class InsufficientFundsException(WestWalletAPIException):
    pass


class CurrencyNotFoundException(WestWalletAPIException):
    pass


class NotAllowedException(WestWalletAPIException):
    """Raises when request type or headers don't match API key settings"""
    pass


class WrongCredentialsException(WestWalletAPIException):
    """Raises when you've provided wrong API key"""
    pass


class TransactionNotFoundException(WestWalletAPIException):
    pass


class AccountBlockedException(WestWalletAPIException):
    """Raises if your account unable to create withdrawal"""
    pass


class BadAddressException(WestWalletAPIException):
    """Raises when WestWallet server regex check
    of recipient's address fails"""
    pass


class BadDestTagException(WestWalletAPIException):
    """Raises when WestWallet server regex check
    of recipient's destination tag fails"""
    pass


class MinWithdrawException(WestWalletAPIException):
    pass


class MaxWithdrawException(WestWalletAPIException):
    pass


exceptions = {
    "account_blocked": AccountBlockedException,
    "bad_address": BadAddressException,
    "bad_dest_tag": BadDestTagException,
    "insufficient_funds": InsufficientFundsException,
    "max_withdraw_error": MaxWithdrawException,
    "min_withdraw_error": MinWithdrawException,
    "currency_not_found": CurrencyNotFoundException,
    "not_found": TransactionNotFoundException
}