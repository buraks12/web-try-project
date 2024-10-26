
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def yazilarim(request):
    #giriş yapmış olan kullanıcının yazılarına ulaşmamız lazım



    yazilar = request.user.yazilar.order_by('-id') #bu kategoriye bağlı bütün yazıları çekebiliyoruz
    print(yazilar)
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 5) #bir sayfada min kaç adet yazı gözükmesini istediğini 2.parametrede belirtiyorsun

    return render(request, 'pages/yazilarim.html', context={
        'yazilar' : paginator.get_page(sayfa),
        
    })