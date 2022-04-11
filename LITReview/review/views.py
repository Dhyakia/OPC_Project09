from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import CharField, Value
from itertools import chain

from review import forms
from review.models import Ticket, Review, UserFollows
from authentication.models import User


@login_required
def follows(request):

    if request.method == 'GET':

        message = ''
        followers = UserFollows.objects.filter(followed_user=request.user)
        followings = UserFollows.objects.filter(user=request.user)

        context = {'message': message, 'followers': followers, 'followings': followings}
        return render(request, 'review/follows.html', context=context)

    if request.method == 'POST':
        if 'send-username' in request.POST:
            user_input = request.POST.get("username-follows")

            if User.objects.filter(username=user_input):
                followed_user = User.objects.get(username=user_input)
                obj = UserFollows()
                obj.user = request.user
                obj.followed_user = followed_user
                obj.save()

                return redirect('follows')

            else:
                return redirect('follows')

        if 'unfollow' in request.POST:

            # Je récupère la value de l'input cacher (qui est en fait le token)
            id_to_delete = request.POST.get('unfollow')
            obj = UserFollows.objects.get(id=id_to_delete)
            obj.delete()
            return redirect('follows')


@login_required
def flux(request):

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
    return render(request, 'review/flux.html', context=context)


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
def createCritic(request, id):

    template_name = 'review/create_critic.html'
    ticket = Ticket.objects.get(id=id)

    review_form = forms.ReviewForm

    if request.method == 'GET':
        r_form = review_form()
        message = ''
        context = {'ticket': ticket, 'r_form': r_form, 'message': message}

        return render(request, template_name, context=context)

    elif request.method == 'POST':
        r_form = review_form(request.POST)

        if r_form.is_valid():
            review = r_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect('my-content')

        message = 'forms incorrect'
        context = {'ticket': ticket, 'r_form': r_form, 'message': message}
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

    review = Review.objects.get(id=id)

    if request.method == 'GET':
        context = {'review': review}
        return render(request, 'review/delete_review.html', context=context)

    if request.method == 'POST':

        review.delete()
        return redirect('my-content')

    return render(request, 'review/delete_review.html')
