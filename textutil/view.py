# I have create this file - Iqbal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''<h2>Hello Iqbal</h2><a href="https://google.com">Google</a>''')
def chat(request):
    f=open('C:/Users/Hi/Desktop/one.txt.txt','r')
    ne=f.read()
    f.close()
    return HttpResponse(ne,content_type='text/plain')
