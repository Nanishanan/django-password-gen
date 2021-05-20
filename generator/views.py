from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def book(request):

    janebooks = list('northangerabbey')

    if request.GET.get('Numbers'):
        janebooks.extend(list('0123456789'))
    if request.GET.get('UpperCase'): 
        janebooks.extend(list('NORTHANGERABBEY'))
    if request.GET.get('Specials'): 
        janebooks.extend(list('!@#$%^&*'))

    length = int(request.GET.get('book_length'))
    bookname = ''

    for i in range(length):
        bookname += random.choice(janebooks)

    return render(request, 'generator/book.html', { 'bookname': bookname })

def about(request):
    return render(request, 'generator/about.html')