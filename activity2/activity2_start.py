from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    # TODO Using the Open Weather API, create your own app to retrieve temperature and weather descriptions of a particular city
    def get(self):
        link = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ae0433e337f9bf12a18792179628c98d"
        req = requests.get(link.format("Singapore")).json()

        weather = {
            "Temp": req["main"]["temp"],
            "Weather": req["weather"][0]["main"]
            }
        
        return weather

api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)
