from django.urls import path
from . import views

urlpatterns = [
    path('get_all', views.get_all),
    path('get_by_filter', views.get_by_filter),
    path('add', views.add),
    path('delete', views.delete),
    path('select_course', views.select_course),
]
