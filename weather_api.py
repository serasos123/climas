import requests
import json
from datetime import datetime, timedelta

API_KEY = "c1d6e3fb52794fdb8d9235747241109" 
BASE_URL = "http://api.weatherapi.com/v1/history.json"

def get_weather_data(city, date):
    params = {
            "key": API_KEY,
            "q": city,
            "dt": date,
    }
    print(f"{BASE_URL}?key={params['key']}&q={params['q']}&dt={params['dt']}")
    response = requests.get(BASE_URL , params=params)
    print("status_response: ", response.status_code)
    if(response.status_code == 200):
        return response.json()
    else:
        error = response.json()
        error_message = error["error"]["message"]
        print(f"Error obtaining API data: {error_message}")

def get_past_days_weather(city, num_days):
    today = datetime.now()
    weather_data = []
    for i in range(num_days):
        date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        data = get_weather_data(city, date)
        if(data):
            main = data["forecast"]["forecastday"];
            date_info = {
                "date": date,
                "max_temp": main[0]["day"]["maxtemp_c"],
                "min_temp": main[0]["day"]["mintemp_c"],
                "avg_temp": main[0]["day"]["avgtemp_c"],
                "max_wind": main[0]["day"]["maxwind_kph"],
                "avg_humidity": main[0]["day"]["avghumidity"],
                "total_precip": main[0]["day"]["totalprecip_mm"],
                "avg_visibility": main[0]["day"]["avgvis_km"],
                "rain_chance": main[0]["day"]["daily_chance_of_rain"],
                "condition": main[0]["day"]["condition"]["text"],
                "sunrise": data["forecast"]["forecastday"][0]["astro"]["sunrise"],
                "sunset": data["forecast"]["forecastday"][0]["astro"]["sunset"],
                "moon_phase": data["forecast"]["forecastday"][0]["astro"]["moon_phase"],
            }
            weather_data.append(date_info)
    return weather_data

def update_weather_data(city, num_days, json_name):
    past_weather = get_past_days_weather(city, num_days)

    with open(json_name, 'w') as archivo_json:
        json.dump(past_weather, archivo_json, indent=4)
    print(f"datos guardados en {json_name}")

    return past_weather

