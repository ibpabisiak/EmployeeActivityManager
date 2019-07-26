from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def index(request):
    content = {
        'content' : 'temp',
    }
    return render(request, 'timetracker/index.html', content)
