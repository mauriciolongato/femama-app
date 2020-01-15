from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.objects import Ong, QuestionarioCenso, CensoRespostas, ScoreRespostas, SegmentoOng, \
    Divulgacao, CanalDigital, Fornecedor, Parceria, \
    TipoCancer, EstagioCancer, SistemaSaude, FaixaEtaria, MapeamentoPaciente, ContatoPaciente, TipoParceria,\
    QuantidadeVoluntarios, Coalizao


# Cliente
class OngAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Ong._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Ong._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class CensoRespostasAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CensoRespostas._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in CensoRespostas._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class QuestionarioCensoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in QuestionarioCenso._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in QuestionarioCenso._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class ScoreRespostasAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ScoreRespostas._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in ScoreRespostas._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class SegmentoOngAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SegmentoOng._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in SegmentoOng._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class DivulgacaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Divulgacao._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Divulgacao._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class CanalDigitalAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CanalDigital._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in CanalDigital._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class FornecedorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Fornecedor._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Fornecedor._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class ParceriaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Parceria._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Parceria._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class TipoCancerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TipoCancer._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in TipoCancer._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class EstagioCancerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in EstagioCancer._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in EstagioCancer._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class SistemaSaudeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SistemaSaude._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in SistemaSaude._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class FaixaEtariaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in FaixaEtaria._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in FaixaEtaria._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class MapeamentoPacienteAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MapeamentoPaciente._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in MapeamentoPaciente._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class ContatoPacienteAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ContatoPaciente._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in ContatoPaciente._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class TipoParceriaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TipoParceria._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in TipoParceria._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class QuantidadeVoluntariosAdmin(admin.ModelAdmin):
    list_display = [f.name for f in QuantidadeVoluntarios._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in QuantidadeVoluntarios._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


class CoalizaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Coalizao._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Coalizao._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(Ong, OngAdmin)
admin.site.register(CensoRespostas, CensoRespostasAdmin)
admin.site.register(QuestionarioCenso, QuestionarioCensoAdmin)
admin.site.register(ScoreRespostas, ScoreRespostasAdmin)
admin.site.register(SegmentoOng, SegmentoOngAdmin)
admin.site.register(Divulgacao, DivulgacaoAdmin)
admin.site.register(CanalDigital, CanalDigitalAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Parceria, ParceriaAdmin)
admin.site.register(TipoCancer, TipoCancerAdmin)
admin.site.register(EstagioCancer, EstagioCancerAdmin)
admin.site.register(SistemaSaude, SistemaSaudeAdmin)
admin.site.register(FaixaEtaria, FaixaEtariaAdmin)
admin.site.register(MapeamentoPaciente, MapeamentoPacienteAdmin)
admin.site.register(ContatoPaciente, ContatoPacienteAdmin)
admin.site.register(TipoParceria, TipoParceriaAdmin)
admin.site.register(QuantidadeVoluntarios, QuantidadeVoluntariosAdmin)
admin.site.register(Coalizao, CoalizaoAdmin)
