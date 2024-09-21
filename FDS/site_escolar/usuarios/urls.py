from django.urls import path
from .views import login_view, cadastro_view , home_view , documentos_view

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('home/', home_view, name='home'),
    path('documentos/', documentos_view, name='documentos')   
]
