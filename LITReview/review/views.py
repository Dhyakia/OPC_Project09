from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import CharField, Value


from . import forms
from review.models import Ticket


@login_required
def flux(request):
    return render(request, 'review/flux.html')


@login_required
def follows(request):
    return render(request, 'review/follows.html')


@login_required
def createTicket(request):

    template_name = 'review/create_ticket.html'
    form_class = forms.TicketForm

    if request.method == 'GET':
        form = form_class()
        message = ''
        return render(request, template_name, context={'form': form, 'message': message})

    elif request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('my-content')
        
        message = 'forms incorrect.'
        return render(request, template_name, context={'form': form, 'message': message})


@login_required
def createReview(request):
    return render(
        request, 'review/new_review.html')


@login_required
def myContent(request):

    # take reviews
    # annotate reviews

    # TODO: take tickets wich value 'user' is equal to the current USER
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine the posts
    # TODO: ORDER PER DATE
    posts = tickets

    # TODO: CHANGE CONTEXT WHEN USING POST
    context = {'posts': posts}
    return render(request, 'review/my_content.html', context=context)


@login_required
def editReview(request):
    return render(request, 'review/edit_review.html')


@login_required
def editTicket(request, id):

    ticket = Ticket.objects.get(id=id)

    if request.method == 'GET':
        form = forms.TicketForm(instance=ticket)

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        
        if form.is_valid():
            form.save()
            return redirect('my-content')

    context = {'form': form}

    return render(request, 'review/edit_ticket.html', context=context)


@login_required
def confirmDelete(request):
    return render(request, 'review/delete_content.html')
