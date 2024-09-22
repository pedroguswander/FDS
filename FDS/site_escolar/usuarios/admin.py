from django.contrib import admin

from django.contrib import admin
from .models import Usuario
from .models import Documento

admin.site.register(Usuario)
admin.site.register(Documento)