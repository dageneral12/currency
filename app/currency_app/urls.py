from django.urls import path
from .views import (hello_world,
                    filter_contact_us_msg,
                    rate_list,
                    contact_us_form)


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('show_msgs/', filter_contact_us_msg, name='filter_messages'),
    path('rate_list/', rate_list, name='rate_list'),
    path('contact_us_form', contact_us_form, name='contact_us_form'),
]
