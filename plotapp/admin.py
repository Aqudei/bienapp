from django.contrib import admin
from plotapp import models
# Register your models here.
@admin.register(models.InputFile)
class InputFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'description', 'dete_uploaded', 'status')

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('status', )
        return self.readonly_fields