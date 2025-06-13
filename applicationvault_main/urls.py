from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/v1/core/', include('core.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),  # login/logout
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),  # registration
 

]
