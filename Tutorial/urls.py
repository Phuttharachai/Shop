from django.contrib import admin
from django.urls import path, include
from shop.urls import router
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # drf browsable api docs
    path('api/', get_swagger_view(title='API Docs.')),
    path('', include(router.urls))
]

