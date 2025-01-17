# Порівняння алгоритмів сортування

У цьому завданні ми порівняли три різних алгоритми сортування за часом виконання:
Merge Sort, Insertion Sort та Timsort (вбудований алгоритм Python).

## Результати

| Розмір даних | Алгоритм | Час (секунди) |
|--------------|----------|---------------|
| 100 | Mergesort | 0.000114 |
| 100 | Insertionsort | 0.000147 |
| 100 | Timsort | 0.000007 |
| 1000 | Mergesort | 0.001625 |
| 1000 | Insertionsort | 0.016939 |
| 1000 | Timsort | 0.000072 |
| 5000 | Mergesort | 0.008896 |
| 5000 | Insertionsort | 0.436317 |
| 5000 | Timsort | 0.000448 |

## Висновки
Алгоритм Timsort виявився найефективнішим на всіх наборах даних, що доводить його перевагу
у поєднанні сортування злиттям та сортування вставками.
