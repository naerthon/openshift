from django.conf.urls   import url
from django.contrib.auth.views import login,logout
from .views             import register,password_reset,password_reset_confirm,edit,edit_password
from .forms import AuthForm

urlpatterns = [
    url(r'^login/$',login,{'authentication_form': AuthForm},name='login'),
    url(r'^logout/$',logout,{'next_page': 'core:index'}, name='logout'),
    url(r'^cadastre-se/$',register,name='register'),
    url(r'^nova-senha/$',password_reset,name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$',edit_password,name='edit_password'),
]
