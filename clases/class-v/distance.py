import math
'''
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) 
and calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
'''

'''
1. Signature, description
2. Tests cases
3. Caso base
4. Crear nuestra funcion
'''

'''
Float, Float, Float, Float -> Float
Funcion que recibe las coordenadas en X e Y de dos puntos y retorna su distancia 
'''
# def distanceBetweenPoints(x1, y1, x2 , y2):
#     return 1.0

def distanceBetweenPoints(x1, y1, x2 , y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


assert distanceBetweenPoints(1,2,4,2) == 3.0, "Should be 3.0"
assert distanceBetweenPoints(1,1,1,1) == 0.0, "Should be 0.0"

p1 = input().split(" ") # "2.0 3.0"
p2 = input().split(" ") # "1.0 2.0"

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

distance = distanceBetweenPoints(x1, y1, x2, y2)

print("%.4f" % distance)