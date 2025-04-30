from web3 import Web3

class BlockchainLogger:
    def __init__(self, rpc_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def log_event(self, event_data):
        # Записываем событие в блокчейн
        tx = self.contract.functions.logSecurityEvent(event_data).buildTransaction({
            'from': self.w3.eth.accounts[0],
            'gas': 2000000,
            'gasPrice': self.w3.toWei('20', 'gwei')
        })
        self.w3.eth.sendTransaction(tx)
