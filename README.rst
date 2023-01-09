westwallet-python-api
=====================
.. image:: https://img.shields.io/pypi/v/westwallet-api.svg?style=flat-square&maxAge=1800
    :alt: PyPI
    :target: https://pypi.python.org/pypi/westwallet-api

westwallet-python-api is a `WestWallet Public API <https://westwallet.io/api_docs>`_ wrapper for Python programming language. Use it for building payment solutions.

Installing
----------

Install from pypi:

.. code-block:: text

    pip install -U westwallet-api


Install from latest source code (*may be unstable*):

.. code-block:: text

    pip install git+git://github.com/WestWallet/westwallet-python-api


Create withdrawal example
-------------------------

.. code-block:: python

    # Send 0.1 ETH to 0x57689002367b407f031f1BB5Ef2923F103015A32
    from westwallet_api import WestWalletAPI
    from westwallet_api.exceptions import InsufficientFundsException, BadAddressException

    client = WestWalletAPI("your_api_key", "your_api_secret")
    try:
        sent_transaction = client.create_withdrawal(
            "ETH", "0.1", "0x57689002367b407f031f1BB5Ef2923F103015A32"
        )
    except InsufficientFundsException:
        # handle this case
        pass
    except BadAddressException:
        # handle also this case
        pass
    else:
        print(sent_transaction.__dict__)


Generate address example
-------------------------

.. code-block:: python

    from westwallet_api import WestWalletAPI

    client = WestWalletAPI("your_api_key", "your_api_secret")
    address = client.generate_address("XRP")
    print(address.address, address.dest_tag)


Documentation
-------------
* API: https://westwallet.io/api_docs


Other languages
---------------
* JavaScript: https://github.com/WestWallet/westwallet-js-api
* Golang: https://github.com/WestWallet/westwallet-golang-api
* PHP: https://github.com/WestWallet/westwallet-php-api
