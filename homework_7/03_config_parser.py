# Homework 7, Task 3: Config parser

# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Извлекаем вложенный словарь connection
connection = db_config.get("connection", {})

# Извлекаем значения host и port
host = connection.get("host")
port = connection.get("port")

# Безопасно проверяем параметр ssl_mode (если ключа нет, вернется дефолт 'verify-full')
ssl_settings = db_config.get("ssl_settings", {})
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

# Меняем пользователя на 'admin' во вложенном словаре
connection["user"] = "admin"

# Добавляем новый параметр max_connections со значением 100
connection["max_connections"] = 100

# Выводим итоговую информацию
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")

# Выводим все пары ключ-значение из connection через цикл и .items()
for key, value in connection.items():
    print(f"  * {key}: {value}")