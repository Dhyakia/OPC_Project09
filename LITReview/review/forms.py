from django import forms
from review.models import Ticket, Review


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("title", "description", "image")


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("title", "rating", "body")
