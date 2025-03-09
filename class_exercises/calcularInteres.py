def read_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError as e:
            print(f"Input incorrecto ({e}). Ingrese un numero válido")

def get_total_interest(capital, interest_rate, years):
    return capital * (1 + (interest_rate / 100)) ** years


capital = read_number("Ingrese el capital:")
interest_rate = read_number("Ingrese la tasa de interés:")
years = read_number("Ingrese la cantidad de años:")
total_ammount = get_total_interest(capital, interest_rate, years)
print(f"El total es: ${total_ammount:.2f}")