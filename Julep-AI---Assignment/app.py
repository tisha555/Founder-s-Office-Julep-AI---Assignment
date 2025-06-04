from flask import Flask, render_template, request
import weather, restaurants, data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    foodie_plan = None
    if request.method == 'POST':
        city = request.form['city']
        weather_type = weather.get_weather(city)
        dishes = data.city_dishes.get(city, [])
        plan = []
        meals = ["Breakfast", "Lunch", "Dinner"]
        for i, dish in enumerate(dishes):
            name, address = restaurants.get_restaurant(city, dish)
            plan.append({'meal': meals[i], 'dish': dish, 'name': name, 'address': address})
        foodie_plan = {'city': city, 'weather': weather_type, 'plan': plan}
    return render_template('index.html', foodie_plan=foodie_plan)

if __name__ == '__main__':
    app.run(debug=True)
