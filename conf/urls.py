# import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import AdvertViewSet

router = DefaultRouter()
router.register(r'adverts', AdvertViewSet)

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('page/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    # API
    path('api/v1/', include(router.urls)),
<<<<<<< HEAD

=======
>>>>>>> origin/14_6_auth_permission
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # accounts
    path('accounts/', include('allauth.urls')),
    # main
    path('chat/', include('chatbot.urls')),
    path('', include('main.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
]
