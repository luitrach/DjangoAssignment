
from django.urls import path
from .import views

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('view/<int:pk>',views.book_view,name='book_view'),
    path('edit/<int:pk>',views.book_update,name='book_edit'),
    path('delete/<int:pk>',views.book_delete,name='book_delete'),
 
]