from binance.client import Client
import time

class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key="LONEwcz896gXvQv3p0NOckJYkFwl86S9rPIeNaGTdTYCmhlY2WAy1qLsmwdoELnE",
            api_secret="vPpm0EUvjvjtojd7g5E9unCzc74Z2eGOGRBhOX0UwTh3vUUUJCy8e044mL0YVNpf",
            testnet=True
        )

        # Set correct testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        
        server_time = self.client.futures_time()['serverTime']
        local_time = int(time.time() * 1000)
        self.client.timestamp_offset = server_time - local_time

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)