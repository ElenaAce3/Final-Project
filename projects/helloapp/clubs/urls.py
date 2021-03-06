from django.conf.urls import url
from clubs import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #url(r'^$', views.school_list, name='school_list'),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^FinalProjectHTML.html$', views.BackPageView.as_view()), # Add this /home/ route
    url(r'^school_display.html$', views.SchoolPageView.as_view()),
    url(r'^create_club.html$', views.CreatePageView.as_view()), # Add this /create_club/ route
    url(r'^view_club.html$', views.ClubPageView.as_view()),
    url(r'^post/new/school_display.html$', views.post_new, name='post_new'),
    ]
# Add this /garfield_club/ route
#     url(r'^lincoln_clubs.html$', views.LincolnPageView.as_view()), # Add this /lincoln_clubs/ route
#     url(r'^bellevue_clubs.html$', views.BellevuePageView.as_view()), # Add this /bellevue_clubs/ route
#     url(r'^create_club.html$', views.CreatePageView.as_view()), # Add this /create_club/ route
#     # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
