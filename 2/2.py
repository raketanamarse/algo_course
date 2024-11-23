



# Исходные данные
n = 2  # количество признаков
a = [1, 100]  # вектор весов
mas = [
    [1, 2],
    [2, 1],
    [3, 1],
    [4, 1],
    [5, 1],
    [6, 1],
    [7, 1],
    [8, 1],
    [9, 1],
    [10, 1]
]

list_rel = []  # пустой список (используется по назначению?)

def count():
    # print(mas[0][0])
    # print(mas[1][0])
    
    
    global list_rel  # Используем глобальную переменную
    list_rel = []  # Очищаем список перед добавлением данных


    # Считаем сумму произведений
    for i in range(len(mas)):
        res = 0
        for j in range(n):
            res += mas[i][j] * a[j]
        list_rel.append([i + 1, res])  # Добавляем индекс и результат в list_rel

    print(f"raw mas {mas}\n")
    list_rel.sort(key=lambda x: x[1], reverse=True)  # Сортируем по второму элементу (по результату)
    # print(list_rel)



def mas_change(dok, el, val):
    mas[dok- 1][el-1] = val
    print(mas[dok- 1][el-1])
    count()



def print_dok(kolvo):
    for i in range(kolvo):
        print(list_rel[i], end=" ")
    print("\n")






# Вызов функции
count()

print_dok(2)
print_dok(10)

mas_change(4, 1, 1000)

print_dok(10)