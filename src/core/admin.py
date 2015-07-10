from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import DocumentContent, Pessoa, HistoricalPessoa, Document


# Register your models here.
@admin.register(DocumentContent)
class DocumentContentAdmin(SimpleHistoryAdmin):
    list_display = ['content', 'created_at', 'created_by']

# Register your models here.
@admin.register(Pessoa)
class PessoaAdmin(SimpleHistoryAdmin):
    list_display = ['conteudo', 'user', 'contador', 'contador2']

@admin.register(HistoricalPessoa)
class HistorialPessoaAdmin(admin.ModelAdmin):
    pass

class DocumentContentInline(admin.StackedInline):
    model = DocumentContent

@admin.register(Document)
class Document(admin.ModelAdmin):
    inlines = [DocumentContentInline]


