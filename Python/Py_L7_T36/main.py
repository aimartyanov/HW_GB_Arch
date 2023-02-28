'''
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов
таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
(подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.
Ввод:

print_operation_table(lambda x, y: x * y)

Вывод:
1 2 3 4 5 6
'''
def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)
        print('\t'.join([str(x) for x in nums]))
print_operation_table(lambda x, y: x * y)
