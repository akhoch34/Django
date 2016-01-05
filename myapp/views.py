from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Options
from django import forms
import re

# Create your views here.


def enterOptions(request):
    return render(request, 'form.html')


def calcNgramCount(request):
    if request.method == 'POST':
        mySentence = request.POST.get('textfield', None)
        #options = Options.objects.get(id=options_id)
        word_amount = len(re.findall(r'\w+', str(mySentence)))
        count = word_amount - (2 - 1)  ##TO do
        #options.summary_text=str(count)
        html = "<H1>The number of n-grams needed is: " + str(count) + " </H1>"
        return HttpResponse(html)
    else:
        return render(request, 'form.html')
