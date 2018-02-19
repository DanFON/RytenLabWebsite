"""braineacv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


from contact import views as contact_views
from contact_us import views as contact_us_views


# from resources import views as resources_views

#settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', contact_views.home, name='home'),
    url(r'^about/$', contact_views.about, name='about'),
    url(r'^contact/$', contact_views.userProfile, name='contact'),
    url(r'^contact_us/$', contact_us_views.contact_us, name='contact_us'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^resources/$',contact_views.resources, name='resources'),
    url(r'^staff/$',contact_views.staff, name='staff'),
    url(r'^daniel_onah/$',contact_views.daniel_onah, name='daniel_onah'),
    url(r'^daniel_biography/$',contact_views.daniel_biography, name='daniel_biography'),
    url(r'^daniel_publications/$',contact_views.daniel_publications, name='daniel_publications'),
    url(r'^regina_reynolds/$',contact_views.regina_reynolds, name='regina_reynolds'),
    url(r'^david_zhang/$',contact_views.david_zhang, name='david_zhang'),
     url(r'^juan_botia/$',contact_views.juan_botia, name='juan_botia'),
    url(r'^news/$',contact_views.news, name='news'),
    url(r'^resources2/$',contact_views.resources2, name='resources2'),
    url(r'^careers/$',contact_views.careers, name='careers'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)