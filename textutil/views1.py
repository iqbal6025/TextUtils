from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'home.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    check=request.POST.get('check','off')
    capfirst=request.POST.get('capfirst','off')
    spacefree=request.POST.get('spacefree','off')
    count=request.POST.get('count','off')
    newlineremove=request.POST.get('newlineremove','off')
    analyzed = djtext
    purpose=[]
    count1=0
    if check=='on':
        xya = []
        punctuations = '''!()-[];:{}.,;:_*$%^&'''
        for i in djtext:
            xya = [i for i in djtext if i not in punctuations]
        analyzed = ''.join(map(str, xya))
        purpose.append('Remove Punctuations')
    if capfirst=='on':
        analyzed=''.join(map(str,[i.upper() for i in analyzed]))
        purpose.append('Upper Case')
    if spacefree=='on':
        analyzed=' '.join(map(str,[val for val in analyzed.split()]))
        purpose.append('Space Free')
    if newlineremove=='on':
        analyzed=' '.join(map(str,[i for i in analyzed.split() if i not in "\n"]))
        purpose.append('New Line Remove')
    if count=='on':
        count1=len([val for val in analyzed if val!=" "])
        purpose.append('count')
    elif check=='off' and count=='off' and newlineremove=='off' and spacefree=='off' and capfirst=='off':
        return HttpResponse('Error')
    purpose=','.join(map(str,purpose))
    param = {'purpose':purpose, 'analyzed_text': analyzed,'count':count1}
    return render(request, 'analyze.html', param)
