from django import forms
from review.models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("title", "description", "image")


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("headline", "rating", "body")
        widgets = {"rating": forms.RadioSelect()}


class UserFollowsForm(forms.ModelForm):

    class Meta:
        model = UserFollows
        fields = ('user', 'followed_user')
