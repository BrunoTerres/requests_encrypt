from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('timer/', include('timer.urls')),
    path('admin', admin.site.urls),
]