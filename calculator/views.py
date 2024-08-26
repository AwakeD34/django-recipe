from django.shortcuts import render
from django.http import HttpRequest

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    
}


def start(request):
    return render (request, 'calculator/start.html')


def omlet(request: HttpRequest):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            servings = 1
    except ValueError:
        servings = 1

    recipe = {k: v * servings for k, v in DATA['omlet'].items()}
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta(request: HttpRequest):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            servings = 1
    except ValueError:
        servings = 1

    recipe = {k: v * servings for k, v in DATA['pasta'].items()}
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter(request: HttpRequest):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            servings = 1
    except ValueError:
        servings = 1

    recipe = {k: v * servings for k, v in DATA['buter'].items()}
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)
