from flask import Flask, render_template, request
from datetime import datetime
import requests

from matplotlib import pyplot as plt

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():

    # x_time = [0, 1, 2, 3, 4, 5, 6, 7]
    # y_temp = [25, 30, 32, 28, 21, 19, 18, 17]
    # plt.plot(x_time, y_temp)
    # plt.savefig("test_chart")

    return render_template('home.html')

@app.route('/weatherdata', methods=["GET", "POST"])
def results():
    api_key = "61e2ac5c5dec09d272ffdbfbfe7e27d2"
    form_city = request.form.get('city')
    form_lat = request.form.get('latitude')
    form_lon = request.form.get('longitude')
    measurement = request.form.get('measurement')
    if not form_city:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + form_lat + "&lon=" + form_lon + "&appid=" + api_key
        url2 = "https://api.openweathermap.org/data/2.5/forecast?lat=" + form_lat + "&lon="+ form_lon + "&appid=" + api_key
    else:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&APPID=" + api_key
        url2 = "https://api.openweathermap.org/data/2.5/forecast?q=" + form_city + "&appid=" + api_key

    print(url)
    print(url2)

    response = requests.get(url).json()
    response2 = requests.get(url2).json()

    weatherinfo = response2.get("list")

    latitude_value = response.get("coord", {}).get("lat")
    longitude_value = response.get("coord", {}).get("lon")
    url3 = "https://api.openweathermap.org/data/3.0/onecall?lat=" + str(latitude_value) + "&lon=" + str(longitude_value) + "&exclude=current,minutely,hourly,alerts&appid=" + api_key
    print(url3)

    response3 = requests.get(url3).json()

    icon01 = response3.get("daily")[0].get("weather")[0].get("icon")
    icon11 = response3.get("daily")[1].get("weather")[0].get("icon")
    icon21 = response3.get("daily")[2].get("weather")[0].get("icon")
    icon31 = response3.get("daily")[3].get("weather")[0].get("icon")
    icon41 = response3.get("daily")[4].get("weather")[0].get("icon")
    icon51 = response3.get("daily")[5].get("weather")[0].get("icon")
    icon61 = response3.get("daily")[6].get("weather")[0].get("icon")

    main0 = response2.get("list")[0].get("main")
    temp_value0 = main0['temp']
    datetime0 = response2.get("list")[0].get('dt_txt')

    main1 = response2.get("list")[1].get("main")
    temp_value1 = main1['temp']
    datetime1 = response2.get("list")[1].get('dt_txt')

    main2 = response2.get("list")[2].get("main")
    temp_value2 = main2['temp']
    datetime2 = response2.get("list")[2].get('dt_txt')

    main3 = response2.get("list")[3].get("main")
    temp_value3 = main3['temp']
    datetime3 = response2.get("list")[3].get('dt_txt')

    main4 = response2.get("list")[4].get("main")
    temp_value4 = main4['temp']
    datetime4 = response2.get("list")[4].get('dt_txt')

    main5 = response2.get("list")[5].get("main")
    temp_value5 = main5['temp']
    datetime5 = response2.get("list")[5].get('dt_txt')

    temperatures = [temp_value0, temp_value1, temp_value2, temp_value3, temp_value4, temp_value5]
    datetimes = [datetime0, datetime1, datetime2, datetime3, datetime4, datetime5]

    weather_list = response.get("weather", [{}])
    weather_one = weather_list[0]
    location = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    timestamp_local = datetime.fromtimestamp(timestamp)
    description = weather_one.get("description")
    temp_k = response.get("main", {}).get("temp")
    if measurement == "celsius":
        rounded_temp = round(int(temp_k) - 273.15)
        temp = str(rounded_temp) + "°C"
    elif measurement == "fahrenheit":
        rounded_temp = round((int(temp_k) - 273.15) * 1.8 + 32)
        temp = str(rounded_temp) + "°F"
    wind_speed_metres = response.get("wind", {}).get("speed")
    wind_speed = round((int(wind_speed_metres) * 3.6))
    icon = weather_one.get("icon")
    icon_link_current = "https://openweathermap.org/img/wn/" + icon + "@2x.png"
    icon0 = "https://openweathermap.org/img/wn/" + icon01 + "@2x.png"
    icon1 = "https://openweathermap.org/img/wn/" + icon11 + "@2x.png"
    icon2 = "https://openweathermap.org/img/wn/" + icon21 + "@2x.png"
    icon3 = "https://openweathermap.org/img/wn/" + icon31 + "@2x.png"
    icon4 = "https://openweathermap.org/img/wn/" + icon41 + "@2x.png"
    icon5 = "https://openweathermap.org/img/wn/" + icon51 + "@2x.png"
    icon6 = "https://openweathermap.org/img/wn/" + icon61 + "@2x.png"
    humidity = response.get("main", {}).get("humidity")

    icons_dict = {
        "icon0": icon0,
        "icon1": icon1,
        "icon2": icon2,
        "icon3": icon3,
        "icon4": icon4,
        "icon5": icon5,
        "icon6": icon6
    }

    weather_dict = {
        "location": location,
        "description": description,
        "temp": temp,
        "wind_speed": wind_speed,
        "icon_link_current": icon_link_current,
        "humidity": humidity
    }

    return render_template('weatherdata.html', weather_dict=weather_dict, response=response, icons_dict=icons_dict)

if __name__ == '__main__':
    app.run(debug=True)