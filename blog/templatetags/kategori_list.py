from django import template 
from blog.models import KategoriModels


register = template.Library()

@register.simple_tag
def kategori_list():
    kategoriler = KategoriModels.objects.all()
    return kategoriler



