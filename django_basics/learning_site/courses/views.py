from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    out = ', '.join([str(c) for c in courses])
    return HttpResponse(out) 
