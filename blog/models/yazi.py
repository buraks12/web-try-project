from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModels
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel


class YazilarModel(DateAbstractModel):

    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik =models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik', unique=True) #baslık variablından oluşturulacağını belirttik
    kategoriler = models.ManyToManyField(KategoriModels, related_name='yazi') #bir yazının birden fazla kategoriye atanabilmesi için gereklidir
    #bir kategoriden birden fazla yazıya erişmek için relatedname i kullanıyoruz
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar') #ondelete -> bir user silindiğinde ona ait bütün yazıların silinmesine yarar
     
    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik