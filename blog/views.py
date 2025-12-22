from django.http import HttpResponse

def home(request):
    return HttpResponse("Halo, Erico! Django sudah jalan 🚀")