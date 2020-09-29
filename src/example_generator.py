import random
from  random import randint


def generate_file(N=50, M=30, file_name='data/list_to_open.txt'):
    random.seed(239)
    file = open(file_name, 'w')
    n = N * randint(1, 20)
    file.write("N = " + str(N) + "\n")
    file.write("M = " + str(M) + "\n")
    for i in range(n):
        file.write(str(randint(1, N)) + ",")
    file.write(str(randint(1, N)))

if __name__ == '__main__':
    print("Введите N и M")
    #N = int(input())
    #M = int(input())
    generate_file()
