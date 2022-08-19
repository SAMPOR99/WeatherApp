from django.shortcuts import render
import json
import urllib.request
from decouple import config
secret_api_key = config("secret_api_key")

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=' + secret_api_key).read()
        json_data = json.loads(res)
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + "k",
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ""
        data = {}
    return render(request, 'index.html',  {"city": city, "data": data})
