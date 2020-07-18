from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/', views.cv_page, name='cv_page'),
    path('cv/newcvpost', views.cvpost_new, name='cvpost_new'),
    path('cv/newcvpostexperience', views.cvpostexperience_new, name='cvpostexperience_new'),
    path('cv/newcvpostskills', views.cvpostskills_new, name='cvpostskills_new'),
]