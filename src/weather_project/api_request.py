import requests
key = '1ea2213bd583da2aa7b4fb251af866ac'
request_url = f"https://api.weatherstack.com/current?access_key={key}&query=Wellington"

def fetch_data():
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        print('API response received!')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error orccured: {e}")
        raise

# fetch_data()

def fetch_mock_data():
    return {'request': {'type': 'City', 'query': 'Wellington, New Zealand', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Wellington', 'country': 'New Zealand', 'region': '', 'lat': '-41.300', 'lon': '174.783', 'timezone_id': 'Pacific/Auckland', 'localtime': '2026-05-26 00:50', 'localtime_epoch': 1779756600, 'utc_offset': '12.0'}, 'current': {'observation_time': '12:50 PM', 'temperature': 14, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '07:32 AM', 'sunset': '05:04 PM', 'moonrise': '02:08 PM', 'moonset': '02:10 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 75}, 'air_quality': {'co': '73.85', 'no2': '1.45', 'o3': '52', 'so2': '1.55', 'pm2_5': '4.45', 'pm10': '6.05', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 30, 'wind_degree': 351, 'wind_dir': 'N', 'pressure': 1021, 'precip': 0, 'humidity': 82, 'cloudcover': 75, 'feelslike': 12, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}
