from django.shortcuts import render, get_object_or_404, redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
import logging

logger = logging.getLogger('konu_okuma')
class DetayView(View):

    http_method_names = ['get', 'post']
    yorum_ekleme_formu = YorumEkleModelForm

    def get(self, request, slug):
        #print(1/0)
        yazi = get_object_or_404(YazilarModel, slug=slug) #yazıları aldık

        if request.user.is_authenticated:
            logger.info('konu okundu:' + request.user.username) #kullanılarımızın verisini logluyoruz

        yorumlar = yazi.yorumlar.all() #yazıya yapılan yorumları aldık
        yorum_ekle_form = self.yorum_ekleme_formu()
        return render(request, 'pages/detay.html', context={

            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorum_ekle_form': yorum_ekle_form

    })

    def post(self, request, slug):

        yazi = get_object_or_404(YazilarModel, slug=slug) #yazıları aldık
        yorum_ekle_form = self.yorum_ekleme_formu(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()

        return redirect('detay', slug=slug)






