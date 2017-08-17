from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'FinalProjectHTML.html', context=None)
# class HomePageView(TemplateView):
#     template_name = "FinalProjectHTML_copy.html"
class GarfieldPageView(TemplateView):
    template_name = "garfield_clubs.html"

class BackPageView(TemplateView):
    template_name = "FinalProjectHTML.html"

class LincolnPageView(TemplateView):
    template_name = "lincoln_clubs.html"

class BellevuePageView(TemplateView):
    template_name = "bellevue_clubs.html"

class CreatePageView(TemplateView):
    template_name = "create_club.html"
