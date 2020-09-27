import os


def read_sequence(file_name):
    file = open(file_name, 'r')
    file = file.read().split('\n')
    N = int(file[0][4:])
    M = int(file[1][4:])
    list_of_pages_char = file[2].split(',')
    list_of_pages = []
    for i in list_of_pages_char:
        list_of_pages.append(int(i))
    return N, M, list_of_pages


def FIFO_algo(M, list_of_pages):
    quantity_of_loads = 0
    use_pages = []
    k = 0  # k - показывает количество элементов взятых из списка страниц и загруженных в память, k может быть больше M из-за повторяющихся страниц
    while len(use_pages != M):
        if use_pages.count(list_of_pages[k]) == -1:
            use_pages.append(list_of_pages[k])
            ++k
            ++quantity_of_loads

    for i in range(len(list_of_pages) - k):
        if use_pages.count(list_of_pages[i]) == -1:
            use_pages = [list_of_pages[i],
                         use_pages[0:-1]]  # если страницы нет в памяти - выгружаем последнюю и добавляем новую в начало
            ++quantity_of_loads
    return quantity_of_loads


if __name__ == '__main__':

    read_sequence('data/example.txt')
    print("ВВедите имя файла с последовательностью страниц")
    file_name = input()
    while not os.path.exists(file_name):
        print('Файла не существует')
        file_name = input()
    N, M, list_of_pages = read_sequence(file_name)
