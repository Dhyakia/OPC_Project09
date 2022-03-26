from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def flux(request):
    return render(request, 'review/flux.html')

@login_required
def follows(request):
    return render(request, 'review/follows.html')

@login_required
def createTicket(request):
    return render(
        request, 'review/create_ticket.html')

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
