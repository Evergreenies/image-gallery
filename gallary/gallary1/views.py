from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import View, TemplateView
from .models import UploadImage


class  NatureView(generic.ListView):
    template_name='gallary1/gallarys.html'

    def get_queryset(self):
        return UploadImage.objects.filter(category='natural')


class  CraftView(generic.ListView):
    template_name='gallary1/gallarys.html'

    def get_queryset(self):
        return UploadImage.objects.filter(category='craft')


class  TraditionalView(generic.ListView):
    template_name='gallary1/gallarys.html'

    def get_queryset(self):
        return UploadImage.objects.filter(category='traditional')





# class IndexView(TemplateView):
#     # return render(request, 'gallary1/home1.html')
#     template_name = 'gallary1/home1.html'

#     # def get(self, request):
#     #     return render(request, 'gallary1/home1.html')

#     # # def get_queryset(self):
#     # #     return {}

# def gallarys(request):
#     return render(request, 'gallary1/gallarys.html')
