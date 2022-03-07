"""Breakglass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from django.contrib import admin

# from Breakglass.views import hello
from django.contrib import admin
from django.urls import path
# from Breakglass import views
from Breakglass.views import login, resourcerequest, approverequest, audit, submitRequest, requestResponse



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login),
    url(r'^home/', login),
    url(r'^request/', resourcerequest),
    url(r'^approve/', approverequest),
    url(r'^audit/', audit),
    url(r'^submitRequest/', submitRequest),
    url(r'^requestResponse/', requestResponse)
]
# url(r'^$', 'homefood.views.home', name='home'),


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
