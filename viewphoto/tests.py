from django.test import TestCase
from .models import Category, Location, Image


class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test_category = Category(name='Simba')
        self.test_category.save_category()

    # Tear down method
    def tearDown(self):
        Category.objects.all().delete()

    # Testing save method
    def test_save_category(self):
        self.assertEqual(len(Category.objects.all())>0)

    # Testing delete method
    def test_delete_category(self):
        self.test_category.delete_category()
        self.assertEqual(len(Category.objects.all()), 0)


class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.test_location = Location(name='Riverbank')
        self.test_location.save_location()


    # Tear down method
    def tearDown(self):
        Location.objects.all().delete()

    # Testing save method
    
























# from django.test import TestCase
# from .models import Editor,Article,tags
#
# # Create your tests here.
# class EditorTestClass(TestCase):
#
#     #set up method
#     def setUp(self):
#         self.james=Editor(first_name = 'James', last_name = 'Muriuki', email ='james@moringaschool.com')
#
#     def test_instance(self):
#         self.assertTrue(isinstance(self.james,Editor))
#
#     def test_save_method(self):
#         self.james.save_editor()
#         editors = Editor.objects.all()
#         self.assertTrue(len(editors) > 0)
#
#     def test_delete_method(self):
#         self.james.save_editor()
#         self.james.delete_editor()
#         the_tags = Editor.objects.all()
#         self.assertTrue(len(editors) == 0)
#
# class ArticleTestClass(TestCase):
#
#     def setUp(self):
#         self.james=Editor(first_name = 'James', last_name = 'Muriuki', email = 'james@moringaschool.com')
#         self.james.save_editor()
#
#         self.new_tag = tags(name = 'testing')
#         self.new_tag.save()
#
#         self.new_article= Article(title = 'Test Article', post = 'This is a random tgest Post', editor = self.james)
#         self.new_article.save()
#         self.new_article.tags.add(self.new_tag)
#
#     def tearDowm(self):
#         Editor.objects.all().delete()
#         tags.objects.all().delete()
#         Article.objects.all().delete()
#
#     # def test_get_news_today(self):
#     #     today_news = Article.today_news()
#     #     self.assertTrue(len(today_news)>0)
#     #
#     # def test_get_news_by_date(self):
#     #     test_date = '2017-03-17'
#     #     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#     #     news_by_date = Article.days_news(date)
#     #     self.assertTrue(len(news_by_date)==0)
