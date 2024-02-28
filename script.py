map = [["-","-","-"], #Пустое поле
       ["-","-","-"],
       ["-","-","-"]]

def print_map(map): #вывод карты
    print("  0 1 2")
    for i in range(3):
       print(i, map[i][0], map[i][1], map[i][2])

def test_complet(map):#Проверка заполнение поля
    for row in map:
        for element in row:
            if element=="-":
                return 1
                break
    return 0

def test_ij(i,j):#Проверка диапазона ввода
    return int(i) >= 0 and int(i) <= 2 and int(j) >= 0 and int(j) <= 2
while True:
    while True:
        print_map(map)
        x,y = input("Введите координаты Х:").split()
        if test_ij(int(y), int(x)):
            if (map[int(y)][int(x)] == "-"): break
        print("Неверный ввод! повторите...")
    map[int(y)][int(x)] = "X"
    if not test_complet(map): break
    while True:
        print_map(map)
        x, y = input("Введите координаты O:").split()
        if test_ij(int(y), int(x)):
            if (map[int(y)][int(x)] == "-"): break
        print("Неверный ввод! повторите...")
    map[int(y)][int(x)] = "O"
    if not test_complet(map): break
print("Игра завершена")
print_map(map)