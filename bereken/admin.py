from django.contrib import admin
from .models import Kosten,Leveranciers,Netbeheerders,Netbeheerderkosten,Algemenekosten,Regiotoeslag

# Register your models here.

admin.site.register(Kosten)
admin.site.register(Leveranciers)
admin.site.register(Netbeheerders)
admin.site.register(Netbeheerderkosten)
admin.site.register(Algemenekosten)
admin.site.register(Regiotoeslag)
