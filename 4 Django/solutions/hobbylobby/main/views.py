from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import Customer, City, State


def index(request):
    cities = City.objects.all().order_by('name')
    customers = Customer.objects.order_by('last_name')
    states = State.objects.order_by('name')
    # for state in states:
    #     print(type(state))
    #     print(state.id)
    #     print(state.name)
    context = {
        'title': 'List of Cities',
        'cities': cities,
        'customers': customers,
        'states': states
    }
    return render(request, 'main/index.html', context)


def receive_form(request):
    # print(request.GET)
    print(request.POST)
    
    city_name = request.POST['city_name']
    city_latitude = request.POST['city_latitude']
    city_longitude = request.POST['city_longitude']
    state_id = request.POST['state_id']

    # print(city_name)
    # print(city_latitude)
    # print(city_longitude)
    # print(state_id)

    state = State.objects.get(id=state_id)
    city = City(name=city_name, latitude=city_latitude, longitude=city_longitude, state=state)
    # city = City(name=city_name, latitude=city_latitude, longitude=city_longitude, state_id=state_id)
    city.save()


    # return HttpResponse('received form submission')
    return HttpResponseRedirect('/')



def template_example(request):
    context = {
        'title': 'Hobby Lobby',
        'user': {
            'first_name': 'Jane',
            'last_name': 'Fonda',
            'age':6
        },
        'text_color': 'white',
        'paint_colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    }
    return render(request, 'main/template_example.html', context)

def orm(request):

    # dual class/table representation
    # the fields of the class are like the columns of the table
    # the instances of the class are like the rows of the table


    # get a record =====================================
    # get a row out of our table
    # the object that represents the row is an instance of the class in models.py
    city = City.objects.get(name='Portland')
    # print(type(city))
    # city = City.objects.get(id=1)
    # city = City.objects.get(latitude=45.5051)
    # print(city.id)
    # print(city.name)
    # print(city.latitude)
    # print(city.longitude)
    # print(city.state)
    print(city.state.name) # Oregon
    # print(city.state_id)
    # print(type(city.state))
    # print()

    # cities_in_oregon = City.objects.filter(state_id=1)
    state = State.objects.get(name='Oregon')
    cities_in_oregon = state.cities.all()
    print(cities_in_oregon)


    # creating a new record ============================
    # oregon = State.objects.get(name='Oregon')
    # print(oregon.name)
    # print(type(oregon))
    # print(type(oregon))
    # city = City(name='Salem', latitude=44.9429, longitude=-123.0351, state=oregon)
    # city = City(name='Salem', latitude=44.9429, longitude=-123.0351, state_id=1)
    # city.save()

    # updading a record ============================
    # city = City.objects.get(name='Salemm')
    # city.name = 'Salem'
    # city.save()



    cities = City.objects.all()
    # print(cities)
    # print(list(cities))
    for city in cities:
        print(city.name)
    #     print(type(city))
    #     print(city.state.name)
    #     print(type(city.state))
    #     # print(city.state_id)
    #     # print(city.latitude)
    #     # print(city.longitude)
    #     print()

    # oregon_cities = City.objects.filter(state_id=1)
    # print(oregon_cities)

    # s_cities = City.objects.filter(name__startswith='S')
    # print(s_cities)

    # cities = City.objects.order_by('name')
    # print(cities)


    # s_cities_sorted = City.objects.filter(name__startswith='S').order_by('name')
    # print(s_cities_sorted)
    # if City.objects.filter(name='Corvallis').exists():
    #     print('corvallis exists')
    # else:
    #     print('corvallis does not exist')

    # city = City.objects.get(name='Corvallis')

    s_cities_sorted = City.objects.filter(name__startswith='S').order_by('name').first()
    print(s_cities_sorted)



    return HttpResponse('ok')


def about(request):
    return HttpResponseRedirect('https://www.google.com/')

def contactus(request):
    return JsonResponse({'name': 'bob', 'age': 55})

def redirect(request):
    # http://localhost:8000/?name=bob&age=55
    print(request.GET)
    name = request.GET['name']
    age = request.GET['age']
    return HttpResponse('Hello ' + name + ' you are ' + age + ' years old')
    