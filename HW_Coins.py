import time

# Жадібний алгоритм
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 потрібно 0 монет

    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Функція для вимірювання часу виконання
def measure_time(func, amount):
    start = time.time()  # Початковий час
    result = func(amount)  # Виконання функції
    end = time.time()  # Кінцевий час
    elapsed = end - start  # Обчислення часу виконання
    return result, elapsed

# Тестування
if __name__ == "__main__":
    amount = 113

    # Жадібний алгоритм
    greedy_result, greedy_time = measure_time(find_coins_greedy, amount)
    print("Жадібний алгоритм:")
    print(greedy_result)
    print(f"Час виконання: {greedy_time:.6f} секунд")

    # Динамічне програмування
    dp_result, dp_time = measure_time(find_min_coins, amount)
    print("\nДинамічне програмування:")
    print(dp_result)
    print(f"Час виконання: {dp_time:.6f} секунд")
