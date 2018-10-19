from django.conf.urls import include, url
from rest_framework import routers

from .api import NoteViewSet
from .api import BodyViewSet
from .api import ChismeViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)
router.register('body', BodyViewSet)
router.register('chisme', BodyViewSet)

urlpatterns = [
    url("^", include(router.urls)),
]
