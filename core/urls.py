from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('blog_bridger_drf.urls')),
    path('api/users/', include("users.urls"),)
]
