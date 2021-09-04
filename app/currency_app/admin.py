
from django.contrib import admin
from .models import Rate, ContactUs, Source
# from rangefilter.filters import DateRangeFilter
# from import_export import ImportExportModelAdmin
# from import_export import resource
# Register your models here.


class RateAdmin(admin.ModelAdmin):

    list_display = (


        'buy',
        'sale',
        'source',
        'currency',
    )

    # filter by
    list_filter = (

        'currency',
        'source',
    )

    # search fields
    search_fields = (
        'source',
        'currency'
    )

    # can't edit it
    readonly_fields = (
        'source',
        'currency',
    )

    # define permissions on who can edit/delete data in admin:

    def has_delete_permissions(self, request, obj=None):
        return False


class SourceAdmin(admin.ModelAdmin):

    list_display = (

        'id',
        'name',
        'source_url',

    )

    # filter by
    list_filter = (

        'name',)

    # search fields
    search_fields = (
        'name',
        'source_url'
    )

    # can't edit it
    readonly_fields = (
        'name',
        'source_url',
    )

    # define permissions on who can edit/delete data in admin:
    def has_delete_permissions(self, request, obj=None):
        return False


class ContactUsAdmin(admin.ModelAdmin):

    list_display = (

        'email_from',
        'subject',
        'message',
    )

    # filter by
    list_filter = (

        'created',
        'email_from',
    )

    # search fields
    search_fields = (
        'subject',

    )

    # define permissions on who can edit/delete data in admin:

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)

admin.site.register(Source, SourceAdmin)

admin.site.register(ContactUs, ContactUsAdmin)



