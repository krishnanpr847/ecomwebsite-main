"""ecomwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('gold/',views.gold_view,name='gold'),
    path('silver/',views.silver_view,name='silver'),
    path('',views.login_view,name='login'),
    path('index/',views.index_view,name='index'),
    path('order/',views.order_view,name='order'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('filter/',views.filter_view,name='filter'),
    path('tracker/',views.tracker_view,name='tracker'),
    path('search/',views.search_view,name='search'),
    path('email/',views.mail_view,name='email'),
    path('0to100/',views.zerotohundred,name='0to100'),
    path('100to300/',views.hundredtothreehun,name='100to300'),
    #path('<slug:slug>/', views.productview_view, name='post_detail'),
    path('productview/<str:product_name>',views.productview_view,name='productview'),
    path('checkout/',views.checkout_view,name='checkout'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
