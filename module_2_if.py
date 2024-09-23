
first = input('Введите 1 число: ')
second = input('Введите 2 число: ')
third = input('Введите 3 число: ')

if first == second and first == third:
    print(3)
elif not first == second and not first == third and not second == third:
    print(0)
else:
    print(2)
