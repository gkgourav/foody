from django.urls import path
from . import views
urlpatterns = [
    # path('',views.show,name='show'),
    path("search",views.search,name="search")
  
  ]