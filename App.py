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

    main1 = response2.get("list")[1].get("main")
    temp_value1 = main1['temp']
    main2 = response2.get("list")[2].get("main")
    temp_value2 = main2['temp']
    main3 = response2.get("list")[3].get("main")
    temp_value3 = main3['temp']
    main4 = response2.get("list")[4].get("main")
    temp_value4 = main4['temp']
    main5 = response2.get("list")[5].get("main")
    temp_value5 = main5['temp']
    main6 = response2.get("list")[6].get("main")
    temp_value6 = main6['temp']
    main7 = response2.get("list")[7].get("main")
    temp_value7 = main7['temp']
    main8 = response2.get("list")[8].get("main")
    temp_value8 = main8['temp']
    main9 = response2.get("list")[9].get("main")
    temp_value9 = main9['temp']


    # datetime2 = response2.get("list")[1].get('dt')
    # print(datetime2)
    # datetime3 = response2.get("list")[2].get('dt')
    # print(datetime3)
    # datetime4 = response2.get("list")[3].get('dt')
    # print(datetime4)
    # datetime5 = response2.get("list")[4].get('dt')
    # print(datetime5)
    # datetime6 = response2.get("list")[5].get('dt')
    # print(datetime6)
    # datetime7 = response2.get("list")[6].get('dt')
    # print(datetime7)
    # datetime8 = response2.get("list")[7].get('dt')
    # print(datetime8)
    # datetime9 = response2.get("list")[8].get('dt')
    # print(datetime9)

    x_time2 = [0, 3, 6, 9, 12, 15, 18, 21]
    y_temp2 = [temp_value1, temp_value2, temp_value3, temp_value4, temp_value5, temp_value6, temp_value7, temp_value8]

    plt.plot(x_time2, y_temp2)
    plt.savefig("weather_chart")

    weather_list = response.get("weather", [{}])
    weather_one = weather_list[0]
    location = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    timestamp_local = datetime.fromtimestamp(timestamp)
    description = weather_one.get("description")
    temp_k = response.get("main", {}).get("temp")
    if measurement == "celsius":
        temp = str(int(temp_k) - 273.15) + "°C"
    elif measurement == "fahrenheit":
        temp = str(((int(temp_k) - 273.15) * 1.8) + 32) + "°F"
    wind_speed = response.get("wind", {}).get("speed")
    icon = weather_one.get("icon")

    weather_dict = {
        "location": location,
        "timezone": timezone,
        "timestamp_local": timestamp_local,
        "description": description,
        "temp": temp,
        "wind_speed": wind_speed,
        "icon": icon
    }

    return render_template('weatherdata.html', weather_dict=weather_dict, response=response)

if __name__ == '__main__':
    app.run(debug=True)