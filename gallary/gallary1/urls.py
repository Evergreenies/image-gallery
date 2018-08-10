from django.conf.urls import url
from . import views
from django.views.generic import View, TemplateView

app_name = 'gallary1'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='gallary1/home1.html'), name='homepage'),
    url(r'^nature/$', views.NatureView.as_view(), name='nature'),
    url(r'^craft/$', views.CraftView.as_view(), name='craft'),
    url(r'^traditional/$', views.TraditionalView.as_view(), name='traditional'),
]
