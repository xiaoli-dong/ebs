from django.shortcuts import render
from account.models import Account

# Create your views here.
def home_screen_view(request):
    #print(request.headers)
    context = {}
    # context['some_string'] = "this is some sting that I am going to pass"
    
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "home/home.html", context)