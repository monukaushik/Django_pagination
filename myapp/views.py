from django.shortcuts import render
from django.core.paginator import Paginator
# from faker import Faker
# import random
from .models import *

# faker=Faker()
# num=int(input("Enter a no : "))
# for _ in range(1,num+1):
#       name=faker.name()
#       rollno=random.randint(1,100)
#       city=faker.city()
#       state=faker.state()
#       Student.objects.create(name=name,rollno=rollno,city=city,state=state)
      
# Create your views here.
def index(request):

   data=Student.objects.all()
   paginator=Paginator(data,10)
   
   page=request.GET.get('page')  
   print('#####',page)
   obj=paginator.get_page(page)
   
   print('@@@@',obj)
   
       
   return render(request,'index.html',{'data':obj})