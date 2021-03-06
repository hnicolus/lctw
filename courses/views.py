from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,get_object_or_404
from .models import Course, Step, Category,Tutorial
import datetime
# Create your views here.

def category_list(request, category):
    courses = Course.objects.order_by('-pub_date').filter(category = category_id )
    paginator = Paginator(courses, 9)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)
    category = Category.objects.all()
    context = {
       'courses':courses,
       'courses':paged_courses,
       'category':category
    }
    return render(request,'courses/course_list.html',context)


def course_list(request):
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)
    paginator = Paginator(courses, 9)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)
    category = Category.objects.all()
    context = {
       'courses':courses,
       'courses':paged_courses,
       'category':category
    }
    return render(request,'courses/course_list.html',context)

def  detail_view(request, course_id):
    course = get_object_or_404(Course,pk=course_id)
    steps = Step.objects.all().filter(course = course)
    context = {
        'course':course,
        'steps': steps
    }
    return render(request, 'courses/course_detail.html',context)

def step_detail(request,course_pk, step_pk):
    step = get_object_or_404(Step,Course_id=course_pk,pk=step_pk)
    context ={
        'step':step
    }
    return render(request, 'courses/step_detail.html',context)

def tutorial_detail(request,course_pk, step_pk,tut_pk):
    course = Course.objects.get(id= course_pk)
    step = Step.objects.get(id=step_pk)
    tutorial = get_object_or_404(Tutorial,id= tut_pk)
    context ={
        'tutorial':tutorial,
        'course':course,
        'step':step
    }
    return render(request, 'courses/tutorial_detail.html',context)

def search(request):
    context = {

    }
    return render(request, 'courses/search.html',context)