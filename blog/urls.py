
from django.contrib import admin
from django.urls import path, include
from blog.views import iletisim, anasayfa, KategoriListView, yazilarim, detay, yazi_ekle, yazi_guncelle, yorum_sil, DetayView, YaziSilDeleteView, YaziEkleCreateView, YaziGuncelleUpdateView, IletisimFormView
from django.views.generic import TemplateView, RedirectView






urlpatterns = [
    path('', anasayfa, name='anasayfa') ,
    path('hakkimda', TemplateView.as_view(
        template_name='pages/hakkimda.html'
    ), name='hakkimda'),
    path('yonlendir', RedirectView.as_view(
        url='https://www.google.com'
    ), name='yonlendir'),
    path('iletisim', IletisimFormView.as_view(), name='iletisim'), # biri benim iletisim kaynağıma gelirse iletisim fonksyionumla cevap ver diyoruz
    path('kategori/<slug:kategoriSlug>', KategoriListView.as_view(
        
    ), name='kategori'),
    path('yazilarim', yazilarim , name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(
        
    ) , name='detay'),
    path('yazi-ekle', YaziEkleCreateView.as_view() , name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view() , name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view() , name='yazi-sil'),
    path('yorum-sil/<int:id>', yorum_sil , name='yorum-sil'),
    

    


]
