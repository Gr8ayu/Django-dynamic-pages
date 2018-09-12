from django.conf.urls import url
from . import views
# Create your views here.

app_name = "blogs"

urlpatterns = [
    url(r'^new/$', views.PostCreate.as_view(), name="BlogCreate"),
    url(r'^$', views.PostList.as_view(), name="BlogList"),
    url(r'^new/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="BlogDetail"),


]
