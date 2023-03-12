from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'a':500,'b':1500,'c':300}
    return render(request,'looping.html',d)