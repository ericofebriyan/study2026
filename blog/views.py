from django.shortcuts import redirect


def home(request):
    # Redirect homepage to perfume CRUD list
    return redirect('perfume-list')

