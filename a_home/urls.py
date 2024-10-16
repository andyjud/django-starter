from django.urls import path
from a_home.views import home_view, count_view

urlpatterns = [
    path('', home_view, name="home"),
    path('count/', count_view, name="count"),
]