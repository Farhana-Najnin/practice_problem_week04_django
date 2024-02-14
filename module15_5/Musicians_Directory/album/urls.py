from django.urls import path
from . import views 
urlpatterns = [
    path('add/', views.addalbum, name='addalbum'),
    path('edit/<int:id>', views.editalbum, name='editalbum'),
    path('delete/<int:id>', views.deletealbum, name='deletealbum'),
]