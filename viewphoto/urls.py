from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.home,name = 'home'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # url(r'^search/', views.search_results, name='search_results'),
    url(r'^pic/(\d+)',views.image_link,name ='image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
