from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('about', views.about, name="about"),
    path('returns', views.returns, name='returns'),
    path('contact', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie/', views.cookie, name='cookie'),
    path('payment-options/', views.payment_options, name='payment_options'),
]