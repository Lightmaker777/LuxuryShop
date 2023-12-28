# LuxuryMarket/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls')),
    path('chatapp/', include('chatapp.urls')), 
    path('terms-and-conditions/', user_views.TermsAndConditionsView.as_view(), name='terms_and_conditions'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
   
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)