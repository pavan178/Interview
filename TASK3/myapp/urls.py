

from django.urls import path

from . import views

#url paths to access the sites on local server
urlpatterns = [

    path('', views.contact),
    path('snippet', views.snippet_detail)

]
