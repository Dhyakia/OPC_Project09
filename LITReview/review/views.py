from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import CharField, Value
from itertools import chain

from . import forms
from review.models import Ticket
from review.models import Review


@login_required
def follows(request):
    return render(request, 'review/follows.html')


@login_required
def flux(request):
    return render(request, 'review/flux.html')


@login_required
def myContent(request):

    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    context = {'posts': posts}
    return render(request, 'review/my_content.html', context=context)


@login_required
def createTicket(request):

    template_name = 'review/create_ticket.html'
    form_class = forms.TicketForm

    if request.method == 'GET':
        form = form_class()
        message = ''

        context = {'form': form, 'message': message}
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('my-content')
        
        message = 'forms incorrect.'

        context = {'form': form, 'message': message}
        return render(request, template_name, context=context)


@login_required
def createReview(request):

    template_name = 'review/create_review.html'
    ticket_form = forms.TicketForm
    review_form = forms.ReviewForm

    if request.method == 'GET':
        t_form = ticket_form()
        r_form = review_form()
        message = ''

        context = {'t_form': t_form, 'r_form': r_form, 'message': message}
        return render(request, template_name, context=context)

    elif request.method == 'POST':
        t_form = ticket_form(request.POST, request.FILES)
        r_form = review_form(request.POST)

        if t_form.is_valid() and r_form.is_valid():

            ticket = t_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = r_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('my-content')

        message = 'forms incorrect'
        
        context = {'t_form': t_form, 'r_form': r_form, 'message': message}
        return render(request, template_name, context=context)


@login_required
def editTicket(request, id):

    ticket = Ticket.objects.get(id=id)

    if request.method == 'GET':
        form = forms.TicketForm(instance=ticket)
        context = {'form': form}
        return render(request, 'review/edit_ticket.html', context=context)

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        
        if form.is_valid():
            form.save()
            return redirect('my-content')


@login_required
def editReview(request, id):

    review = Review.objects.get(id=id)

    if request.method == 'GET':
        form = forms.ReviewForm(instance=review)
        ticket = review.ticket
        context = {'form': form, 'ticket': ticket}
        return render(request, 'review/edit_review.html', context=context)

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('my-content')


@login_required
def deleteTicket(request, id):

    ticket = Ticket.objects.get(id=id)

    if request.method == 'GET':
        context = {'ticket': ticket}
        return render(request, 'review/delete_ticket.html', context=context)

    if request.method == 'POST':
        
        if ticket.image:
            ticket.image.delete()

        ticket.delete()
        
        return redirect('my-content')


@login_required
def deleteReview(request, id):

    return render(request, 'review/delete_review.html')