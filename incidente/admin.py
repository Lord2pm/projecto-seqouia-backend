from django.contrib import admin

from .models import Incidente, TipoIncidente

admin.site.register(Incidente)
admin.site.register(TipoIncidente)
