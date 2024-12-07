from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('AdminHomePage/', views.AdminHomePage, name='AdminHomePage'),
    path('logout/', views.AdminLogout, name='AdminLogout'),
    path('register/', views.register, name='register'),
    path('live_stream_list/', views.live_stream_list, name='live_stream_list'),
    path('live_stream_detail/<int:stream_id>/', views.live_stream_detail, name='live_stream_detail'),
]
