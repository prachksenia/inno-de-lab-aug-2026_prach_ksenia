# Homework 7, Task 5: Metrics  aggregator

# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

# Создаем списки для сбора данных только по активным серверам
active_nodes = []
cpu_loads = []
ram_usages = []

# Распаковываем кортежи прямо в цикле for и фильтруем offline-серверы
for node_name, cpu_load, ram_usage, status in system_telemetry:
    # Очищаем статус от лишних пробелов и проверяем, что сервер online
    if status.strip() == "online":
        # 3. Наполняем списки данными
        active_nodes.append(node_name)
        cpu_loads.append(cpu_load)
        ram_usages.append(ram_usage)

# Рассчитываем итоговые показатели с помощью встроенных функций
active_count = len(active_nodes)
avg_cpu = round(sum(cpu_loads) / active_count, 2)
max_ram = max(ram_usages)

# Собираем метрики в итоговый вложенный словарь
telemetry_report = {
    "active_nodes_count": active_count,
    "metrics": {
        "average_cpu": avg_cpu,
        "max_ram": max_ram
    }
}

# Вывод результатов
print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
print(telemetry_report)