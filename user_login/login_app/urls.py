from msilib.schema import _Validation_records
from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index,name='index'),
    path('signup',views.Sign_up,name='sign_up'),
    path('login/',views.User_login,name='login'),
]