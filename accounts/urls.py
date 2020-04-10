from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^passwordchange/$', views.passwordchange_view, name="passwordchange"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_view, name="activate"),
    url(r'^update/(?P<pk>[\-\w]+)/$', views.edit_user, name='account_update'),
]
