from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello ")

class IndexTemplateView(TemplateView):
    template_name = "index.html"