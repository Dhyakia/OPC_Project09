from django.shortcuts import render

# Create your views here.
def flux(request):
    return render(
        request,
        'review/flux.html'
    )

def follows(request):
    return render(
        request,
        'review/follows.html'
    )

def createTicket(request):
    return render(
        request,
        'review/create_ticket.html'
    )

def createReview(request):
    return render(
        request,
        'review/new_review.html'
    )

def myContent(request):
    return render(
        request,
        'review/my_content.html'
    )

def editReview(request):
    return render(
        request,
        'review/edit_review.html'
    )

def editTicket(request):
    return render(
        request,
        'review/edit_ticket.html'
    )

def confirmDelete(request):
    return render(
        request,
        'review/delete_content.html'
    )
