from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import login as authLogin
from django.contrib.auth.views import logout 
from simplemooc.accounts.views import edit, dashboard, register, edit_password, password_reset, password_reset_confirm

 
urlpatterns = [
 
    url(r'^$', dashboard,  name='dashboard'),
    url(r'^entrar/$', authLogin, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^editar/$', edit,  name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),

]