from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('making_blog/', views.making_blog, name="making_blog"),
    path('making_post/', views.making_post, name='making_post'),
    path('editing_post/<int:post_id>', views.editing_post, name="editing_post")
]