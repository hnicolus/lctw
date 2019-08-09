from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,get_object_or_404
from .models import Course, Step
# Create your views here.
def course_list(request):
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)
    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)
    context = {
       'courses':courses,
       'courses':paged_courses,
    }
    return render(request,'courses/course_list.html',context)

def  detail_view(request, course_id):
    course = get_object_or_404(Course,pk=course_id)
    context = {
        'course':course
    }
    return render(request, 'courses/course_detail.html',context)

def step_detail(request,course_pk, step_pk):
    step = get_object_or_404(Step,course_id=course_pk,pk=step_pk)
    context ={
        'step':step
    }
    return render(request, 'courses/step_detail.html',context)

def search(request):
    context = {

    }
    return render(request, 'courses/search.html',context)