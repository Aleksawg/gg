from web3 import Web3

ganache_url = "http://127.0.0.1:7545"  # Адрес локального блокчейна
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("✅ Успешное подключение к Ganache!")
    print(f"Баланс 1-го аккаунта: {web3.eth.get_balance(web3.eth.accounts[0]) / 10**18} ETH")
else:
    print("❌ Ошибка подключения к Ganache")
