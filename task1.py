import time
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Реалізіація детермінованого QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибираємо середній елемент як опорний
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Реалізація рандомізованого QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Вибираємо випадковиий елемент як опорний
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Функція для замірювання часу сортування
def measure_time(sort_function, arr, num_runs=5):
    times = []
    for _ in range(num_runs):
        arr_copy = arr.copy()  # Впевнюємося, що масив не змінюється
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)


# Визначення розмірів масивів
array_sizes = [10_000, 50_000, 100_000, 500_000]

# Визначення списку для збереження результатів
results = []

# Запускаємо сортування для кожного розміру масиву
for size in array_sizes:
    array = np.random.randint(0, 10**6, size).tolist()
    rand_qs_time = measure_time(randomized_quick_sort, array)
    det_qs_time = measure_time(deterministic_quick_sort, array)

    results.append([size, rand_qs_time, det_qs_time])
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_qs_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_qs_time:.4f} секунд")

# Конвертуємо результати у DataFrame
df_results = pd.DataFrame(results, columns=["Розмір масиву", "Рандомізований QuickSort (сек)", "Детермінований QuickSort (сек)"])

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.plot(df_results["Розмір масиву"], df_results["Рандомізований QuickSort (сек)"], marker='o', linestyle='-', label='Рандомізований QuickSort')
plt.plot(df_results["Розмір масиву"], df_results["Детермінований QuickSort (сек)"], marker='s', linestyle='-', label='Детермінований QuickSort')

# Налаштування візуалізації
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (сек)")
plt.title("Порівняння часу виконання QuickSort")
plt.legend()
plt.grid(True)

# Відображення графіку
plt.show()