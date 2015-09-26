from django.shortcuts import render

def Hello_world(request):
    return render(request,'../templates/home.html')
