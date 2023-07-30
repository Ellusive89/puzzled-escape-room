from django.shortcuts import render

# Create your views here.


def escaperoom_page_view(request):
    return render(request, 'escaperoom.html')
