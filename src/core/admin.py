from django.contrib import admin

from .models import Document


# Register your models here.
@admin.register(Document)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'created_by']

