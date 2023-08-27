from django.urls import path
from . import views
from home.views import NotFoundView

app_name ='home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]

handler404 = NotFoundView.as_view()