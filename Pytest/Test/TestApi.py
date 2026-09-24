import requests


def get_weather():
    # response = requests.get("https://api.weather.com")
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    return response.json()


# फंक्शन प्रत्यक्ष call करून बघण्यासाठी:
if __name__ == "__main__":
    result = get_weather()
    print(result)
