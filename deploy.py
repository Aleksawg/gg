from web3 import Web3
import solcx

# Компилируем Solidity
solcx.install_solc('0.8.0')  # Устанавливаем нужную версию компилятора
compiled_sol = solcx.compile_files(["security_logs.sol"])
contract_interface = compiled_sol["security_logs.sol:SecurityLogs"]

# Подключаемся к локальному блокчейну (Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]  # Используем первый аккаунт в Ganache

# Деплой контракта
SecurityLogs = w3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
tx_hash = SecurityLogs.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Адрес контракта
contract_address = tx_receipt.contractAddress
print(f"Контракт развернут по адресу: {contract_address}")
