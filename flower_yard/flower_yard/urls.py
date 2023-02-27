from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include, path


schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
        description="Документация для приложения product проекта flower-yard",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api_doc/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='api_doc'
    ),
    path('', include('flower.urls'))
]

admin.site.site_title = 'Цветочный дворик'
admin.site.site_header = 'Цветочный дворик'

if settings.DEBUG:
    import debug_toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

