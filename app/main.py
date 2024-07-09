from app.fetch_weather import get_forecast
from app.clean_forecast import digest_forecast
from app.send_email import send_email

def main():
    # first, get weather forecast for given location
    raw_forecast = get_forecast()

    # now, pass raw forecast data to GPT to digest
    cleaned_forecast = digest_forecast(raw_forecast)
    print(cleaned_forecast)

    # finally, send the forecast in an email to the "to" user specified
    send_email(cleaned_forecast)
    
main()