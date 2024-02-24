'''
Design a code that with a age given say if the person is an adult or not

'''
'''
1. Signature, description
2. Tests cases
3. Caso base
4. Crear nuestra
'''

'''
Int -> Boolean
Function that return True when age is greater or equal than 18 else False
'''
# def isAdult(age):
#     return False
def isAdult(age):
    if age >= 18:
        return True
    else:
        return False

assert isAdult(17) == False, "Should be false"
assert isAdult(19) == True, "Should be True"
assert isAdult(18) == True, "Should be True"