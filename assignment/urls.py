from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    # Other URL patterns of your project
    path('mainapp/', include('mainapp.urls')),
]

# siglbjytwhomiqhk