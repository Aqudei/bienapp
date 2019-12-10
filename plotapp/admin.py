from django.contrib import admin
from plotapp import models
# Register your models here.
@admin.register(models.InputFile)
class InputFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'description', 'dete_uploaded', 'status', 'pdf_file')
    readonly_fields = ('status', 'pdf_file')
