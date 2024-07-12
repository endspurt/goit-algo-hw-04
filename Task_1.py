import timeit
import random

# Реалізація сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для перевірки роботи та вимірювання часу алгоритмів сортування
def compare_sorts():
    # Генерація випадкового списку
    data_sizes = [100, 1000, 5000]
    algorithms = {
        'Mergesort': merge_sort,
        'Insertionsort': insertion_sort,
        'Timsort': sorted
    }

    results = []

    for size in data_sizes:
        print(f"Розмір даних: {size}")
        data = [random.randint(0, 10000) for _ in range(size)]
        
        for name, func in algorithms.items():
            # Копіювання даних, щоб сортування не змінювало вихідний список
            data_copy = data.copy()
            # Вимірювання часу виконання
            time = timeit.timeit(lambda: func(data_copy), number=1)
            results.append((size, name, time))
            print(f"{name}: {time:.6f} секунд")
    
    return results

if __name__ == "__main__":
    results = compare_sorts()

    with open("results.txt", "w", encoding="utf-8") as f:
        for size, name, time in results:
            f.write(f"Розмір даних: {size}, Алгоритм: {name}, Час: {time:.6f} секунд\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Порівняння алгоритмів сортування\n\n")
        f.write("У цьому завданні ми порівняли три різних алгоритми сортування за часом виконання:\n")
        f.write("Merge Sort, Insertion Sort та Timsort (вбудований алгоритм Python).\n\n")
        f.write("## Результати\n\n")
        f.write("| Розмір даних | Алгоритм | Час (секунди) |\n")
        f.write("|--------------|----------|---------------|\n")
        for size, name, time in results:
            f.write(f"| {size} | {name} | {time:.6f} |\n")
        f.write("\n## Висновки\n")
        f.write("Алгоритм Timsort виявився найефективнішим на всіх наборах даних, що доводить його перевагу\n")
        f.write("у поєднанні сортування злиттям та сортування вставками.\n")

