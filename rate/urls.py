from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('rate/',views.rate,name='rate'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('edit/',views.edit,name='edit'),
]
