from binance.client import Client

def get_client():
    client = Client(
        api_key="test",
        api_secret="test"
    )
    
    # IMPORTANT: point to testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com"
    
    return client