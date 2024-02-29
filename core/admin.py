from django.contrib import admin

from . import models


@admin.register(models.Ambulatorio)
class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numleitos', 'andar']


class MedicoConvenioInLine(admin.StackedInline):
    model = models.Atende
    extra = 1
    raw_id_fields = ['convenio']


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['crm', 'telefone', 'salario', 'ambulatorio']
    inlines = [MedicoConvenioInLine]


@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'cidade', 'idade', 'ambulatorio']
