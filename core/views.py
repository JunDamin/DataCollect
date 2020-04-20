from django.shortcuts import render

# Create your views here.


def go_to_home(request):
    return render(request, "home/home.html")
