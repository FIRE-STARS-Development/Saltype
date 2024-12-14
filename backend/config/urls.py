from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/django/authentication/", include("apps.authentication.urls")),
    path("api/django/mistype/", include("apps.mistype.urls")),
    path("api/django/score/", include("apps.score.urls")),
    path("api/django/ranking/", include("apps.ranking.urls")),
    path("api/django/request/", include("apps.contact.urls")),
    path("api/django/user/", include("apps.user.urls")),
]
