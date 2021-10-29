from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    #return HttpResponse('Hello World')
    #return render(request,'base.html', context={'name': 'PN'})
    pass

def root(request):
    return render(request, 'index.html',context={'user':request.user})

def squar(request):
   #num = request.GET['numb']
   #num = int(num)
   #result = num**2
   return render(request, 'base.html', context={'op': 'result'})

def square(request):
   num = request.POST['numb']
   num = int(num)
   result = num**2
   return render(request, 'op.html', context={'op': result})