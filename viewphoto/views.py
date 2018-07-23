from django.shortcuts import render, redirect
from .models import Image, Category, Location
# from django.http import HttpResponse,Http404
# from .models import Article
# import datetime as dt

def home(request):
    categories = Category.objects.all()
    locations = Location.objects.all()


    if request.GET.get('location'):
        pic = Image.filter_by_location(request.GET.get('location'))

    elif request.GET.get('category'):
        pic = Image.filter_by_category(request.GET.get('category'))

    elif request.GET.get('query'):
        pic = Image.search_image(request.GET.get('query'))

    else:
        pic = Image.objects.all()

    return render(request, 'index.html', {'categories': categories, 'locations': locations, 'pic': pic})

def image_link(request, id):
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    try:
        pic = Image.get_image_by_id(id)
    except Image.DoesNotExist:
        raise Http404()

    return render(request, 'image.html', {'categories': categories, 'locations': locations, 'pic': pic})
# Create your views here.


# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')
#
# # def news_of_day(request):
# #     date = dt.date.today()
# #
# #     #Function to convert date object to find exact day
# #     day = convert_dates(date)
# #     html = f'''
# #         <html>
# #             <body>
# #                 <h1>News for {day} {date.day}-{date.month}-{date.year} </h1>
# #
# #             </body>
# #         </html>
# #         '''
# #     return HttpResponse(html)
#
# def news_today(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news})
#
# # def convert_dates(dates):
# #     #Function that gets the weekday number for the date.
# #     day_number = dt.date.weekday(dates)
# #
# #     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
# #
# #     #returning the actual dy of the week
# #     day = days[day_number]
# #     return day
#
# # def past_days_news(request,past_date):
# #     #Converts data from the string Url
# #     date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#
# def past_days_news(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
#     except valueError:
#         # Raise 404 error when valueError is thrown
#         raise Http404()
#         assert False
#
#     if date == dt.date.today():
#         return redirect(news_today)
#
#     news = Article.days_news(date)
#
#     return render(request, 'all-news/past-news.html', {"date": date,"news": news})
#
#
#     # day = convert_dates(date)
#     # html = f'''
#     #     <html>
#     #         <body>
#     #             <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
#     #         </body>
#     #     </html>
#     #         '''
#     # return HttpResponse(html)
#
# #Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')
#
# def search_results(request):
#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_titles(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'all-news/search.html',{"message":message,"articles":searched_articles})
#
#     else:
#         message = "You haven't searchred for any term"
#         return render(request, 'all-news/search.html',{"message":message})
#
# def article(request,article_id):
#     try:
#         article = Article.objects.get(id = article_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-news/article.html", {"article":article})
