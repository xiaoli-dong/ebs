from django.shortcuts import render
from account.models import Account
from project.models import Project
from project.views import get_project_queryset
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
PROJECTS_PER_PAGE = 1

# Create your views here.
def home_screen_view(request):
    #print(request.headers)
    context = {}
    # context['some_string'] = "this is some sting that I am going to pass"
    
    # accounts = Account.objects.all()
    # context['accounts'] = accounts

    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, "home/home.html", context)

