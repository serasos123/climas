from weather_api import update_weather_data
from data_display import print_sunrise_sunset_table, display_sorted_data
from data_analysis import analyze_weather_data 

def main_menu():
    print("\nBienvenido al Sistema de Consulta del Clima")
    while True:
        city = input("Ingrese la ciudad que desea buscar: ").strip()
        if not city:
            print("Error: La ciudad no puede estar vacía.\n")
            continue

        num_days_str = input("Ingrese la cantidad de días de historial que desea obtener: ").strip()
        if not num_days_str.isdigit():
            print("Error: La cantidad de días debe ser un número entero positivo.\n")
            continue

        num_days = int(num_days_str)
        if num_days <= 0:
            print("Error: La cantidad de días debe ser mayor que cero.\n")
            continue

        json_name = input("Ingrese el nombre del archivo donde desea guardar los datos (por ejemplo, clima_ciudades.json): ").strip()
        if not json_name:
            print("Error: El nombre del archivo no puede estar vacío.\n")
            continue

        updated_weather_data = update_weather_data(city, num_days, json_name)

        while True:
            print("\n¿Qué desea hacer ahora?")
            print("1. Estadísticas generales")
            print("2. Ordenar y ver datos por temperatura (máxima o mínima)")
            print("3. Ordenar y ver datos por humedad")
            print("4. Mostrar datos de amanecer y atardecer")
            print("5. Salir")

            choice = input("Ingrese su elección (1/2/3/4/5): ").strip()
            if choice == '1':
                stats_table = analyze_weather_data(updated_weather_data, json_name)
                print(stats_table)
            elif choice == '2':
                sort_options = {
                    "max": "min_temp",
                    "min": "max_temp"
                }
                sort_choice = input("Ordenar por temperatura máxima o mínima? (max/min): ").strip()
                column_name = sort_options.get(sort_choice)
                if column_name:
                    display_sorted_data(updated_weather_data, column_name)
                else:
                    print("Error: Opción de temperatura no válida.")
            elif choice == '3':
                display_sorted_data(updated_weather_data, 'avg_humidity')
            elif choice == '4':
                print_sunrise_sunset_table(updated_weather_data)
            elif choice == '5':
                print("Saliendo del sistema.")
                return
            else:
                print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nSaliendo del sistema.")

