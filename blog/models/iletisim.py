from django.db import models

class IletisimModel(models.Model):

    email = models.EmailField(max_length=250) #validation ı django otomatik yapıyor. Command ile source koduna bak.!.
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)


    class Meta:

        db_table = 'iletisim'     
        verbose_name = 'Iletisim'
        verbose_name_plural = 'Iletisim'

    def __str__(self):
        return self.email
       