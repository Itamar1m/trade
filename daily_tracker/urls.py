from django.urls import path
from . import views

urlpatterns=[
    path('test/',views.test,name='test'),
    path('remove_row/<int:pk>',views.remove_row,name='remove-row'),
    path('create_table/',views.create_table,name='create-table'),
    path('view_table/<int:pk>',views.view_table,name='view-table'),
    path('remove_row/<int:pk>',views.remove_row,name='remove-row'),
    path('delete_table/<int:pk>',views.delete_table,name='delete-table'),
   
 ]


