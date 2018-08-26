# accounts.passwords.urls.py 
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns  = [
        path(r'password/change/', 
                auth_views.PasswordChangeView.as_view(), 
                name='password_change'),
        path(r'password/change/done/',
                auth_views.PasswordChangeDoneView.as_view(), 
                name='password_change_done'),
        path(r'password/reset/', 
                auth_views.PasswordResetView.as_view(), 
                name='password_reset'),
        path(r'password/reset/done/', 
                auth_views.PasswordResetDoneView.as_view(), 
                name='password_reset_done'),
        path(r'password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
                auth_views.PasswordResetConfirmView.as_view(), 
                name='password_reset_confirm'),
        path(r'password/reset/complete/', 
                auth_views.PasswordResetCompleteView.as_view(), 
                name='password_reset_complete'),
]