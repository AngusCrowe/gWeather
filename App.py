from flask import Flask, render_template, request
from datetime import datetime, timedelta
import requests
import pytz

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
    k_max_temp0 = response3.get("daily")[0].get("temp").get("max")
    k_min_temp0 = response3.get("daily")[0].get("temp").get("min")

    icon11 = response3.get("daily")[1].get("weather")[0].get("icon")
    k_max_temp1 = response3.get("daily")[1].get("temp").get("max")
    k_min_temp1 = response3.get("daily")[1].get("temp").get("min")

    icon21 = response3.get("daily")[2].get("weather")[0].get("icon")
    k_max_temp2 = response3.get("daily")[2].get("temp").get("day")
    k_min_temp2 = response3.get("daily")[2].get("temp").get("night")

    icon31 = response3.get("daily")[3].get("weather")[0].get("icon")
    k_max_temp3 = response3.get("daily")[3].get("temp").get("day")
    k_min_temp3 = response3.get("daily")[3].get("temp").get("night")

    icon41 = response3.get("daily")[4].get("weather")[0].get("icon")
    k_max_temp4 = response3.get("daily")[4].get("temp").get("day")
    k_min_temp4 = response3.get("daily")[4].get("temp").get("night")

    icon51 = response3.get("daily")[5].get("weather")[0].get("icon")
    k_max_temp5 = response3.get("daily")[5].get("temp").get("day")
    k_min_temp5 = response3.get("daily")[5].get("temp").get("night")

    icon61 = response3.get("daily")[6].get("weather")[0].get("icon")
    k_max_temp6 = response3.get("daily")[6].get("temp").get("day")
    k_min_temp6 = response3.get("daily")[6].get("temp").get("night")

    local_timezone = response3.get("timezone")

    # main0 = response2.get("list")[0].get("main")
    # temp_value0 = main0['temp']
    # datetime0 = response2.get("list")[0].get('dt_txt')
    #
    # main1 = response2.get("list")[1].get("main")
    # temp_value1 = main1['temp']
    # datetime1 = response2.get("list")[1].get('dt_txt')
    #
    # main2 = response2.get("list")[2].get("main")
    # temp_value2 = main2['temp']
    # datetime2 = response2.get("list")[2].get('dt_txt')
    #
    # main3 = response2.get("list")[3].get("main")
    # temp_value3 = main3['temp']
    # datetime3 = response2.get("list")[3].get('dt_txt')
    #
    # main4 = response2.get("list")[4].get("main")
    # temp_value4 = main4['temp']
    # datetime4 = response2.get("list")[4].get('dt_txt')
    #
    # main5 = response2.get("list")[5].get("main")
    # temp_value5 = main5['temp']
    # datetime5 = response2.get("list")[5].get('dt_txt')
    #
    # temperatures = [temp_value0, temp_value1, temp_value2, temp_value3, temp_value4, temp_value5]
    # datetimes = [datetime0, datetime1, datetime2, datetime3, datetime4, datetime5]

    weather_list = response.get("weather", [{}])
    weather_one = weather_list[0]
    location = response.get("name")
    timestamp1 = response.get("dt")
    description = weather_one.get("description")
    temp_k = response.get("main", {}).get("temp")
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

    if measurement == "celsius":
        rounded_temp = round(int(temp_k) - 273.15)
        temp = str(rounded_temp) + "°C"
        min0 = str(round(int(k_min_temp0) - 273.15)) + "°C"
        min1 = str(round(int(k_min_temp1) - 273.15)) + "°C"
        min2 = str(round(int(k_min_temp2) - 273.15)) + "°C"
        min3 = str(round(int(k_min_temp3) - 273.15)) + "°C"
        min4 = str(round(int(k_min_temp4) - 273.15)) + "°C"
        min5 = str(round(int(k_min_temp5) - 273.15)) + "°C"
        min6 = str(round(int(k_min_temp6) - 273.15)) + "°C"
        max0 = str(round(int(k_max_temp0) - 273.15)) + "°C"
        max1 = str(round(int(k_max_temp1) - 273.15)) + "°C"
        max2 = str(round(int(k_max_temp2) - 273.15)) + "°C"
        max3 = str(round(int(k_max_temp3) - 273.15)) + "°C"
        max4 = str(round(int(k_max_temp4) - 273.15)) + "°C"
        max5 = str(round(int(k_max_temp5) - 273.15)) + "°C"
        max6 = str(round(int(k_max_temp6) - 273.15)) + "°C"

    elif measurement == "fahrenheit":
        rounded_temp = round((int(temp_k) - 273.15) * 1.8 + 32)
        temp = str(rounded_temp) + "°F"
        min0 = str(round((int(k_min_temp0) - 273.15) * 1.8 + 32)) + "°F"
        min1 = str(round((int(k_min_temp1) - 273.15) * 1.8 + 32)) + "°F"
        min2 = str(round((int(k_min_temp2) - 273.15) * 1.8 + 32)) + "°F"
        min3 = str(round((int(k_min_temp3) - 273.15) * 1.8 + 32)) + "°F"
        min4 = str(round((int(k_min_temp4) - 273.15) * 1.8 + 32)) + "°F"
        min5 = str(round((int(k_min_temp5) - 273.15) * 1.8 + 32)) + "°F"
        min6 = str(round((int(k_min_temp6) - 273.15) * 1.8 + 32)) + "°F"
        max0 = str(round((int(k_max_temp0) - 273.15) * 1.8 + 32)) + "°F"
        max1 = str(round((int(k_max_temp1) - 273.15) * 1.8 + 32)) + "°F"
        max2 = str(round((int(k_max_temp2) - 273.15) * 1.8 + 32)) + "°F"
        max3 = str(round((int(k_max_temp3) - 273.15) * 1.8 + 32)) + "°F"
        max4 = str(round((int(k_max_temp4) - 273.15) * 1.8 + 32)) + "°F"
        max5 = str(round((int(k_max_temp5) - 273.15) * 1.8 + 32)) + "°F"
        max6 = str(round((int(k_max_temp6) - 273.15) * 1.8 + 32)) + "°F"

    temps_dict = {
        "min0": min0,
        "min1": min1,
        "min2": min2,
        "min3": min3,
        "min4": min4,
        "min5": min5,
        "min6": min6,
        "max0": max0,
        "max1": max1,
        "max2": max2,
        "max3": max3,
        "max4": max4,
        "max5": max5,
        "max6": max6,
    }

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


    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    datetime_object551 = datetime.utcfromtimestamp(timestamp1)
    day_of_week = datetime_object551.weekday()

    datetime_object_utc = datetime.utcfromtimestamp(timestamp1)
    adelaide_timezone = pytz.timezone(local_timezone)
    datetime_object_adelaide = pytz.utc.localize(datetime_object_utc).astimezone(adelaide_timezone)
    time_string = datetime_object_adelaide.strftime("%H:%M")
    print("Local Time in Adelaide:", time_string)

    day1 = days_of_week[day_of_week]
    day2 = days_of_week[day_of_week + 1]
    day3 = days_of_week[day_of_week + 2]
    day4 = days_of_week[day_of_week + 3]
    day5 = days_of_week[day_of_week + 4]
    day6 = days_of_week[day_of_week + 5]
    day7 = days_of_week[day_of_week + 6]

    day_dict = {
        "time": time_string,
        "day1": day1,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "day7": day7
    }

    return render_template('weatherdata.html', weather_dict=weather_dict, response=response, icons_dict=icons_dict, temps_dict=temps_dict, day_dict=day_dict)

if __name__ == '__main__':
    app.run(debug=True)