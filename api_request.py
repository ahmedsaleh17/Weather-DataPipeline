import json
import requests
import os
from dotenv import load_dotenv


# make a request to api and return content
def make_request(api_url):

    print("Ingesting weather data from WeatherStack API...")
    try:
        # send a HTTP request and receive a response

        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        # weather json data
        data = response.json()
    
        return data  # json data

    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":

    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment variable
    api_key = os.getenv("WEATHERSTACK_API_KEY")

    if not api_key:
        raise ValueError("WEATHERSTACK_API_KEY not found. Please set it in your .env file.")

    api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

    # get weather data

    weather_data = make_request(api_url)

    print(weather_data)

    file_name = "weather_data_sample.json"

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=4)
