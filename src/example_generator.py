from random import randint

print("Введите N и M")
N = int(input())
M = int(input())
file = open('data/example.txt', 'w')
n = N * randint(1, 20) // 10
file.write("N = "+str(N)+"\n")
file.write("M = "+str(M)+"\n")
for i in range(n):
    file.write(str(randint(1, N))+",")
file.write(str(randint(1, N)))
