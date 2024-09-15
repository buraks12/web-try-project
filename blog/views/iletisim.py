from django.shortcuts import render
from django.http import HttpResponse

def iletisim(request):

    context ={
        'key': 'başlık içerik naber'
    }
    
    
    return render(request, 'pages/iletisim.html', context=context)