from . import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


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
    return render(request, 'review/my_content.html')

@login_required
def editReview(request):
    return render(request, 'review/edit_review.html')

@login_required
def editTicket(request):
    return render(request, 'review/edit_ticket.html')

@login_required
def confirmDelete(request):
    return render(request, 'review/delete_content.html')
