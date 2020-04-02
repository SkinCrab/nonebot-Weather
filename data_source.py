import json
import requests
import os

def read_file():
    with open(os.path.dirname(__file__).replace('\\','/')+"/_city.json",'rb') as r:
        data = json.load(r)
        return data

def get_city_code(city):
    file = read_file()
    n=0
    while(True) :
        if file[n]["city_name"] == "null":
            break
        else:
            if file[n]["city_name"] == city:
                return file[n]["city_code"]
            else:
                n += 1
    return -1


async def get_weather_of_city(city):
        code = get_city_code(city)
        if code == -1:
            return "未查询到该城市的信息"
        else:
            url = f"http://t.weather.sojson.com/api/weather/city/{code}"
            info = requests.get(url)
            weather = info.json()
            status = weather["status"]
            case = weather["data"]["forecast"]
            if status == 200 :
                update_time = weather["cityInfo"]["updateTime"]
                return f"""{weather["cityInfo"]["city"]}今天{case[0]["type"]}\n{case[0]["high"]}\n{case[0]["low"]}\n{case[0]["fx"]}\n风力：{case[0]["fl"]}"""
            else:
                return "error"