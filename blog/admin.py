from django.contrib import admin
from blog.models import KategoriModels, YazilarModel, YorumModel, IletisimModel


admin.site.register(KategoriModels)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (

        'baslik', 'olusturulma_tarihi', 'duzenleme_tarihi'
    )



@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):

    list_display = (

        'yazan', 'olusturulma_tarihi', 'duzenleme_tarihi'
    )
    search_fields = ('yazan__username',)


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):

    list_display = (
        'email', 'olusturulma_tarihi'
    )
    search_fields = ('email',)







# Register your models here.
