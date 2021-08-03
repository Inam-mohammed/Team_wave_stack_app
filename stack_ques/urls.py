from django.urls import path, include
from .views import index, QuestionAPI, display
from rest_framework import routers


router = routers.DefaultRouter()
router.register("questions", QuestionAPI)


urlpatterns = [
    path('', index, name='index'),
    path('',include(router.urls)),
    path('display', display, name='disp')
]