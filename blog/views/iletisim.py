from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel
from django.views.generic import FormView

class IletisimFormView(FormView):
    template_name = 'pages/iletisim.html'
    form_class = IletisimForm
    success_url = 'iletisim/email-gonderildi'


    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

