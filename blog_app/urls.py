# All URL hits by the client will reach out to 'mysite.urls' in which some of the
# URLs will redirect to 'blog_app.urls' which is made by me to keep the 
# 'mysite.urls' file clean

from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('path/<int:pk>/', views.post_detail, name='post_detail'),
] 
