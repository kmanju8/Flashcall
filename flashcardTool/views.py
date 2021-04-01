from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('You are on the homepage')

def login(request):
    return HttpResponse('Login page')

def profile(request): 
    return HttpResponse('Profile page - view cards and decks')

def addCardsAndDecks(request): 
    return HttpResponse('Make cards and add them to decks on this page')



