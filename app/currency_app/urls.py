from django.urls import path
from .views import (hello_world,
                    filter_contact_us_msg,
                    rate_list,
                    contact_us_form,
                    SourceListView,
                    SourceCreateView,
                    SourceUpdateView,
                    SourceDeleteView,
                    SourceDetailView,
                    rate_create,
                    rate_update,
                    rate_delete,
                    rate_details)


urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('show_msgs/', filter_contact_us_msg, name='filter_messages'),
    path('rate_list/', rate_list, name='rate_list'),
    path('contact_us_form/', contact_us_form, name='contact_us_form'),
    path('rate_list/rate_create/', rate_create, name = 'rate_create'),
    path('rate_list/rate_update/<int:rate_id>/', rate_update, name = 'rate_update'),
    path('rate_list/rate_delete/<int:rate_id>/', rate_delete, name = 'rate_delete'),
    path('rate_list/rate_details/<int:rate_id>/', rate_details, name = 'rate_details'),
    path('source_list/', SourceListView.as_view(), name = 'source_list'),
    path('source_list/source_create/', SourceCreateView.as_view(), name = 'source_create'),
    path('source_list/source_update/<int:pk>/', SourceUpdateView.as_view(), name = 'source_update'),
    path('source_list/source_delete/<int:pk>/', SourceDeleteView.as_view(), name = 'source_create'),
    path('source_list/source_details/<int:pk>/', SourceDetailView.as_view(), name = 'source_view')
]
