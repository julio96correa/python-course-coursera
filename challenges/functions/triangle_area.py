import math

def read_number (prompt) -> float:
    while True:
        try:
            return float( input(prompt).strip())
        except ValueError as e:
            print("Input incorrecto ({e}). Ingrese un número válido.")

def triangle_area(s1: float, s2:float, s3:float) -> float:
    subperimeter = get_subperimeter(s1,s2,s3)
    area = get_area(subperimeter, s1, s2, s3)
    return area 


def get_subperimeter(s1:float, s2: float, s3: float) -> float:
    subperimeter = (s1+s2+s3)/2
    return subperimeter

def get_area(subperimeter: float, s1: float, s2: float, s3: float) -> float:
    area = math.sqrt((subperimeter * (subperimeter-s1) * (subperimeter-s2) * (subperimeter-s3)))
    return area

#Main
s1 = read_number("Ingrese el valor del lado:")
s2 = read_number("Ingrese el valor del lado:")
s3 = read_number("Ingrese el valor del lado:")
area = triangle_area(s1, s2, s3)
print(f"El area del triangulo es ({area:.1f})")
