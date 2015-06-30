from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Document


# Register your models here.
@admin.register(Document)
class DocumentoAdmin(SimpleHistoryAdmin):
    list_display = ['content', 'created_at', 'created_by']

