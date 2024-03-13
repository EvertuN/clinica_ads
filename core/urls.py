from django.urls import path

from core import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('relatorios/pacientes', views.PacientesListView.as_view(), name='relat_pacientes'),
    path('relatorios/pdfpacientes', views.RelatPdfPacientes.as_view(), name='pdfpacientes'),
    path('relatorios/pacientes_convenio/', views.PacientesConvenioListView.as_view(), name='pacientes_convenio'),
    path('relatorios/pdfpacientesconvenio/', views.RelatPdfPacientesConvenio.as_view(), name='pdfpacientesconvenio'),
]
