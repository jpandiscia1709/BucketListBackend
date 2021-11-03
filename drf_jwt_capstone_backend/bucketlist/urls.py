from django.urls import path
from bucketlist import views

urlpatterns = [
    path('', views.BucketList.as_view())
]