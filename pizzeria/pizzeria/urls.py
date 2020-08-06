from django.contrib import admin
from django.urls import path, include

"""Se configuró para que incluya todas las URLs de pizzeriapp/urls"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzeriaapp.urls')),
]
