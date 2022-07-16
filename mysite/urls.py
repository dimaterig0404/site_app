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
# from urllib.parse import parse_qs
from django.contrib import admin
from django.urls import path,include

from mysite.apps import myapp2
from . import views

urlpatterns = [
    path('',include('myapp2.urls'), name='index'),# path('',include('myapp.urls'), name='index'),
    path('merop/',include('myapp2.urls'), name='seans'),
    path('login/', include('myapp2.urls'), name='login'),
    path('reg/', include('myapp2.urls'), name='registration'),
    path('logout/', include('myapp2.urls'), name='logout'),
    
    
    # path('prof',include('myapp2.urls'), name='prof'),
    path('prof/my_ine',include('myapp2.urls'), name='prof_detail_my'),
    path('prof/my_ine/edit',include('myapp2.urls'), name='prof_detail_my_edit'),
    path('prof/my_ine/edit/save',include('myapp2.urls'), name='prof_detail_my_edit_save'),
    path('prof/<int:prof_id>',include('myapp2.urls'), name='prof_detail2'),
    path('buy/<str:seans_id>',include('myapp2.urls'), name='buy_valet2' ),
    path('like/<str:seans_id>',include('myapp2.urls'), name='buy_valet2' ),
    path('eror404/',include('myapp2.urls'), name='eror404'),
    # path('buy/<str:seans_id>',views.buy_valet, name='buy_valet' ),
    
    
    # path('reg/Qr',include('myapp.urls'), name='registration_Qr' ),
    # path('reg/info',include('myapp.urls'), name='registration_info'),
    # path('reg/valid',include('myapp.urls'), name='registration_finish'),
    # path('reg/',views.reg, name='registration'),
    
    path('adminiStrator/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
        
    
]

