import pandas as pd
from tabulate import tabulate

def display_sorted_data(data, sort_by):
    df = pd.DataFrame(data)
    if sort_by not in df.columns:
        print(f"Error: La columna '{sort_by}' no existe en los datos.")
        return
    
    df_sorted = df.sort_values(by=sort_by)
    table = tabulate(df_sorted, headers="keys", tablefmt="grid")
    print(table)

def print_sunrise_sunset_table(weather_data):
    headers = ["Fecha", "Amanecer", "Atardecer", "Fase Lunar"]
    table_data = []
    for day in weather_data:
        row = [
            day['date'],
            day['sunrise'],
            day['sunset'],
            day['moon_phase']
        ]
        table_data.append(row)
    
    table = tabulate(table_data, headers=headers, tablefmt="grid")
    print(table)
