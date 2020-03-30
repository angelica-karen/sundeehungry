"""sundeehungry URL Configuration

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

    path('weblog/', include('blog.urls')),

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    url(r'^restaurant/sign-in/$', auth_views.login,
        {'template_name':'restaurant/sign_in.html'},
        name = 'restaurant-sign-in'),

    path('restaurant/sign-in/$', auth_views.login,
        {'template_name':'restaurant/sign_in.html'},
        name = 'restaurant-sign-in'),

    url(r'^restaurant/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'restaurant-sign-out'),

    path('restaurant/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'restaurant-sign-out'),

    path('restaurant/sign-out/', LogoutView.as_view(template_name='home.html'), name='restaurant-sign-out'),
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from sundeehungryapp import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Restaurant
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('restaurant/sign-in/', LoginView.as_view(template_name='restaurant/sign_in.html'),
    #    name='restaurant-sign-in'),
    url(r'^restaurant/sign-in/$', auth_views.login,
        {'template_name':'restaurant/sign_in.html'},
        name = 'restaurant-sign-in'),

    #path('restaurant/sign-out/', LogoutView.as_view(template_name='restaurant/home.html'),
        #name='restaurant-sign-out'),
    url(r'^restaurant/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'restaurant-sign-out'),

    path('restaurant/sign-up', views.restaurant_sign_up, name = 'restaurant-sign-up'),
    path('restaurant/', views.restaurant_home, name = 'restaurant-home'),

    #Sign In/ Sign Up/ Sign Out
    #path('api/social/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-toek (sign in/sign up)
    # /revoke-token (sign out)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
