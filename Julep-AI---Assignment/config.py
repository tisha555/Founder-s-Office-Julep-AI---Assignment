def foodie_tour(city):
    weather_type = get_weather(city)
    dishes = city_dishes.get(city, [])
    
    print(f"\n🍽️ {city} Foodie Tour ({weather_type} dining suggested):\n")

    meals = ["Breakfast", "Lunch", "Dinner"]
    for i, dish in enumerate(dishes):
        name, address = get_restaurant(city, dish)
        print(f"{meals[i]} - Try {dish} at {name} ({address})")
