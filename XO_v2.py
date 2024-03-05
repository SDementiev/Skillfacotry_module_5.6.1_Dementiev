def print_map(map):  # вывод карты
    print("\n  0 1 2")
    for i in range(3):
        print(i, map[i][0], map[i][1], map[i][2])


def check_compl(map):  # Проверка заполнение поля
    for row in map:
        for element in row:
            if element == "-":
                return 1
                break
    return 0


def step_input(map, N):  # Заполнение по N
    while True:
        print_map(map)
        if N == "X":
            print("\nВведите координаты крестика.")
        else:
            print("\nВведите координаты нолика.")
        x, y = input("Первая координата # в строке, через пробел вторая - # в столбце:").split()
        if x.isdigit() and y.isdigit():  # проверка числа
            if test_ij(int(y), int(x)):  # проверка диапазона
                if (map[int(y)][int(x)] == "-"):  # проверка не занятой ячейки
                    break
        print("Неверный ввод! Повторите...")
    map[int(y)][int(x)] = N
    return map


def check_win(map, N):  # Проверка выигрыша по элементу N
    if map[0][0] == N and map[0][1] == N and map[0][2] == N:  # Построчная проверка
        return 1
    elif map[1][0] == N and map[1][1] == N and map[1][2] == N:  # Построчная проверка
        return 1
    elif map[2][0] == N and map[2][1] == N and map[2][2] == N:  # Построчная проверка
        return 1
    elif map[0][0] == N and map[1][0] == N and map[2][0] == N:  # Проверка по столбцам
        return 1
    elif map[0][1] == N and map[1][1] == N and map[2][1] == N:  # Проверка по столбцам
        return 1
    elif map[0][2] == N and map[1][2] == N and map[2][2] == N:  # Проверка по столбцам
        return 1
    elif map[0][0] == N and map[1][1] == N and map[2][2] == N:  # Проверка по диагонали
        return 1
    else:
        return 0


def test_ij(i, j):  # Проверка диапазона ввода
    return i >= 0 and i <= 2 and j >= 0 and j <= 2


print("    Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).")
print("Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает.")
print("Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали")
print("нет трёх одинаковых знаков, партия считается закончившейся в ничью. Первый ход делает игрок, ставящий крестики.")
print("Обычно по завершении партии выигравшая сторона зачёркивает чертой свои три знака (нолика или крестика),")
print("составляющих сплошной ряд или большую диагональ.\n")
while True:
    map = [["-", "-", "-"],  # Пустое поле
           ["-", "-", "-"],
           ["-", "-", "-"]]
    while True:
        step_input(map, "X")
        if not check_compl(map) or check_win(map, "X"):
            break
        step_input(map, "O")
        if not check_compl(map) or check_win(map, "O"):
            break
    print("\nИгра завершена")
    if check_win(map, "X"):
        print("Победили крестики!\nПримите поздравления!")
    elif check_win(map, "O"):
        print("Победили нолики!\nПримите поздравления!")
    else:
        print("Боевая ничья\nУРА!")
    print_map(map)
    print("\nЕще партейку?\nНажмите N и 'ввод' если наигрались...")
    if input() in ('n', 'N', 'Т', 'т'):
        break
