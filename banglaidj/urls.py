"""banglaidj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from blog_post import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('post-list/',views.all_posts,name='all-posts'),
    path('single-post',views.single_post,name='single-post'),
    path('single-post/<post_id>/', views.single_post, name='single-post'),
    path(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post, name='single-post'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    #path('image-to-text/',views.imageToText,name='image-to-text'),
    path('', include('blog_post.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)