def read_number (prompt) -> int:
    """
    Solicita un número y lo retorna como int.
    Si la entrada es inválida o negativa, se solicita otra vez un número.
    """
    while True:
        try:
            number = int( input (prompt))
            if number < 0:
                print("El número no puede ser negativo. Ingrese un número válido")
            else:
                return number
        except ValueError as e:
            print(f"Input inválido, Error: {e}. Ingrese un número válido")

def calculate_arrive_time (departure_time: int, departure_minute: int, departure_second: int, duration_time: int, duration_minute: int, duration_second: int) -> str:
    """
    Funcion que calcula la hora, minutos y segundos del aterrizaje de un vuelo
    """
    arrive_time, arrive_minute, arrive_second = 0, 0, 0

    arrive_second = departure_second + duration_second
    if (arrive_second > 59):
        arrive_minute += 1
        arrive_second -= 60
    
    arrive_minute += departure_minute + duration_minute
    if (departure_minute + duration_minute > 59):
        arrive_time += 1
        arrive_minute -= 60
    

    arrive_time += departure_time + duration_time
    if (arrive_time > 24):
        arrive_time = arrive_time % 24
    
    arrive = str(arrive_time) + ":" + str(arrive_minute) + ":" + str(arrive_second)
    return arrive

#main
departure_time = read_number("Hora de salida: ")
departure_minute = read_number("Minuto de salida: ")
departure_second = read_number("Segundo de salida: ")

duration_time = read_number("Horas de duración: ")
duration_minute  = read_number("Minutos de duración: ")
duration_second = read_number("Segundos de duración: ")

print(calculate_arrive_time(departure_time, departure_minute, departure_second, duration_time, duration_minute, duration_second))