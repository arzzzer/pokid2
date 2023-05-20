from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def pokid_view(request):
    measures = Measure.objects.all()
    children = Child.objects.all()
    context = {
        'measures': measures,
        'children': children,
    }
    return render(request, 'index.html', context)