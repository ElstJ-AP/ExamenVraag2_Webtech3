from django.shortcuts import render
import urllib2
import json

def index(request):
	if(request.GET.get('mybtn')):
		voornaam = request.GET.get('voornaam')
		achternaam = request.GET.get('achternaam')
		response = urllib2.urlopen('http://api.icndb.com/jokes/random?firstName=' + voornaam + '&lastName=' + achternaam)
		joke = response.read()
		return render(request, 'chuck_norris/joke.html', {'joke': joke})		
	return render(request, 'chuck_norris/index.html')

	