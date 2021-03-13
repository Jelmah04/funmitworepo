
from django.urls import path
from django.conf.urls import url
from . import views
from .views import Register, Login


urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('login', views.login, name='login'),

	# url(r'^login/$', views.signin, name='login'),
	url(r'^reg/$', views.reg, name='reg'),
    url(r'^check-mail-ajax/$', views.check_mail_ajax, name='check_mail_ajax'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'login-req', Login.as_view(), name='login_ajax'),
    
    # url(r'^check-mail-ajax/$', views.check_mail_ajax, name='check_mail_ajax'),
    # url(r'^register/$', Register.as_view(), name='register'),
    # url(r'login-req', Login.as_view(), name='login_ajax'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('register', views.register, name='register'),
    path('addtouser', views.addtouser, name='addtouser'),
    path('funding', views.funding, name='funding'),
    path('fundings', views.fundings, name='fundings'),
    path('transaction', views.transaction, name='transaction'),
    path('services', views.services, name='services'),
    path('airtime', views.airtime, name='airtime'),
    path('data', views.data, name='data'),
    path('cable', views.cable, name='cable'),
    path('electricity', views.electricity, name='electricity'),
    path('wallet', views.wallet, name='wallet'),
    path('profile', views.profile, name='profile'),
    path('sendmail', views.sendmail, name='sendmail'),
]






