from django.urls import path
from .views import page

urlpatterns = [
    path('<slug:page_slug>/', page, name='pages'),
]