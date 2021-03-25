from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns=[
    path('signup/',views.sign_up,name="sign-up"),
    path('login/',LoginView.as_view(),name='login'),
    path('logut/',LogoutView.as_view(),name='logout'),
    path ('view_all_tables/',views.view_all_tables,name = 'view-all-tables')
]