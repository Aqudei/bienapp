from django.db import models
from django.utils.text import gettext_lazy as _

# Create your models here.


class InputFile(models.Model):
    file = models.FileField(_("Input File"))
    description = models.CharField(
        _("Description"), max_length=255, null=True, blank=True)
    dete_uploaded = models.DateTimeField(_("Date Uploaded"), auto_now_add=True)
