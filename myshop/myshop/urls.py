"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
from shop import views as shop_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
     path('register/', account_views.register, name='register'),
        path('profile/', account_views.profile, name='profile'),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
        path('password-reset/done/', auth_views. PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
        path('password-reset/', auth_views. PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
        path('password-reset-confirm/<uidb64>/<token>/', auth_views. PasswordResetConfirmView.as_view(template_name='registration/password_confirm.html'), name='password_reset_confirm'),
        path('about/', shop_views.about,name='about'),
        path('returns/', shop_views.returns, name='returns'),
        path('contact/', shop_views.contact, name='contact'),
        path('privacy-policy/', shop_views.privacy_policy, name='privacy_policy'),
        path('payment-options/', shop_views.payment_options, name='payment_options'),
        path('cookie/', shop_views.cookie, name='cookie'),
        path('password-reset-complete/', auth_views. PasswordResetCompleteView.as_view(template_name='registration/password_complete.html'), name='password_reset_complete'),
    path('', include('shop.urls', namespace='shop')),
    path(
            'admin/password_reset/',
            auth_views.PasswordResetView.as_view(),
            name='admin_password_reset',
        ),
        path(
            'admin/password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(),
            name='password_reset_done',
        ),
        path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm',
        ),
        path(
            'reset/done/',
            auth_views.PasswordResetCompleteView.as_view(),
            name='password_reset_complete',
        ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)