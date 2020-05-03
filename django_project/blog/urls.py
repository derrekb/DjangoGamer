from django.urls import path
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,searchposts,RecommenderResultsView)
from .import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [

    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('game_result/', views.RecommenderResultsView.as_view(), name = 'results'),
    path('searchposts', views.searchposts, name='searchposts'),
  

]