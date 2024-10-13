from django.shortcuts import render
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            # Fixed the typo in the URL (http://)
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' +
                city + '&units=metric&appid=d1268fd030e75143f6616767890d99bf'
            ).read()

            list_of_data = json.loads(source)

            # Corrected the key names for country code and coordinates
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + '°C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon']),
            }
            print(data)
        except Exception as e:
            # Handle errors, e.g., invalid city names or API issues
            print(f"Error: {e}")
            data = {}  # In case of an error, return an empty context
    else:
        data = {}  # Initialize data as an empty dictionary if the request is GET

    # Render the template with the data (or empty if GET)
    return render(request, "main/index.html", data)
