# Homework 7, Task 4: Roles audit

# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Преобразуем список во множество для моментального удаления дубликатов
unique_requested_roles = set(requested_roles)

# Находим общие роли (пересечение множеств с помощью знака &)
common_roles = unique_requested_roles & required_admin_roles

# Находим недостающие роли (разность множеств с помощью знака -)
missing_roles = required_admin_roles - unique_requested_roles

# Проверяем наличие 'security_officer' через оператор membership 'in'
has_security_officer = "security_officer" in unique_requested_roles

# Вывод результатов
print(f"Уникальные запрошенные роли: {unique_requested_roles}")
print(f"Общие административные роли: {common_roles}")
print(f"Недостающие административные роли: {missing_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")