import requests
from django.conf import settings
from django.shortcuts import render

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        print(data)  # Debugging: Print the API response

        if data.get('cod') == 200:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'wind_deg': data['wind']['deg'],
                'clouds': data['clouds']['all'],
                'visibility': data.get('visibility', 'N/A'),
                'sunrise': data['sys']['sunrise'],
                'sunset': data['sys']['sunset'],
            }
        else:
            weather_data = {'error': data.get('message', 'City not found')}

        return render(request, 'weather/index.html', {'weather': weather_data})

    return render(request, 'weather/index.html')