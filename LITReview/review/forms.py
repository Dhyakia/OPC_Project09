from django import forms
from django.shortcuts import render
from review.models import Ticket, Review

from django.utils.safestring import mark_safe


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("title", "description", "image")


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("headline", "rating", "body")
        # TODO: rating doit s'afficher comme une liste 'radio'
        # horizontalement
        widgets = {"rating": forms.RadioSelect()}
