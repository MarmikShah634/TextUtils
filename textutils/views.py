from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == 'on':
        for c in djtext:
            if c not in punctuations:
                analyzed += c
        params = {'purpose' : 'Removed punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        if fullcaps == 'on':
            for c in djtext:
                analyzed += c.upper()
        params = {'purpose' : 'Changed to upper case', 'analyzed_text' : analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for c in djtext:
            if c != "\n" and c != '\r':
                analyzed += c
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)