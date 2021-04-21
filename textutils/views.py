from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    # params = {'purpose': 'No text entered/utils selected', 'analysed_text': 'Please enter and utils text before submitting'}

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext=analysed

    if fullcaps=="on":
        analysed=""
        for char in djtext:
            analysed=analysed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analysed_text': analysed}
        djtext=analysed

    if newlineremover=="on":
        analysed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analysed=analysed+char
        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext=analysed

    if (extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Change To Uppercase', 'analysed_text': analysed}
        djtext=analysed


    return render(request,'analyse.html', params )