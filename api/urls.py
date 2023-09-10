from django.urls import path

from .views import SlackView


urlpatterns = [
  path('api/', SlackView.as_view())
]