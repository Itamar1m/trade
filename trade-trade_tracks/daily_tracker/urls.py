from django.urls import path
from . import views

urlpatterns=[

    path('test/',views.test,name='test'),
    path('remove_row/<int:pk>',views.remove_row,name='remove-row'),
    path('create_table/',views.create_table,name='create-table'),
    path('view_table/<int:pk>',views.view_table,name='view-table'),
    path('remove_row/<int:pk>/<int:date>/<int:symbol>',views.remove_row,name='remove-row'),
    path('delete_table/<int:pk>',views.delete_table,name='delete-table'),
    path('add_column/<int:pk>/<str:name>',views.add_column,name='add-column'),
    path('remove_column/<int:pk>/<str:name>',views.remove_column,name='remove-column'),
    path('table_filter/',views.table_filter,name='table-filter'),
    path('export_csv/<int:pk>',views.export_csv,name='export-csv')
  
 ]


