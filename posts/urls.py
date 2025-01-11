from django.urls import path
from . import views
'''
you are able to use <a href="{% url 'posts:list' %}">
with app_name and name variables
'''

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
]
