import random
import itertools

# Создание случайного списка из 20 значений по 4 случайных целых числа от -10 до 10
values = [random.randint(-10, 10) for _ in range(20)]
print("Список значений:", values)

# Нахождение всех уникальных комбинаций
pairs = list(itertools.combinations(values, 2))
print("\nВсе уникальные пары:")
print(pairs)

# Запрос целого числа
value = int(input("\nВведите целое число: "))

# Вычисление количества пар, чья сумма меньше заданного значения
count = 0
for pair in pairs:
    if sum(pair) < value:
        count += 1
        
print(f"\nКоличество пар, чья сумма меньше {value}: {count}")
