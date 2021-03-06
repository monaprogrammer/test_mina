from django.urls import path
from . import views

app_name = 'posts'
urlpatterns =[
        path('', views.all_posts, name='all_posts'),
        path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name= 'post_detail'),
        path('add_post/<int:user_id>/', views.add_post, name = 'add_post'),

]