"""Djangoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

app_name="Djangoapi"

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include('Djangoapi.apps.articles.urls', namespace='articles')),
    url(r'^api/', include('Djangoapi.apps.authentication.urls', namespace='authentication')),
    url(r'^api/', include('Djangoapi.apps.profiles.urls', namespace='profiles')),
<<<<<<< HEAD
] 

=======
]
>>>>>>> e83f9a70c4d95f9b0cf00cfb93f1eb5fd8737b4e
