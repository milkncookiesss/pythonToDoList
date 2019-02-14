from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
  #return HttpResponse("<div id='app'> <h1> hello world </h1> </div>")  #string of html code
  return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
  #return HttpResponse("<div class='login'> <h2> this will be the login page </h2> </div>")
  return render(request, "login.html", {})