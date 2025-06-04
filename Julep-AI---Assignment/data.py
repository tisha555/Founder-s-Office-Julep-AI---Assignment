def get_restaurant(city, dish):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={dish}+in+{city}&key={PLACES_API_KEY}"
    res = requests.get(url).json()
    try:
        name = res["results"][0]["name"]
        address = res["results"][0]["formatted_address"]
    except:
        name = "Restaurant not found"
        address = "N/A"
    return name, address
