from django.shortcuts import render
from django.views.generic import TemplateView
from .models import School
from .models import Club
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ClubForm


# def school_list(request):
#     schools= School.objects
#     #Club.objects.order_by('created_date')
#     return render(request, 'clubs/FinalProjectHTML.html', {'schools': schools})

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        schools = School.objects.filter()
        return render(request,'FinalProjectHTML.html', {'schools': schools})

class SchoolPageView(TemplateView):
    def get(self, request, **kwargs):
        clubs = Club.objects.filter()
        school_nm = request.GET["school"]
        school = School.objects.filter(school_name=school_nm).first()
        return render(request,'school_display.html', {'school': school, 'clubs': clubs})
#
class BackPageView(TemplateView):
    def get(self, request, **kwargs):
        schools = School.objects.filter()
        return render(request,'FinalProjectHTML.html', {'schools': schools})
#
class CreatePageView(TemplateView):
    template_name = "create_club.html"

class ClubPageView(TemplateView):
    def get(self, request, **kwargs):
        #clubs = Club.objects.filter()
        club_nm = request.GET["club"]
        club = Club.objects.filter(club_name=club_nm).first()
        return render(request,'view_club.html', {'club': club})

#all of this is probably wrong
def post_new(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('school_display.html', pk=post.pk)
    else:
        form = ClubForm()
    return render(request, 'create_club.html', {'form': form})
