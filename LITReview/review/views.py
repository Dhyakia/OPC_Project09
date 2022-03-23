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