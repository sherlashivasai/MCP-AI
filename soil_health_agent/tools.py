import os
import requests
import json
import random
from langchain_core.tools import tool
# No Pydantic needed anymore
# from pydantic import BaseModel, Field 

@tool
def get_weather_info(location: str) -> str:
    """
    Gets the current weather for a specified location, including temperature,
    humidity, rainfall (last hour), and light condition (weather description).
    """
    # 1. Get the API key from environment variables
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    
    if not api_key:
        return "Error: OPENWEATHER_API_KEY environment variable not set."

    # 2. Define the API endpoint and parameters
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    # 3. Call the API
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        return f"Error: API request failed. {e}"

    # 4. Check for a valid response
    if response.status_code == 200:
        data = response.json()
        
        # 5. Safely extract the data
        main_data = data.get("main", {})
        weather_data = data.get("weather", [{}])[0]
        rain_data = data.get("rain", {})

        temperature = main_data.get("temp")
        humidity = main_data.get("humidity")
        light_condition = weather_data.get("description")
        rainfall_1h = rain_data.get("1h", 0) 

        # 6. Format the output as a JSON string for the agent
        result = {
            "location": data.get("name"),
            "temperature_celsius": temperature,
            "humidity_percent": humidity,
            "rainfall_last_1hr_mm": rainfall_1h,
            "light_condition": light_condition
        }
        return json.dumps(result, indent=2)
        
    else:
        return f"Error: Could not find weather for {location}. Status code: {response.status_code}"


# --- FIX: Updated the tool to take 'location' string ---

@tool
def get_soil_npk(location: str) -> str:
    """
    Gets DUMMY soil NPK (Nitrogen, Phosphorus, Potassium) content 
    for a specific location.
    This tool returns random values and does not call a real API.
    """
    
    # Generate random values for each property and depth
    n_0_5 = random.randint(3000, 7000)
    n_5_15 = random.randint(2000, 5000)
    p_0_5 = random.randint(1500, 2500)
    p_5_15 = random.randint(1000, 2000)
    k_0_5 = random.randint(8000, 13000)
    k_5_15 = random.randint(9000, 14000)

    # 1. Create the dummy data structure
    simplified_data = {
        "location": location, # Added location
        "source": "Dummy Data (Randomly Generated)",
        "soil_properties": {
            "n_0-5cm": f"{n_0_5} dg/kg",
            "n_5-15cm": f"{n_5_15} dg/kg",
            "p_0-5cm": f"{p_0_5} mg/kg",
            "p_5-15cm": f"{p_5_15} mg/kg",
            "k_0-5cm": f"{k_0_5} cg/kg",
            "k_5-15cm": f"{k_5_15} cg/kg"
        }
    }

    # 2. Return the data as a clean JSON string
    return json.dumps(simplified_data, indent=2)