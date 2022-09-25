from . import views 
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('crawler/', views.crawlerPage, name='crawler'),    
    path('blog/', views.blogPage, name='crawler-blog'),   

    path('crawler/add/', views.crawlerAdd, name='crawler-add'),    
    path('crawler/edit/<str:pk>/', views.crawlerEdit, name='crawler-edit'),    
    path('crawler/delete/<str:pk>/', views.crawlerDelete, name='crawler-delete'),    
]