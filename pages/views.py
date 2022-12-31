from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'page/home.html'


class AboutUsView(generic.TemplateView):
    template_name = 'page/about_us.html'
