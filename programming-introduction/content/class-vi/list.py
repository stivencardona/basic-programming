'''
Dado un conjunto de numeros, realice lo siguiente con ellos
1. Guarde esos numeros en una lista
2. Cree una funcion que retorne la suma de los elementos de esa lista
3. Cree una funcion que retorne el menor y el mayor de esa lista
4. Cree una funcion que retorne otra lista con los elementos elevados
'''

'''
1. Solution
'''

numeros = input().split(" ")

def cast_to_int(lista_of_strings):
    result = []
    for s in lista_of_strings:
        result.append(int(s))
    return result


list_of_numbers = cast_to_int(numeros)

'''
2. Suma de elementos
'''

def sum(list_of_numbers):
    accumulate = 0
    for number in list_of_numbers:
        accumulate = accumulate + number
    return accumulate

# print(sum(list_of_numbers))

'''
3. Minor & Mayor in a list of numbers
'''

def minor(list_of_numbers):
    minor = 100000000000

    for number in list_of_numbers:
        if number < minor:
            minor = number
    
    return minor

def mayor(list_of_numbers):
    mayor = -100000000000

    for number in list_of_numbers:
        if number > mayor:
            mayor = number
    
    return mayor

# print(mayor(list_of_numbers))


'''
4. Create a list with the square of the elements of another list
'''

def square_list(list_of_numbers):
    result = []
    for number in list_of_numbers:
        result.append(number**2)
    return result
