from django.conf.urls import url
from . import views

app_name= "payment_ns"

urlpatterns =[
    url(r'^$', views.pay, name="pay"),
    url(r'^help/$', views.help, name="help"),
    url(r'^(?P<payment_type>\D+)/',
        views.pay, {'discount': '40'}, name ="pay_details"),
]




def com(*dim, **kwargs ):
    pass


com(1, 2, 3, width=2, height=3, length=2)