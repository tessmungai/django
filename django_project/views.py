import requests
from django.http import response
from django.shortcuts import render

def home (request):
  response = requests.get('https://api.kanye.rest/')
  data = response.json()
  result = data['quote']
  return render(request, 'Templates/index.html',{'result':result})