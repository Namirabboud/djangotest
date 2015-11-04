from django.conf.urls import url
from django.views.generic.base import RedirectView


from . import views

urlpatterns = [
    url( r'^$', RedirectView.as_view( url='messenger/', permanent=False ), name='index' ),
    url( r'^your-name/$', views.welcome, name='welcome' )
]
