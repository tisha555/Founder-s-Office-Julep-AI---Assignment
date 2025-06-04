def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    weather = res["weather"][0]["main"]
    return "Outdoor" if weather in ["Clear", "Clouds"] else "Indoor"
