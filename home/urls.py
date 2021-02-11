from django.urls import path
from home import views

app_name = "home"
urlpatterns = [
    path('', views.home, name="home"),
    path('poll/<str:poll_id>', views.poll.as_view(), name="poll"),
]
