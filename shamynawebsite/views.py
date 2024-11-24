from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def left(request):
    return render(request, 'left.html')
    
def right(request):
    return render(request, 'right.html')