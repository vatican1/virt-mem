import os


def read_sequence(file_name='data/list_to_open.txt'):
    file = open(file_name, 'r')
    file = file.read().split('\n')
    N = int(file[0][4:])
    M = int(file[1][4:])
    list_of_pages_char = file[2].rstrip().split(',')
    list_of_pages = []
    for i in list_of_pages_char:
        list_of_pages.append(int(i))
    return N, M, list_of_pages


def fifo_algo(M, list_of_pages):
    quantity_of_loads = 0
    use_pages = [list_of_pages[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != M:
        if use_pages.count(list_of_pages[k]) == 0:
            use_pages.append(list_of_pages[k])
        k += 1

    for i in range(len(list_of_pages) - k):  # Запускаем цикл на все элементы после k-ого
        if use_pages.count(list_of_pages[i + k]) == 0:
            use_pages = use_pages[1:] + [list_of_pages[i + k]]
            # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            quantity_of_loads += 1
    return quantity_of_loads


def lru_algo(M, list_of_pages):
    quantity_of_loads = 0
    use_pages = [list_of_pages[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != M:
        if use_pages.count(list_of_pages[k]) == 0:
            use_pages.append(list_of_pages[k])
        else:
            el = list_of_pages[k]
            use_pages = use_pages[0:use_pages.index(el)] + use_pages[use_pages.index(el) + 1:] + [el]
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


def find_min(use_pages):  # [a,b,c,d,e][1,1,1,1,1]
    min_index_of_el = 0
    min_el = [use_pages[0][0], use_pages[1][0]]
    for i in enumerate(use_pages[1]):
        if i[1] < min_el[1]:
            min_el = [use_pages[0][i[0]], use_pages[1][i[0]]]
            min_index_of_el = i[0]
    return min_index_of_el


def opt_algo(M, list_of_pages):
    list_of_pages_weight = [[], []]
    # Массив, где хранится, количество раз, когда страница встречается в последовательности
    for i in enumerate(list_of_pages):
        list_of_pages_weight[0].append(i[1])
        list_of_pages_weight[1].append(list_of_pages[i[0]:].count(i[1]))
    # for i in list_of_pages:
    #     list_of_pages_weight.append([i, list_of_pages.count(i)])

    quantity_of_loads = 0
    use_pages = [[list_of_pages_weight[0][0]], [list_of_pages_weight[1][0]]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages[0]) != M:
        if use_pages[0].count(list_of_pages_weight[0][k]) == 0:
            use_pages[0].append(list_of_pages_weight[0][k])
            use_pages[1].append(list_of_pages_weight[1][k])
        k += 1

    for i in range(len(list_of_pages_weight[0]) - k):  # Запускаем цикл на все элементы после k-ого
        # print(list_of_pages_weight[i + k])
        if use_pages[0].count(list_of_pages_weight[0][i + k]) == 0:
            index_min = find_min(use_pages)  # тут находим индекс элемента, встречающегося минимальное количество раз
            use_pages[0] = use_pages[0][0:index_min] + use_pages[0][index_min + 1:] + [list_of_pages_weight[0][i + k]]
            use_pages[1] = use_pages[1][0:index_min] + use_pages[1][index_min + 1:] + [list_of_pages_weight[1][i + k]]
            # ставим вместо удалённой страницы
            quantity_of_loads += 1
    return quantity_of_loads


if __name__ == '__main__':
    N, M, list_of_pages = read_sequence()
    print("FIFO " + str(fifo_algo(M, list_of_pages)))
    print("LRU " + str(lru_algo(M, list_of_pages)))
    print("OPT " + str(opt_algo(M, list_of_pages)))
    # print("ВВедите имя файла с последовательностью страниц")
    # file_name = input()
    # while not os.path.exists(file_name):
    #     print('Файла не существует')
    #     file_name = input()
    # N, M, list_of_pages = read_sequence(file_name)
