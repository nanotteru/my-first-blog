"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#1
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

#2
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #sampleアプリケーションのURLconf読み込み
#     path('sample/', include('sample.urls'))
# ]

#5
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    
    path('admin/', admin.site.urls),
    #sampleアプリケーションのURLconf読み込み
    path('sample/', include('sample.urls')),
    #apiアプリケーションのURLconf読み込み
    path('api/', include('api.urls')),
    #blogアプリケーションのURLconf読み込み
    path('blog/', include('blog.urls')),
    ]
