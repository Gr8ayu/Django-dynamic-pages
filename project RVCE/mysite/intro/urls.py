from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# Create your views here.

app_name = "intro"

urlpatterns = [
    url(r'^$', views.index, name="homepage"),
    url(r'^departments/$', views.BranchList.as_view(), name="branch"),
    url(r'^departments/(?P<pk>[0-9]+)/$', views.BranchDetail.as_view(), name="branchDetail"),

    url(r'^update/$', views.update_profile, name='profileUpdate'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/login/$', auth_views.login, name='login'),

    # By default, the django.contrib.auth.views.login view will try to render the registration/login.html
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^students/$', views.StudentList.as_view(), name="StudentList"),


]
