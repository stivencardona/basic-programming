# vas a recibir un numero n la cantidad de numeros que tendras que leer
# vas a recibir n numeros enteros
# debes dar como resultado el numero mas grande y el numero mas pequeno de esos numeros
# n = 5
# x1 = 2, x2 = 10, ... x5 = 6

n = int(input())

greater = -10000000000000
lowest = 10000000000000
for i in range(n):
    x = int(input())
    if x > greater:
        greater = x
    if x < lowest:
        lowest = x

print(greater, lowest)
    