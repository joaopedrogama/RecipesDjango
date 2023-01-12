from django.shortcuts import render

# from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Gama'
    })


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Gama'
    })
