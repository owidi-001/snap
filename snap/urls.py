from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',include('accounts.urls')),  
    path('',include('post.urls')),  
    path('', include('django.contrib.auth.urls')),
    # api
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)