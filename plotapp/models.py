from django.db import models
from django.utils.text import gettext_lazy as _

# Create your models here.


class InputFile(models.Model):
    STATUS_CHOICES = (('queued','queued'), ('processing','processing'),('done','done'),('error','error'))
    file = models.FileField(_("Input File"))
    description = models.CharField(
        _("Description"), max_length=255, null=True, blank=True)
    dete_uploaded = models.DateTimeField(_("Date Uploaded"), auto_now_add=True)
    status = models.CharField(_("Staus"), max_length=50, choices=STATUS_CHOICES, default='queued')
    pdf_file = models.FileField(_("PDF File"), null=True)