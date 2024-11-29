import json
import requests
from datetime import datetime


# Define the API endpoint and API key (you need to replace with your actual key)
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '05c7f8b28705511925335e9de0c1ab9a'  # Replace this with your API key


# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather_data(city):
    res_payload = {}
    params = {
        'q': city,           # City name
        'appid': API_KEY,    # API Key
        'units': 'metric'    # Temperature in Celsius (optional, you can adjust it)
    }
    
    response = requests.get(API_URL, params=params)
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found
    if response.status_code == 200:
        x = response.json()
        
        if x["cod"] != "404": 
          
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
          
            # store the value corresponding 
            # to the "temp" key of y 
            res_payload["current-temperature"] = y["temp"] 
          
            # store the value corresponding 
            # to the "pressure" key of y 
            res_payload["current-pressure"] = y["pressure"] 
          
            # store the value corresponding 
            # to the "humidity" key of y 
            res_payload["current-humidiy"] = y["humidity"]

            # key in variable z 
            z = x["weather"] 
          
            # store the value of "weather" 
            # key in variable z 
            res_payload["description"] = z[0]["description"]  
            return res_payload  # Return the weather data as JSON if successful
    else:
        raise Exception(f"Failed to fetch data from API. Status Code: {response.status_code}")


# Lambda handler function
def lambda_handler(event, context):
    try:
        # Retrieve the city name from the event (could be passed as a parameter)
        city_name = event.get('city', 'Bengaluru')  # Default to 'Bengaluru' if no city is provided
        
        # Fetch the weather data for the city
        weather_data = fetch_weather_data(city_name)
        

        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully fetched weather data for {city_name}"),
            'response' : weather_data
        }

    except Exception as e:
        # Handle any error and return a failure response
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

print(lambda_handler({'city':"Bengaluru"},{}))
