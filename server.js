const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const winston = require('winston');
const app = express();

// Конфигурация логирования
const logger = winston.createLogger({
    level: 'info',
    transports: [
        new winston.transports.Console({
            format: winston.format.simple(),
        }),
        new winston.transports.File({ filename: 'server.log' }),
    ],
});

// Защита сервера с помощью helmet
app.use(helmet());

// Ограничение запросов
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 минут
    max: 100, // Максимум 100 запросов
    message: "Слишком много запросов с вашего IP, попробуйте позже.",
});

// Применяем ограничение ко всем запросам
app.use(limiter);

// Пример маршрута
app.get('/', (req, res) => {
    logger.info('Запрос на главную страницу');
    res.send('Защищённый сервер работает!');
});

// Пример маршрута, который может вызвать ошибку
app.get('/error', (req, res) => {
    logger.error('Ошибка при обработке запроса');
    res.status(500).send('Произошла ошибка на сервере!');
});

// Пример маршрута, который заблокирует слишком много запросов
app.get('/rate-limited', (req, res) => {
    logger.warn('Слишком много запросов, возможно это бот!');
    res.send('Превышен лимит запросов');
});

// Запуск сервера
const PORT = 3000;
app.listen(PORT, () => {
    logger.info(`Сервер запущен на порту ${PORT}`);
});
