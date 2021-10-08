from django.urls import path  
from app import views  
urlpatterns = [  
    path('create/', views.create, name='create'),  
    path('list/',views.list, name='list'),
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.delete, name='delete'),  
]  