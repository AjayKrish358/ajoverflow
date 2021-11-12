from django.urls import path
from . import views

app_name='stack_app'
urlpatterns=[path('',views.index,name='index'),
             path('login/',views.login_user,name='login'),
             path('signup/',views.signup,name='signup'),
             path('logout/',views.logout_user,name='logout'),
             path('create/',views.create,name='create'),
             path('my_ques/',views.my_ques,name='my_ques'),
             path('<str:ques>/',views.question,name='question'),
              ]
