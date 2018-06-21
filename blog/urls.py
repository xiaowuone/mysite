#from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r'',views.IndexView.as_view(), name='index'),
	#path(r'post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
	path(r'post/<pk>/', views.PostDetailView.as_view(), name='detail'),
	path(r'archives/<year>/<month>/', views.ArchivesView.as_view(), name='archives'),
	path(r'category/<pk>/', views.CategoryView.as_view(), name='category'),
	
]
