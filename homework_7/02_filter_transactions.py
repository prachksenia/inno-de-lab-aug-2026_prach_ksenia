# Homework 7, Task 2: Filter transactions

# Список транзакций, полученных от платежного шлюза
raw_transactions = ["SUCCESS: 100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# Разбивает строку на статус и сумму, очищает от пробелов, int(), условия отбирают только "SUCCESS" и суммы больше 0
cleaned_transactions = [
    int(amount.strip())
    for transaction in raw_transactions
    for status, amount in [transaction.split(":")]
    if status.strip() == "SUCCESS" and int(amount.strip()) > 0
]

# Вывод результата на экран
print(f"Очищенные транзакции: {cleaned_transactions}")