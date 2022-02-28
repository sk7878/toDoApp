from django.urls import path
from .views import delete_view, main_view, update_view

urlpatterns = [
    path('', main_view, name='main'),
    path('update/<int:pk>', update_view, name='update'),
    path('delete/<int:pk>', delete_view, name='delete')
]

