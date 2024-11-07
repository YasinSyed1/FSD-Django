from django.shortcuts import render
from django.http import HttpResponse
from form2.models import Person1

# Create your views here.

def home(request):
  if request.method == 'POST':
      print(request.POST)
      name = request.POST['name']
      maths = request.POST['maths']
      physics = request.POST['physics']
      chemistry = request.POST['chemistry']
      Person1.objects.create(name=name,maths = maths, physics=physics, chemistry=chemistry)
      # return HttpResponse('Thank You Again!!!!!!!!!!!!!')
  
  
  return render(request, 'form2.html')
  
  
