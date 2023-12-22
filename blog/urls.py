from django.urls import path
from . import views



app_name='blog'

urlpatterns = [
    path('blog/',views.blog,name='article-list'),
    path('blog/<int:id>/',views.blog_detail,name='blog-detail'),
    path('example/',views.example),
    path('add-article/',views.add_article,name="add-article"),
    path('edit-article/<int:id>/',views.edit_article,name="edit-article"),
    path('delete-article/<int:pk>/',views.delete_article,name="delete-article"),
]
