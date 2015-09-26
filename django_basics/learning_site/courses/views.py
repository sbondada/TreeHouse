from django.shortcuts import get_object_or_404, render

from .models import Course,Step

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    steps = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'steps': steps})
