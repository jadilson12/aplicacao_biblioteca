
from django.contrib import admin
from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.home, name='core_home'),
    path('admin/', admin.site.urls),
]