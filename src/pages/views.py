from django.http import HttpRresponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
  return HttpRresponse('<div>Hello World</div>')