from django.http import HttpResponse

def index(request):
    """incharge of returning the home page """
    return HttpResponse("tesla")