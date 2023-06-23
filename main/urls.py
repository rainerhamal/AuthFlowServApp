from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'), #get request to retrieve and display user information 
    path('sign_up', views.sign_up, name='sign_up'), #get and post request for insert/sign up operation
    path('<int:id>/', views.user_update, name='user_update'), #get and post request for update operation
    # path('login', views.login, name='login')
]
