from .models import Page
from django.shortcuts import get_object_or_404, render


# Create your views here.

def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, 'pages/sample.html', {'page':page})