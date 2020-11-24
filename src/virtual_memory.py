def read_sequence(file_name='data/sequence_example.txt'):
    file = open(file_name, 'r')
    file_text = file.read().split('\n')
    n = int(file_text[0][4:])
    m = int(file_text[1][4:])
    list_of_pages_char = file_text[2].rstrip().split(',')
    pages_numbers = []
    for i in list_of_pages_char:
        pages_numbers.append(int(i))
    file.close()
    return n, m, pages_numbers


def fifo_algo(m, pages_numbers):
    quantity_of_loads = 0
    use_pages = [pages_numbers[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != m:
        if use_pages.count(pages_numbers[k]) == 0:
            use_pages.append(pages_numbers[k])
        k += 1

    for i in range(len(pages_numbers) - k):  # Запускаем цикл на все элементы после k-ого
        if use_pages.count(pages_numbers[i + k]) == 0:
            use_pages = use_pages[1:] + [pages_numbers[i + k]]
            # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            quantity_of_loads += 1
    return quantity_of_loads


def lru_algo(m, pages_numbers):
    quantity_of_loads = 0
    use_pages = [pages_numbers[0]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages) != m:
        if use_pages.count(pages_numbers[k]) == 0:
            use_pages.append(pages_numbers[k])
        else:
            el = pages_numbers[k]
            use_pages = use_pages[0:use_pages.index(el)] + use_pages[use_pages.index(el) + 1:] + [el]
        k += 1

    for i in range(len(pages_numbers) - k):  # Запускаем цикл на все элементы после k-ого
        if use_pages.count(pages_numbers[i + k]) == 0:
            use_pages = use_pages[1:] + [pages_numbers[i + k]]
            # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            quantity_of_loads += 1
        else:
            el = pages_numbers[i + k]
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


def opt_algo(m, pages_numbers):
    list_of_pages_weight = [[], []]
    # Массив, где хранится, количество раз, когда страница встречается в последовательности
    for i in enumerate(pages_numbers):
        list_of_pages_weight[0].append(i[1])
        list_of_pages_weight[1].append(pages_numbers[i[0]:].count(i[1]))
    # for i in list_of_pages:
    #     list_of_pages_weight.append([i, list_of_pages.count(i)])

    quantity_of_loads = 0
    use_pages = [[list_of_pages_weight[0][0]], [list_of_pages_weight[1][0]]]
    k = 1  # k - показывает количество элементов взятых из списка страниц и загруженных в память,
    # k может быть больше M из-за повторяющихся страниц
    while len(use_pages[0]) != m:
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
    n, m, list_of_pages = read_sequence()
    print("FIFO " + str(fifo_algo(m, list_of_pages)))
    print("LRU " + str(lru_algo(m, list_of_pages)))
    print("OPT " + str(opt_algo(m, list_of_pages)))
    # print("Введите имя файла с последовательностью страниц")
    # file_name = input()
    # while not os.path.exists(file_name):
    #     print('Файла не существует')
    #     file_name = input()
    # N, M, list_of_pages = read_sequence(file_name)
