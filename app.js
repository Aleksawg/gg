const Web3 = require('web3');
const fs = require('fs');
const path = require('path');

// Подключаемся к локальному Ganache
const web3 = new Web3('http://localhost:8545');

// Адрес контракта и ABI
const contractAddress = '0x9cf6Db774f574BA73968baBB3D08838150456fBD'; // Убедитесь, что это правильный адрес
const abi = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'build/contracts/SimpleStorage.json'), 'utf8')).abi;

// Создаем экземпляр контракта
const simpleStorage = new web3.eth.Contract(abi, contractAddress);

async function fetchValue() {
    try {
        const value = await simpleStorage.methods.retrieve().call();
        console.log("Значение из контракта:", value);
    } catch (error) {
        console.error("Ошибка при вызове retrieve:", error);
    }
}

async function storeValue(value) {
    const accounts = await web3.eth.getAccounts();
    try {
        const receipt = await simpleStorage.methods.store(value).send({ from: accounts[0] });
        console.log("Транзакция выполнена:", receipt);

        // После записи нового значения, проверим, что оно сохранено
        fetchValue(); // Вызовем fetchValue, чтобы проверить результат
    } catch (error) {
        console.error("Ошибка при вызове store:", error);
    }
}

// Пример использования
fetchValue(); // Получаем значение перед записью
storeValue(42); // Пример записи значения (замените на нужное вам значение)
