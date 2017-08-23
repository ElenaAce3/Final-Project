from django import forms
# from django import Club

from .models import Club

class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ('club_name', 'club_meeting', 'club_event', 'club_contact', 'club_bio', 'club_school')

# class ClubForm(forms.Form):
#     # mb add "max_length=250" to all of these
#     name_info = forms.CharField(widget=forms.Textarea)
#     meetings_info = forms.CharField(widget=forms.Textarea)
#     events_info = forms.CharField(widget=forms.Textarea)
#     contact_info = forms.CharField(widget=forms.Textarea)
#     bio_info = forms.CharField(widget=forms.Textarea)
