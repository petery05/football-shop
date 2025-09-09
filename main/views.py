from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project' : 'Football Shop',
        'npm' : '2406432910',
        'name': 'Peter yap',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)