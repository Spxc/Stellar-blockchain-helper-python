# Stellar Python Library

This is a Python library that provides functions for interacting with the Stellar network using the Stellar SDK for Python.

<br>


## Installation

To use this library, you need to have Python 3 installed. You can install the library using pip:

```bash
pip install stellar-sdk
```

<br>


## Usage

### Load Account Pools

```python
from stellar_sdk import Server

server = Server("https://horizon.stellar.org")

def load_account_pools(account):
    try:
        account_info = server.load_account(account)
        liquidity_pools = [
            balance for balance in account_info["balances"]
            if balance.get("liquidity_pool_id")
        ]
        return liquidity_pools
    except Exception as e:
        print(e)
        return False
```

<br>

### Load pool details
```python
from stellar_sdk import Server

server = Server("https://horizon.stellar.org")

def load_pool_details(balance):
    try:
        pool_id = balance["liquidity_pool_id"]
        pool_info = server.liquidity_pools().liquidity_pool_id(pool_id).call()

        token_a = pool_info["reserves"][0]["asset"].split(":")
        token_b = pool_info["reserves"][1]["asset"].split(":")
        
        pool = {
            "shares": balance["balance"],
            "total_shares": pool_info["total_shares"],
            "tta": pool_info["reserves"][0]["amount"],
            "ttb": pool_info["reserves"][1]["amount"],
            "ta": {
                "code": token_a[0],
                "issuer": token_a[1]
            },
            "tb": {
                "code": token_b[0],
                "issuer": token_b[1]
            },
            "taa": (balance["balance"] / pool_info["total_shares"]) * (pool_info["reserves"][0]["amount"] / 100),
            "tba": (balance["balance"] / pool_info["total_shares"]) * (pool_info["reserves"][1]["amount"] / 100)
        }
        return pool
    except Exception as e:
        print(e)
        return False

```

<br>

## License
This library is licensed under the [MIT](#) License.
