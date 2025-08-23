"""
URL configuration for Capedu_dgango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,re_path,include
from hello import views
product_patterns = [path('',views.products),path("new",views.products_new),path("top",views.products_top)]
stat_patterns = [path('',views.stat),path("stat_new",views.stat_new),path("stat_top",views.stat_top)]
#stat_patterns1 = [path('',views.stat1),path("stat_new1",views.stat_new1),path("stat_top1",views.stat_top1)]

urlpatterns = [
    path('', views.index,name="home",kwargs={"id":"18497260"}),
    path("about",views.about,kwargs={"name":"Tom","age":"38"}),
    path("contact",views.contact,name='contact'),
    path("about_us",views.about_us),
    path("users/<str:name>",views.users),
    path("info",views.request_info),
    path("custom",views.custom_answer),
    path("customm",views.custom_answer1),
    path("products/<int:id>/",include(product_patterns)),
    path("user/",views.user),
    path("stats/<int:id>/",include(stat_patterns)),
    path("stat1/",views.stat1),
    path("stat1_top/",views.stat_top1),
    path("stat1_new/",views.stat_new1),
    path("contact_us",views.redirect_func),
    path("j_responce",views.json_responce),
    path("cookies_set",views.set_cookie_view),
    path("cookies_get",views.get_cookie_view),


    #path("stats1/",include(stat_patterns1))
]
handler_404 = "hello.views.error_404"
#path(route,view,kwargs,name)