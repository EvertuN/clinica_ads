from io import BytesIO

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView, ListView
from xhtml2pdf import pisa

from core.models import Paciente, Possui, Consulta, Medico


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class PacientesListView(ListView):
    template_name = "relatorios/pacientes.html"
    model = Paciente
    context_object_name = 'pacientes'


class RelatPdfPacientes(View):

    def get(self, request):
        pacientes = Paciente.objects.all()
        data = {
            'pacientes': pacientes
        }
        template = get_template("relatorios/pdfpacientes.html")
        html = template.render(data)
        result = BytesIO()
        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        except Exception as e:
            print(e)
            return


class PacientesConvenioListView(ListView):
    template_name = "relatorios/pacientes_convenio.html"
    context_object_name = 'pacientes_por_convenio'

    def get_queryset(self):
        pacientes_por_convenio = {}

        pacientes = Paciente.objects.all()

        for paciente in pacientes:
            possui_entries = Possui.objects.filter(paciente=paciente.id)
            for possui_entry in possui_entries:
                convenio = possui_entry.convenio
                if convenio not in pacientes_por_convenio:
                    pacientes_por_convenio[convenio] = []

                pacientes_por_convenio[convenio].append({
                    'nome': paciente.nome,
                    'idade': paciente.idade
                })

        return pacientes_por_convenio


class RelatPdfPacientesConvenio(View):

    def get(self, request):
        pacientes_por_convenio = PacientesConvenioListView().get_queryset()
        data = {
            'pacientes_por_convenio': pacientes_por_convenio
        }
        template = get_template("relatorios/pdfpacientesconvenio.html")
        html = template.render(data)
        result = BytesIO()
        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        except Exception as e:
            print(e)
            return HttpResponse('Error gerando o PDF', content_type='text/plain')

