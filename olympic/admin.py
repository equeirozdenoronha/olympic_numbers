from django.contrib import admin
from django.core import management
from django.shortcuts import redirect

from .models import NOC


class NOCAdmin(admin.ModelAdmin):
    def import_movies_from_url(request):
        print('import nocs here')
        try:
            management.call_command('import_from_csv')
            message = 'successfully imported data from CSV'

        except Exception as ex:
            message = 'Error importing from data from CSV {}'.format(str(ex))

        admin.ModelAdmin.message_user(NOC, request, message)
        return redirect('admin:index')


admin.site.register(NOC, NOCAdmin)
