from django.urls import path
from . import views

urlpatterns = [path('chart/',views.chart,name='chart'),
            path('daily_chart/<str:stock>/<str:date>/<int:pk>',views.daily_chart,name='daily-chart')

                ]
