from django.shortcuts import render
from .models import Person
from django.http import JsonResponse

def index(request):
    context = {}
    person_list = Person.objects.all()
    context['person_list'] = person_list
    return render(request, 'index.html', context)

def person_json(request):
    persons = Person.objects.all()
    data = [person.to_dict_json() for person in persons]
    response = {'data': data}
    return JsonResponse(response)
