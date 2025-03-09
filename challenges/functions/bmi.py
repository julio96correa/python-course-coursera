def read_number (prompt) -> float:
    while True:
        try:
            number = float( input(prompt).strip())
            return number
        except ValueError as e:
            print(f"Input incorrecto ({e}). Ingrese un número válido")

def get_bmi(weight_lb: float, height_inch: float) -> float:
    
    """
        Function that calculates the body mass index
    """

    bmi = ( weight_lb / (height_inch ** 2) ) * 703
    return bmi

#main
weight_lb = read_number("Ingrese el peso en libras: ")       
height_inch = read_number("Ingrese la altura en pulgadas: ")       
bmi = get_bmi(weight_lb, height_inch)
print(f"Su índice de masa corporal es {bmi:.2f}")