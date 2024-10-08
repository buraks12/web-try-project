from django.db import models

class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
