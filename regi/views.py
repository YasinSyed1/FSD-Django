from django.shortcuts import render
from django.http import HttpResponse
from regi.models import Person
# Create your views here.

def home(request):
    if request.method == 'POST':
      print(request.POST)
      name = request.POST['name']
      mob_num = request.POST['mob_num']
      hobbies = request.POST['hobbies']
      Person.objects.create(name=name,mobile_num = mob_num, hobbies=hobbies)
      # return HttpResponse('Thank You!!!!!!!!!!!!!')
    all_hobbies = Person.objects.all
    
    return render(request, 'form1.html', {'hobbies':all_hobbies})
  
  
