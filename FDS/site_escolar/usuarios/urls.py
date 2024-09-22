from django.urls import path
from .views import login_view, cadastro_view , home_view , documentos_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('home/', home_view, name='home'),
    path('documentos/', documentos_view, name='documentos')   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
