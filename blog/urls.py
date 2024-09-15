from blog.views import iletisim, anasayfa, kategori
from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('', anasayfa, name='anasayfa') ,
    path('iletisim', iletisim, name='iletisim'), # biri benim iletisim kaynağıma gelirse iletisim fonksyionumla cevap ver diyoruz
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori')

]
