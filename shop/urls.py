from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views


class OptionalSlashRouter(DefaultRouter):
    """Just to change the default behavior of trailing slashes so
    that urls can now work with or without trailing slashes."""

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'


router = DefaultRouter()
router.register(r'pets', views.PetViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'customers', views.CustomerViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
