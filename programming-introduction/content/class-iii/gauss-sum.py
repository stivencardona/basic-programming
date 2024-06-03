# Dado un numero n quiero que me des la sumatoria de los numeros desde 1 hasta n
# n = 2 => sum = 1 + 2 = 3
# n = 4 => sum = 1 + 2 + 3 + 4 = 10
# n = 6 => sum = 1 + 2 + 3 + 4 + 5 + 6 = 21

# 1 , 2, 3, 4, 5, 6 => (n * (n + 1)) / 2

n = int(input())

sum = 0
numbers = range(n) # [0,1,2,3...,n-1] -> 0,1,2,3 -> 1, 2, 3, 4 
for x in numbers:
    sum += (x + 1)