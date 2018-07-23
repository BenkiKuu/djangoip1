from django.db import models
import datetime as dt



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='pic/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ManyToManyField(Category, blank=True)
    location = models.ManyToManyField(Location, blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pics = cls.objects.get(id=id)
        return pics

    @classmethod
    def filter_by_category(cls, category):
        pics = cls.objects.filter(category=category)
        return pics

    @classmethod
    def filter_by_location(cls, location):
        pics = cls.objects.filter(location=location)
        return pics

    @classmethod
    def search_image(cls, query):
        pics = cls.objects.filter(name=query)
        return pics






# class Editor(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)
#     import datetime as dt
    # try:
    #     editor = Editor.objects.get(email = 'example@gmai.com')
    #     print('Editor found')
    # except DoesNotExist:
    #     print('Editor was not found')

#     def __str__(self):
#         return self.name
#
#     def save_image(self):
#         self.save()
#
#
#     # class Meta:
#     #     ordering = ['first_name']
#
# class tags(models.Model):
#     name = models.CharField(max_length =30)
#
#     def __str__(self):
#         return self.name
#
# class Article(models.Model):
#     title = models.CharField(max_length =60)
#     post = models.TextField()
#     editor = models.ForeignKey(Editor)
#     tags = models.ManyToManyField(tags)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     article_image = models.ImageField(upload_to = 'articles/')
#
#
#     @classmethod
#     def todays_news(cls):
#         today = dt.date.today()
#         news = cls.objects.filter(pub_date__date = today)
#         return news
#
#     @classmethod
#     def days_news(cls,date):
#         news = cls.objects.filter(pub_date__date = date)
#         return news
#
#     @classmethod
#     def search_by_titles(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news
