from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def programming(request):

    l = news("programming")
    s = wiki("Computer programming")
    redditlist = reddit("ProgrammerHumor")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        't6' : redditlist[5][0],
        'redurl6' : redditlist[5][1],
        'Main_name' : "Programming",
    }

    return render(request, 'base.html', context)

def fortnite(request):
    l = news("fortnite")
    s = wiki("Fortnite")
    redditlist = reddit("FortniteMemes")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        'Main_name' : "Fortnite"
    }

    return render(request, 'base.html', context)
    
def physics(request):
    l = news("Physics")
    s = wiki("Physics")
    redditlist = reddit("physicsmemes")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        'Main_name' : "Physics"
    }

    return render(request, 'base.html', context)

def haryypotter(request):
    l = news("Harry Potter")
    s = wiki("Harry_Potter")
    redditlist = reddit("HarryPotterMemes")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        'Main_name' : "Harry Potter"
    }

    return render(request, 'base.html', context)

def cat(request):
    l = news("Cat")
    s = wiki("Cat")
    redditlist = reddit("Catmemes")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        'Main_name' : "Cat",
        # 'query' : a
    }

    return render(request, 'base.html', context)

def wiki(subject):
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
            'action': 'query',
            'format': 'json',
            'titles': subject,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
        }

    response = requests.get(url, params=params)
    data = response.json()

    if list(data['query']['pages'].keys())[0] == '-1':
        return 'Page not found'
    else:
        page = next(iter(data['query']['pages'].values()))
        return page['extract']

def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    try:
        if r.headers["content-type"] in image_formats:
            return True
        return False
    except KeyError:
        return False

def crypto(request):
    l = news("Cryptocurrency")
    s = wiki("Cryptocurrency")
    redditlist = reddit("cryptocurrencymemes")

    context = {
        'title1' : l[0][0],
        'author1' : l[0][1],
        'desc1' : l[0][2],
        'url1' : l[0][3],
        'title2' : l[1][0],
        'author2' : l[1][1],
        'desc2' : l[1][2],
        'url2' : l[1][3],
        'title3' : l[2][0],
        'author3' : l[2][1],
        'desc3' : l[2][2],
        'url3' : l[2][3],
        'wiki_info' : s,
        't1' : redditlist[0][0],
        'redurl1' : redditlist[0][1],
        't2' : redditlist[1][0],
        'redurl2' : redditlist[1][1],
        't3' : redditlist[2][0],
        'redurl3' : redditlist[2][1],
        't4' : redditlist[3][0],
        'redurl4' : redditlist[3][1],
        't5' : redditlist[4][0],
        'redurl5' : redditlist[4][1],
        'Main_name' : "Crypto Currency"
    }

    return render(request, 'base.html', context)

def reddit(string):
    auth = requests.auth.HTTPBasicAuth('tn-A6UAOUcTqwGW9d-XErg', 'd-FjQO7mQ2rKCZF23A5RWgnE6Doegg')
    data = {'grant_type': 'password',
            'username': 'abhay21508',
            'password': 'apiproject'}
    headers = {'User-Agent': 'Kiwipedia_reddit_info'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    res = requests.get(f"https://oauth.reddit.com/r/{string}/hot",  
                    headers=headers, params = {'limit' : '15'})
    lst = []
    for post in res.json()['data']['children']:
        title = post['data']['title']
        url = post['data']['url']
        if is_url_image(url):
            lst.append([title, url])
        if len(lst) == 6:
            break
    
    return lst

def news(string):
    
    l = [[] for i in range(3)]
    key = '0ff59476433b4f938005527d91082cc3'
    search_query = string
    params = {
        'apiKey' : key,
        'sortBy' : 'relevancy',
        'language' : 'en',
        'searchIn' : 'title,description',
        'q' : search_query,
    } 
    res = requests.get('https://newsapi.org/v2/everything', params=params)
    print(res.status_code)
    i = 0
    for i in range(3):
        article = res.json()['articles'][i]
        l[i].append(article['title'])
        l[i].append(article['author'])
        l[i].append(article['description'])
        l[i].append(article['url'])
        i += 1

    return l



