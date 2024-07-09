import dotenv
import os
import requests

def get_forecast() -> str:
    dotenv.load_dotenv()

    try:
        wfo = os.getenv('WFO')
        location_x = os.getenv('LOCATION_X')
        location_y = os.getenv('LOCATION_Y')

        url = f'https://api.weather.gov/gridpoints/{wfo}/{location_x},{location_y}/forecast'
        response = requests.get(url)

        if not response.status_code == 200:
            print(f'Error in fetch_weather.get_forecast: Weather.gov GET request failed with status code {response.status_code}')
            return "--"
        else:
            response_json = response.json()
            relevant_info = response_json['properties']['periods'][0:3]
            return relevant_info

    except Exception as e:
        print(f'The following exception occurred in fetch_weather.get_forecast: {e}')
        return "--"

get_forecast()