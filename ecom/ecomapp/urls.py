from django.urls import path
from ecomapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('order',views.order,name="order"),
    path('checkout',views.checkout,name="checkout"),



]
