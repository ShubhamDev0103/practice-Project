from re import template
from xml.dom.minidom import DocumentType
from django.urls import path, re_path

from doob_pro.settings import MEDIA_ROOT, STATIC_ROOT
# from django.conf.urls import url
from . import views
from .models import *
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about/(?P[0-9]+)/\\Z', views.about, name = 'about'), 
    path('Register/(?P[0-9]+)/\\Z', views.Cus_Register.as_view(), name= 'Register'),
    path('account/login/(?P[0-9]+)/\\Z', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = Login), name='Login'),
    path('Profile/', views.Cus_Profile.as_view(), name='Profile'),
    path('account/login/(?P[0-9]+)/\\Z', auth_views.LogoutView.as_view(template_name = 'index.html'), name='logout'),

    path('AdminForgetPassword/(?P[0-9]+)/\\Z', auth_views.PasswordChangeView.as_view(template_name = 'Admin_PasswordChange.html', form_class = Admin_PasswordChange, success_url = '/passwordchangedone/'), name='AdminForgetPassword'),
    path('passwordchangedone/(?P[0-9]+)/\\Z', auth_views.PasswordChangeDoneView.as_view(template_name = 'AdminPassChageDone.html'), name='passwordchangedone'),

    path('password-reset/(?P[0-9]+)/\\Z', auth_views.PasswordResetView.as_view(template_name = 'AdminForgetPassword.html', form_class = Admin_PasswordReset), name='password_reset'),
    path('password-reset/done/(?P[0-9]+)/\\Z', auth_views.PasswordResetDoneView.as_view(template_name = 'AdminPassRestDone.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'AdminPassRestConfirm.html', form_class = Admin_New_Rest_Password), name='password_reset_confirm'),
    path('password-rest-complete/(?P[0-9]+)/\\Z', auth_views.PasswordResetCompleteView.as_view(template_name = 'Admin_ResetComplate.html'), name='password_reset_complete'),
    path('delete/(?P[0-9]+)/\\Z', views.delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)