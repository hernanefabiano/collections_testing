from __future__ import absolute_import, division, print_function, unicode_literals

from rest_framework.routers import DefaultRouter

from .views import CarModelListViewSet

router = DefaultRouter()

router.register(r"listings", CarModelListViewSet, base_name="listings")

urlpatterns = router.urls

