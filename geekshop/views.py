from django.shortcuts import render


def index(request):
    context = {
        'slogan': 'супер предложение',
        'user': 'ХИТ ПРОДАЖ!'
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')
