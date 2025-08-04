from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kanpur'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1bd55fa538f4abaeb03e5146c947bee0'
    PARAMS = {'units': 'metric'}

    API_KEY = 'AIzaSyAj3my6zTNqLV9Bpxn9TlHfmukknIZ3cXA'
    SEARCH_ENGINE_ID = 'c2ab87c8b7cd140e4'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        # Weather API
        weather_data = requests.get(url, params=PARAMS).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        # Google Image Search API
        search_data = requests.get(city_url).json()
        search_items = search_data.get("items")
        image_url = search_items[0]['link'] if search_items else None

        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_ocurred': False,
            'image_url': image_url
        })

    except Exception as e:
        messages.error(request, 'This data is not available from the API')
        day = datetime.date.today()
        return render(request, 'index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_ocurred': True,
            'image_url':"https://wallpaperaccess.com/full/1638737.jpg"
        })
    
    print("Image URL:", image_url)
