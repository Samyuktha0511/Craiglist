import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_CRAIGSLIST_URL = 'https://chennai.craigslist.org/search/ccc?query={}'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    response = requests.get('https://chennai.craigslist.org/search/ccc?query=MUSIC&sort=rel')
    data = response.text
    print(data)
    stuff_for_frontend = {
          'search': search,
    }
    return render(request, 'app_one/new_search.html', stuff_for_frontend)
