import numpy as np
import pandas as pd
from tabulate import tabulate

def analyze_weather_data(data, json_name):
    df = pd.DataFrame(data)
    if 'max_temp' not in df.columns or 'min_temp' not in df.columns or 'avg_temp' not in df.columns or 'avg_humidity' not in df.columns:
        raise ValueError("Faltan columnas necesarias en los datos")
    
    max_global_temp = np.max(df['max_temp'])
    min_global_temp = np.min(df['min_temp'])
    max_temp_mean = np.mean(df['max_temp'])
    avg_temp_mean = np.mean(df['avg_temp'])
    avg_humidity_mean = np.mean(df['avg_humidity'])
    
    max_temp_std = np.std(df['max_temp'])
    avg_temp_std = np.std(df['avg_temp'])
    avg_humidity_std = np.std(df['avg_humidity'])
    avg_precip = np.mean(df['total_precip'])
    avg_visibility = np.mean(df['avg_visibility'])
    avg_rain_chance = np.mean(df['rain_chance'])
    max_wind_mean = np.mean(df['max_wind'])
    
    print()
    print(f"Muestras de los últimos {len(data)} días en: {json_name}")
    print()
    stats_list = [
        ["Max Temp", f"{max_global_temp:.2f}°C"],
        ["Min Temp", f"{min_global_temp:.2f}°C"],
        ["Max Temp (Media)", f"{max_temp_mean:.2f}°C"],
        ["Avg Temp (Media)", f"{avg_temp_mean:.2f}°C"],
        ["Avg Humidity", f"{avg_humidity_mean:.2f}%"],
        ["Std Max Temp", f"{max_temp_std:.2f}°C"],
        ["Std Avg Temp", f"{avg_temp_std:.2f}°C"],
        ["Std Avg Humidity", f"{avg_humidity_std:.2f}%"],
        ["Avg Precipitation", f"{avg_precip:.2f} mm"],
        ["Avg Visibility", f"{avg_visibility:.2f} km"],
        ["Avg Rain Chance", f"{avg_rain_chance:.2f}%"],
        ["Max Wind (Media)", f"{max_wind_mean:.2f} kph"],
    ]

    table = tabulate(stats_list, headers=["Estadística", "Valor"], tablefmt="grid")

    return table
