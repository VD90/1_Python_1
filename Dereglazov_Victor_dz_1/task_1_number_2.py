my_list = []
list_of_cubes = []
add_list_of_cubes = []

my_list = list(range(1001))
my_list = my_list[1::2]
print(my_list)

for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)
print(list_of_cubes)

# можно ли использлвать my_lst (cо списком нечётных чисел), чтобы не вводить фунцию range?

# (берем число, убираем последнюю цифру, складываем в переменную, которая всё эжто суммирует,
# уменьшаем число на эту цифру) - цикл, пока цифра не сотрётся
# но, либо эннумирэйт, либо класть в переменную

for i, val in enumerate(list_of_cubes):
    summa = 0
    for i, val in enumerate(list_of_cubes):
        s = 0
        figure = val
        while val > 0:
            s = s + val % 10
            val = val // 10
        if s % 7 == 0:
            summa += figure
print(summa)
print(list_of_cubes)

for idx in range(len(list_of_cubes)):
    list_of_cubes[idx] += 17
print(list_of_cubes)

for i, val in enumerate(list_of_cubes):
    summa = 0
    for i, val in enumerate(list_of_cubes):
        s = 0
        figure = val
        while val > 0:
            s = s + val % 10
            val = val // 10
        if s % 7 == 0:
            summa += figure
print(summa)
