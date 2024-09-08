from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'main',
        'name': 'Farrel Dharmawan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)