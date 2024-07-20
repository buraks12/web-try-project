from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

course_dictionary = {
    "python": "Python Course Page",
    "java": "Java Course Page",
    "kotlin": "Kotlin Course Page",
    "swift": "Swift Course Page"
}

def index(request):
    return HttpResponse("This is first Django project, first index")
def course(request,item):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
       return HttpResponseNotFound("Error Not Found! Please look for Another Course")
        #raise Http404("")

    #return HttpResponse(course_dictionary.get(item,"Not Found!"))

def course_number_view(request, num1):
    course_list = list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse("course", args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Error Not Found! Please look for Another Course")


    

