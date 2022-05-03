"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
# modified to import "include" as well
from django.urls import path, include
from register import views as v
from django.conf.urls.i18n import i18n_patterns
urlpatterns = []
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    # default path the user is brought to
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    # path('testlang/', include('testlang.urls', namespace='testlang')),
]

