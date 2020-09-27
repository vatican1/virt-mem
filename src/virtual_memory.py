import os


def read_sequence(file_name='data/example1.txt'):
    file = open(file_name, 'r')
    file = file.read().split('\n')
    N = int(file[0][4:])
    M = int(file[1][4:])
    list_of_pages_char = file[2].rstrip().split(',')
    list_of_pages = []
    for i in list_of_pages_char:
        list_of_pages.append(int(i))
    return N, M, list_of_pages


def FIFO_algo(M, list_of_pages):
    quantity_of_loads = 1
    use_pages = [list_of_pages[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память, k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != M:
        if use_pages.count(list_of_pages[k]) == 0:
            use_pages.append(list_of_pages[k])
            quantity_of_loads += 1
        k += 1

    for i in range(len(list_of_pages) - k):  # Запускаем цикл на все элементы после k-ого
        if use_pages.count(list_of_pages[i + k]) == 0:
            use_pages = use_pages[1:] + [list_of_pages[i + k]]
            # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            quantity_of_loads += 1
    return quantity_of_loads


def LRU_algo(M, list_of_pages):
    quantity_of_loads = 1
    use_pages = [list_of_pages[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память, k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != M:
        if use_pages.count(list_of_pages[k]) == 0:
            use_pages.append(list_of_pages[k])
            quantity_of_loads += 1
        else:
            el = list_of_pages[k]
            use_pages = use_pages[0:use_pages.index(el)] + use_pages[use_pages.index(el) + 1:] + el
        k += 1

    for i in range(len(list_of_pages) - k):  # Запускаем цикл на все элементы после k-ого
        if use_pages.count(list_of_pages[i + k]) == 0:
            use_pages = use_pages[1:] + [list_of_pages[i + k]]
            # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            quantity_of_loads += 1
        else:
            el = list_of_pages[i + k]
            use_pages = use_pages[0:use_pages.index(el)] + use_pages[use_pages.index(el) + 1:] + [el]
    return quantity_of_loads


def find_min(use_pages):
    min = use_pages[0][1]
    min_arr = use_pages[0]
    for i in use_pages:
        if i[1] < min:
            min_arr = i
    return min_arr


def OPT_algo(M, list_of_pages):
    list_of_pages_weight = []  # Массив, где хранится, количество раз, когда страница встречается в последовательности
    for i in list_of_pages:
        list_of_pages_weight.append([i, list_of_pages.count(i)])

    quantity_of_loads = 1
    use_pages = [list_of_pages_weight[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память, k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != M:
        if use_pages.count(list_of_pages_weight[k]) == 0:
            use_pages.append(list_of_pages_weight[k])
            quantity_of_loads += 1
        k += 1

    for i in range(len(list_of_pages_weight) - k):  # Запускаем цикл на все элементы после k-ого
        print(list_of_pages_weight[i + k])
        if use_pages.count(list_of_pages_weight[i + k]) == 0:
            min = find_min(use_pages)  # тут находим элемент, встречающийся минимальное количество раз
            use_pages = use_pages[0:use_pages.index(min)] + use_pages[use_pages.index(min) + 1:] + [
                list_of_pages_weight[i + k]]  # ставим вместо удалённой страницы
            quantity_of_loads += 1
    return quantity_of_loads


if __name__ == '__main__':
    N, M, list_of_pages = read_sequence()
    print("FIFO " + str(FIFO_algo(M, list_of_pages)))
    print("LRU " + str(LRU_algo(M, list_of_pages)))
    print(OPT_algo(M, list_of_pages))
    # print("ВВедите имя файла с последовательностью страниц")
    # file_name = input()
    # while not os.path.exists(file_name):
    #     print('Файла не существует')
    #     file_name = input()
    # N, M, list_of_pages = read_sequence(file_name)
