def read_number (prompt) -> int:
    """
    Solicita un número y lo retorna como int.
    Si la entrada es inválida, se solicita otra vez un numero.
    """
    while True:
        try:
            number = int( input (prompt))
            return number
        except ValueError as e:
            print(f"Input inválido, Error: {e}. Ingrese un número válido")

def calculate_change (change) -> str:
    """
    Funcion que calcula el vuelto en monedas de denominacin 500, 200, 100 y 50.
    Se debe devolver con la menor cantidad de monedas posible.
    Se imprime la cantidad de cada moneda separados por comas.
    """
    coins_500 = change // 500
    change = change - 500 * coins_500


    coins_200 = change // 200
    change = change - 200 * coins_200


    coins_100 = change // 100
    change = change - 100 * coins_100


    coins_50 = change // 50
    change = change - 50 * coins_50

    change = str(coins_500) + "," + str(coins_200) + "," + str(coins_100) + "," + str(coins_50)
    return change
 
change = read_number("Ingrese la cantidad a devolver: ")
print(calculate_change(change))