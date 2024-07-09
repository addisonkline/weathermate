import instructor
from pydantic import BaseModel
from openai import OpenAI
import os
import dotenv

# Define your desired output structure
class Forecast(BaseModel):
    forecast_today: str
    forecast_tonight: str
    forecast_tomorrow: str

def digest_forecast(raw_data: str) -> str:
    dotenv.load_dotenv()
    
    try:
        # Patch the OpenAI client
        client = instructor.from_openai(OpenAI(
            api_key = os.getenv('OPENAI_API_KEY')
        ))

        # Extract structured data from natural language
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=Forecast,
            messages=[
                { 
                    "role": "user", 
                    "content": f"Please parse through the following weather data and summarize it into 2-3 sentence forecasts for today, tonight, and tomorrow: {raw_data}. Make sure to include key details like exact temperatures."
                }
            ],
        )

        return f"Today: {response.forecast_today} \n \n Tonight: {response.forecast_tonight} \n \n Tomorrow: {response.forecast_tomorrow}"
    except Exception as e:
        print(f'Exception occurred in clean_forecast.digest_forecast: {e}')
        return "--"