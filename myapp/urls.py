
from django.urls import path,include
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',index,name='index'),
    
    path('accounts',accounts,name="accounts"),
    path('about',about,name='about'),
    path('menu',menu,name='menu'),
    path('reservation',reservation,name='reservation'),
    path('service',service,name='service'), 
    path('testimonial',testimonial,name='testimonial'),
    path('login_reg',login_reg,name="login_reg"),

    path("userReg",userReg,name="userReg"),
    path("userLogin",userLogin,name="userLogin"),
    path("userlogout",userlogout, name="userlogout")
]