from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from bs4 import BeautifulSoup as soup
import requests
import re
from .models import MovieData
# Create your views here.
def movies_home(request):
    obj = MovieData.objects.all()
    return render(request, 'movierecommends/homepage.html', {'movie_data': obj})

def save_date_to_db(request):
    url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    response = requests.get(url).content
    res = soup(response, 'html.parser')
    table_content = res.find('tbody', class_='lister-list')
    for tb in table_content.find_all('tr'):
        imdb_rank = re.sub(r"[.]", '', tb.find(
            class_="titleColumn").text.strip().split('\n')[0].strip())

        image_url = tb.find(class_='titleColumn').find('a')['href']
        poster, stream = getRawData(image_url)
        movie_title = tb.find(class_="titleColumn").text.strip().split('\n')[1].strip()
        release_year = re.sub(r"[()]", "", tb.find(
            class_="titleColumn").text.strip().split('\n')[2])
        obj = MovieData.objects.create(
            rank = imdb_rank,
            movie_name=movie_title,
            poster = poster,
            streamOn = stream,
            year = release_year
        )
        obj.save()
    return HttpResponse("Saved")

def getRawData(image_url):
    url = 'https://www.imdb.com/'+str(image_url)
    response = requests.get(url).content
    res = soup(response, 'html.parser')
    poster = res.find(class_='poster').find('img')['src']
    try:
        stream = res.find(class_='buybox__cta').text.strip()
    except:
        stream = "None"
    return poster, stream
