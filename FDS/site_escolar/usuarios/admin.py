from django.contrib import admin

from django.contrib import admin
from .models import Usuario
from .models import Documento
from .models import Solicitacao

admin.site.register(Usuario)
admin.site.register(Documento)
admin.site.register(Solicitacao)