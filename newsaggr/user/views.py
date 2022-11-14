from django.shortcuts import render,redirect
import requests
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from user.forms import UserRegistrationForm
from user.models import Profile

# Create your views here.
def business(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=business&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=business&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'business.html',context)
def entertainment(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=entertainment&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=entertainment&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'entertainment.html',context)
def sports(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=sports&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=sports&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'sports.html',context)
def health(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=health&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=health&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'health.html',context)
def science(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=science&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=science&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'science.html',context)
def technology(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=technology&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'category=technology&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'technology.html',context)
def index(request):
    if request.user.is_authenticated:
        l = []
        m = []
        data = Profile.objects.get(email=request.user.email)
        l1=['business','sports','general']
        if data.arguments!=None:
            l1 = data.arguments
            l1.append('general')
        for j in l1:
            url = ('https://newsapi.org/v2/top-headlines?'
                'country=in&'
                'category={0}&'
                'from=2022-10-15&'
                'to=2022-11-11&'
                'apiKey=38dce74af0e94a3abc8f386589cbcb9c'.format(j))
            response = requests.get(url)    
            if response.json()['totalResults']==0:
                continue
            headline_title = []
            headline_author = []
            headline_url = []
            for k in range(4):
                headline_title.append(response.json()['articles'][k]['title'])
                headline_author.append(response.json()['articles'][k]['author'])
                headline_url.append(response.json()['articles'][k]['url'])
            topheadline = zip(headline_title, headline_author,headline_url)
            trending_title=[]
            trending_author = []
            trending_description = []
            trending_url=[]
            trending_image=[]
            for p in range(4,8):
                trending_title.append(response.json()['articles'][p]['title'])
                trending_author.append(response.json()['articles'][p]['author'])
                img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
                if response.json()['articles'][p]['urlToImage']!=None:
                    img = response.json()['articles'][p]['urlToImage']
                trending_image.append(img)
                trending_description.append(response.json()['articles'][p]['description'])
                trending_url.append(response.json()['articles'][p][ 'url'])
            trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
            l.append([j,topheadline,trendings])
            
        context = {
                'top':l
            }
        return render(request,'index.html',context)
    else:
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=in&'
            'from=2022-10-15&'
            'to=2022-11-11&'
            'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
        response = requests.get(url)
        
        headline_title = []
        headline_author = []
        headline_url = []
        for i in range(4):
            headline_title.append(response.json()['articles'][i]['title'])
            headline_author.append(response.json()['articles'][i]['author'])
            headline_url.append(response.json()['articles'][i]['url'])
        topheadline = zip(headline_title, headline_author,headline_url)
        
        trending_title=[]
        trending_author = []
        trending_description = []
        trending_url=[]
        trending_image=[]
        for i in range(4,8):
            trending_title.append(response.json()['articles'][i]['title'])
            trending_author.append(response.json()['articles'][i]['author'])
            img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
            if response.json()['articles'][i]['urlToImage']!=None:
                img = response.json()['articles'][i]['urlToImage']
            trending_image.append(img)
            trending_description.append(response.json()['articles'][i]['description'])
            trending_url.append(response.json()['articles'][i]['url'])
            
        trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
        
        topstories_title = []
        topstories_author = []
        topstories_url = []
        topstories_image=[]
        for i in range(8,9):
            topstories_title.append(response.json()['articles'][i]['title'])
            topstories_author.append(response.json()['articles'][i]['author'])
            img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
            if response.json()['articles'][i]['urlToImage']!=None:
                img = response.json()['articles'][i]['urlToImage']
            topstories_image.append(img)
            topstories_url.append(response.json()['articles'][i]['url'])
        topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
        
        topstories_title = []
        topstories_author = []
        topstories_url = []
        topstories_image=[]
        for i in range(9,11):
            topstories_title.append(response.json()['articles'][i]['title'])
            topstories_author.append(response.json()['articles'][i]['author'])
            img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
            if response.json()['articles'][i]['urlToImage']!=None:
                img = response.json()['articles'][i]['urlToImage']
            topstories_image.append(img)
            topstories_url.append(response.json()['articles'][i]['url'])
        topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
        
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=in&'
            'to=2022-11-12&'
            'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
        response2 = requests.get(url)
        
        latest_title = []
        latest_desc = []
        latest_url = []
        latest_image=[]
        for i in range(5):
            latest_title.append(response2.json()['articles'][i]['title'])
            latest_desc.append(response2.json()['articles'][i]['description'])
            img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
            if response2.json()['articles'][i]['urlToImage']!=None:
                img = response2.json()['articles'][i]['urlToImage']
            latest_image.append(img)
            latest_url.append(response2.json()['articles'][i]['url'])
        latest = zip(latest_title, latest_desc,latest_url,latest_image)
        
        
        context = {
                'top': topheadline,
                'trendings':trendings,
                'topstoriestop':topstoriestop,
                'topstoriesbottom':topstoriesbottom,
                'latest':latest
            }
        return render(request,'index.html',context)
def index2(request):
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'from=2022-10-15&'
        'to=2022-11-11&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response = requests.get(url)
    
    headline_title = []
    headline_author = []
    headline_url = []
    for i in range(4):
        headline_title.append(response.json()['articles'][i]['title'])
        headline_author.append(response.json()['articles'][i]['author'])
        headline_url.append(response.json()['articles'][i]['url'])
    topheadline = zip(headline_title, headline_author,headline_url)
    
    trending_title=[]
    trending_author = []
    trending_description = []
    trending_url=[]
    trending_image=[]
    for i in range(4,8):
        trending_title.append(response.json()['articles'][i]['title'])
        trending_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        trending_image.append(img)
        trending_description.append(response.json()['articles'][i]['description'])
        trending_url.append(response.json()['articles'][i]['url'])
        
    trendings = zip(trending_title, trending_author, trending_description,trending_url,trending_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(8,9):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriestop = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    topstories_title = []
    topstories_author = []
    topstories_url = []
    topstories_image=[]
    for i in range(9,11):
        topstories_title.append(response.json()['articles'][i]['title'])
        topstories_author.append(response.json()['articles'][i]['author'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response.json()['articles'][i]['urlToImage']!=None:
            img = response.json()['articles'][i]['urlToImage']
        topstories_image.append(img)
        topstories_url.append(response.json()['articles'][i]['url'])
    topstoriesbottom = zip(topstories_title, topstories_author,topstories_url,topstories_image)
    
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'to=2022-11-12&'
        'apiKey=38dce74af0e94a3abc8f386589cbcb9c')
    response2 = requests.get(url)
    
    latest_title = []
    latest_desc = []
    latest_url = []
    latest_image=[]
    for i in range(5):
        latest_title.append(response2.json()['articles'][i]['title'])
        latest_desc.append(response2.json()['articles'][i]['description'])
        img = 'https://static8.depositphotos.com/1391774/933/i/450/depositphotos_9334068-stock-photo-ripped-newspapers.jpg'
        if response2.json()['articles'][i]['urlToImage']!=None:
            img = response2.json()['articles'][i]['urlToImage']
        latest_image.append(img)
        latest_url.append(response2.json()['articles'][i]['url'])
    latest = zip(latest_title, latest_desc,latest_url,latest_image)
    
    
    context = {
            'top': topheadline,
            'trendings':trendings,
            'topstoriestop':topstoriestop,
            'topstoriesbottom':topstoriesbottom,
            'latest':latest
        }
    return render(request,'index2.html',context)

def preferance(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            l = []
            if 'BUSINESS' in request.POST:
                l.append('business')
            if 'HEALTH' in request.POST:
                l.append('health')
            if 'ENTERTAINMENT' in request.POST:
                l.append('entertainment')
            if 'SCIENCE' in request.POST:
                l.append('science')
            if 'SPORTS' in request.POST:
                l.append('sports')
            if 'TECHNOLOGY' in request.POST:
                l.append('technology')
            current_user=request.user
            profile = Profile.objects.get(email=current_user.email)
            profile.arguments=l
            profile.save()
            return redirect('users:index')
        return render(request,'preferance.html')

def userprofile(request):
    print('userprofile')
    if request.user.is_authenticated:
        name = request.user.username
        email = request.user.email
        password = request.user.password
        if password!="":
            updata = User.objects.get(email=email)
            updata.set_password(password)
            updata.save()
        data = Profile.objects.get(email=email)
        a = data.arguments
    else:
        name = ""
        email = ""
        a = []
    context = {
            'name':name,
            'email':email,
            'a' : a
        }
    return render(request,'userprofile.html',context)

def signin(request):
    if request.method == "POST":
        student = authenticate(username=request.data.get('username'),password=request.data.get('password'))
        if student is not None:
            login(request, student)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        db_obj_email = User.objects.values_list('email')
        if form.is_valid():
            user = form.save()
            if (user.email,)  not in db_obj_email:
                    return render(request,'signup.html',{'note':"User Not Found! Please Register"})
            profile = Profile.objects.create(email=user.email,arguments=[None])
            profile.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('users:login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'signup.html', context)
#    return render(request,'signup.html')

def forgetpass(request):
    global id4
    def sendemail(email2):
        import smtplib, ssl
        import uuid
        id = uuid.uuid4()
        id = str(id)
        id1 = id[2:8]

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "princetestemail123@gmail.com"
        receiver_email = f"{email2}"
        password = "alknkhbiczclwcxw"
        message = f"""\
        Subject: Hi there
        
        Your OTP Forget Password is :: {id1}"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return id1    
    otp = False
    if request.method == 'POST':
        if 'password' not in request.POST:
            email = request.POST.get('email')
            db_obj_email = User.objects.values_list('email')
            if (email,)  not in db_obj_email:
                return render(request,'forgot.html',{'note':"User Not Found! Please Register"})
            else:
                otp = True
                id4=sendemail(email)
                return render(request,'forgot.html',{'otp':otp})        
        else:
            if id4==request.POST.get("otp1"):
                email = request.POST.get('email')
                password = request.POST.get('password')
                updata = User.objects.get(email=email)
                updata.set_password(password)
                updata.save()
                messages.success(request, f'Your account has been created. You can log in now!')
                return render(request,'forgot.html',{'note':"password Change Successfully"})
            else:
                return render(request,'forgot.html',{'note':"OTP IS WRONG OR PASSWORD"})
                
            
    return render(request,'forgot.html',{'otp':otp})

def loggout(request):
    
    logout(request)
    return redirect('users:index')
