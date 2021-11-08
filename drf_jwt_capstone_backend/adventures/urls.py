from django.urls import path
from adventures import views


urlpatterns = [
    path('all/', views.get_all_adventures),
    # path('', views.user_adventure),
]

