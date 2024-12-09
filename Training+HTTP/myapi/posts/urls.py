from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDelete


urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),  
    path('posts/<int:pk>/', PostRetrieveUpdateDelete.as_view(), name='post-detail'),
]