"""
URL configuration for ActualProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from Sign_Up_Pages.views import HomePage,sign_up
from Sign_In_Pages.views import signIn
from FeedPages.views import Feed,Fetch,id ,create_feed
from myapp.views import Request,Sign_out,Contact_us

urlpatterns = [
    path('', HomePage),
    path ('sign_up/',sign_up),
    path('sign_in/', signIn, name='sign_in'),
    # path('feedtable/', combinedData),
    path('feedtable/', Fetch),
    path('feed/request/', Request, name='requests'),
    # path('fetch/', Fetch),
    # path('feedtable1/',requestTable),
    path('feed/',Feed),
    # path('okay/',my_view),
    path('create_feed/', create_feed),
    path('id',id),
    path('feed/sign_out',Sign_out, name='sign_out'),
    path('feed/about_us',Contact_us,name='about_us'),
    path('admin/', admin.site.urls)


]
