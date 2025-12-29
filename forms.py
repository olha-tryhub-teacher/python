from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("tasks.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
