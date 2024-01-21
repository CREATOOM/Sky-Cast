# make a virtual envirnment and install all the module
# import the flask module
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# make a route and render all the html templates in this route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')
        try:
            # take a variable to show the json data
            r = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=2cbb9e7e13c21acc8097206279632fd3')

            # read the json object
            json_object = r.json()

            # take some attributes like temperature,humidity,pressure of this
            temperature = int(json_object['main']['temp'] - 273.15)  # this temparetuure in kelvin
            humidity = int(json_object['main']['humidity'])
            pressure = int(json_object['main']['pressure'])
            wind = int(json_object['wind']['speed'])

            # atlast just pass the variables
            condition = json_object['weather'][0]['main']
            desc = json_object['weather'][0]['description']

            return render_template('home.html', temperature=temperature, pressure=pressure, humidity=humidity,
                                   city_name=city_name, condition=condition, wind=wind, desc=desc)

        except Exception as e:
            error_message = "Sorry yrr :) City Does Not Exits"
            return render_template('home.html', error_message=error_message)
    else:
        return render_template('home.html')


