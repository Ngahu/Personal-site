from django.shortcuts import render



def index(request):
    """incharge of returning the home page """
    return render(request, 'Portfolio/projects.html', {})
