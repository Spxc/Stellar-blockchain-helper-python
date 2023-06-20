from stellar_sdk import Server, Keypair

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