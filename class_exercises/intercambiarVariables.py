#intercambiar los valores de tres numeros hacia la derecha

x1, x2, x3 = 1, 2, 3
x1, x2, x3 = x3, x1, x2
print('estas son la x: \nx1: ' , x1 , '\nx2: ' , x2, '\nx3: ', x3) 

#Metodo con XOR

x1, x2, x3 = 1, 2, 3

x1 = x1 ^ x2 ^ x3
print(x1)
x2 = x1 ^ x2 ^ x3
print(x2)
x3 = x1 ^ x2 ^ x3
print(x3)
x1 = x1 ^ x2 ^ x3
print(x1)
print('estas son la x: \nx1: ' , x1 , '\nx2: ' , x2, '\nx3: ', x3) 
