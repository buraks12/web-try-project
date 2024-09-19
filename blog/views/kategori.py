
from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModels
from django.core.paginator import Paginator



def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModels, slug=kategoriSlug)
    yazilar = kategori.yazi.order_by('-id') #bu kategoriye bağlı bütün yazıları çekebiliyoruz
    print(yazilar)
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2) #bir sayfada min kaç adet yazı gözükmesini istediğini 2.parametrede belirtiyorsun

    return render(request, 'pages/kategori.html', context={
        'yazilar' : paginator.get_page(sayfa),
        'kategori_isim': kategori.isim
    })