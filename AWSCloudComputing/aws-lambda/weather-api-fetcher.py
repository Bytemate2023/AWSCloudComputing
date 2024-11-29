import json
import requests

def lambda_handler(event, context):
    city = 'Bengaluru'
    api_key = 'your_api_key'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    weather_data = response.json()

    return {
        'statusCode': 200,
        'body': json.dumps(weather_data)
    }
