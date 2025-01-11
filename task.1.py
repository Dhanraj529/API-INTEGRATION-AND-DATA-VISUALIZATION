import requests
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_weather_data(city, api_key):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code, response.text)
        return None

def parse_weather_data(data):
    if data and "current" in data:
        temperature = data["current"]["temperature"]
        observation_time = data["current"]["observation_time"]
        return temperature, observation_time
    else:
        print("Invalid data format.")
        return None, None

def visualize_weather(city, temperature, observation_time):
    sns.set(style="whitegrid")
    plt.figure(figsize=(6, 4))
    plt.bar(city, temperature, color="skyblue")
    plt.title(f"Current Temperature in {city}")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.ylim(0, max(temperature + 5, 40))
    plt.text(city, temperature, f"{temperature}°C", ha='center', va='bottom', fontsize=12)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    API_KEY = "dd1817a0306b7b1e3da8c42aa78cd8b7"  
    city = "Pune"  
    
    weather_data = fetch_weather_data(city, API_KEY)
    temperature, observation_time = parse_weather_data(weather_data)
    
    if temperature is not None:
        
        visualize_weather(city, temperature, observation_time)
