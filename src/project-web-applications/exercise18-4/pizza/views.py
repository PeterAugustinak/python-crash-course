from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for Pizza app."""
    return render(request, 'pizza/index.html')