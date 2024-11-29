import json
import requests
import boto3
from datetime import datetime

# Initialize the boto3 S3 client
s3_client = boto3.client('s3')

# Define the API endpoint and API key (you need to replace with your actual key)
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = 'your_openweathermap_api_key_here'  # Replace this with your API key
S3_BUCKET_NAME = 'your-s3-bucket-name'  # Replace this with your S3 bucket name
S3_FILE_PREFIX = 'weather_data/'
S3_FILE_NAME = f"weather_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

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



# Function to write the fetched data into S3
def write_to_s3(data, bucket_name, file_name):
    try:
        # Convert the data to JSON string
        json_data = json.dumps(data)

        # Write the data to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json_data,
            ContentType='application/json'
        )
        print(f"Data successfully written to {file_name} in S3 bucket {bucket_name}")
    
    except Exception as e:
        raise Exception(f"Failed to write data to S3: {str(e)}")

# Lambda handler function
def lambda_handler(event, context):
    try:
        # Retrieve the city name from the event (could be passed as a parameter)
        city_name = event.get('city', 'Bengaluru')  # Default to 'Bengaluru' if no city is provided
        
        # Fetch the weather data for the city
        weather_data = fetch_weather_data(city_name)
        
        # Write the fetched data to S3
        write_to_s3(weather_data, S3_BUCKET_NAME, S3_FILE_PREFIX + S3_FILE_NAME)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully fetched weather data for {city_name} and uploaded to S3: {S3_FILE_NAME}")
        }

    except Exception as e:
        # Handle any error and return a failure response
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
