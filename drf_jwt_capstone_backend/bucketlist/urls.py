from django.urls import path
from bucketlist import views


urlpatterns = [
    path('all/', views.get_all_bucketlists),
    path('', views.user_bucketlist),
]