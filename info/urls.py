from django.urls import path
from . import views
app_name='info'

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name='contact'),
    path('confirm-contact/',views.confirm_contact,name='confirm_contact'),
]
