from django.shortcuts import render

# Create your views here.

def index(request):
    """
    App index view.
    """
    return render(request, 'shop/index.html', {})