# 🍽️ Foodie Tour Generator

[🌐 Live Demo](https://food-tour-generator.netlify.app/)

---

## 🌟 Overview

**Foodie Tour Generator** crafts a personalized one-day food itinerary tailored to your chosen city. By blending live weather updates, iconic local dishes, and top-rated restaurants, it designs perfect breakfast, lunch, and dinner experiences — indoors or outdoors, rain or shine!

---

## 🚀 Features

- 🔥 **Real-time Weather Check:** Suggests indoor/outdoor dining based on current weather.
- 🍛 **Iconic Local Dishes:** Picks 3 famous dishes unique to each city.
- 🍽️ **Top-Rated Restaurants:** Finds the best places serving those dishes using Google Places API.
- 📅 **Custom Foodie Tour:** Builds a complete day’s meal plan — breakfast, lunch, and dinner.
- 📱 **Responsive Design:** Seamless experience on desktop and mobile devices.

---

## 🛠️ How It Works

1. **Enter City:** Type your desired city in the search box.
2. **Fetch Weather:** Retrieves today's weather with OpenWeatherMap API.
3. **Select Dishes:** Picks 3 iconic dishes for that city from an internal database.
4. **Find Restaurants:** Searches Google Places API for top spots serving those dishes.
5. **Create Tour:** Suggests a food itinerary considering indoor/outdoor dining based on weather.
6. **Display:** Shows a clear, appetizing plan for all meals of the day.

---

## 🧰 Tech Stack

| Technology          | Role                              |
|---------------------|----------------------------------|
| React.js            | Frontend framework               |
| OpenWeatherMap API  | Weather data                     |
| Google Places API   | Restaurant information           |
| CSS3                | Responsive styling               |
| Netlify             | Deployment                      |

---

## 📸 Screenshots

### Home Page — Search Input

![Search Input](https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80)

### Foodie Tour Result Example

![Foodie Tour](https://images.unsplash.com/photo-1551218808-94e220e084d2?auto=format&fit=crop&w=800&q=80)

### Outdoor Dining Suggestion

![Outdoor Dining](https://images.unsplash.com/photo-1470770903676-69b98201ea1c?auto=format&fit=crop&w=800&q=80)

### Indoor Dining Suggestion

![Indoor Dining](https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80)

---
## 💻 How to Run Locally


# Clone the repository
git clone https://github.com/yourusername/foodie-tour-generator.git
cd foodie-tour-generator

# Install dependencies
npm install

# Create a .env file and add your API keys:
# REACT_APP_WEATHER_API_KEY=your_openweather_api_key
# REACT_APP_PLACES_API_KEY=your_google_places_api_key

# Start the development server
npm start

---
## 🔮 Future Improvements

- 🚀 Expand the city & dish database dynamically  
- 🌟 Add user reviews and restaurant ratings  
- 🗺️ Include an interactive map view  
- 🍃 Support dietary restrictions & allergies  
- ⏱️ Optimize meal stops by time and distance  

---

## 🙏 Credits

- Weather data by [OpenWeatherMap](https://openweathermap.org/)  
- Restaurant data by [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview)  
- Photos sourced from [Unsplash](https://unsplash.com/)  

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

