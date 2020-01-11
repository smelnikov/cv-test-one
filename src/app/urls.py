from django.urls import include, path
from rest_framework import routers

from . import views, viewsets


router = routers.DefaultRouter()
router.register(r'app', viewsets.ApplicationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', views.TestView.as_view()),
]
