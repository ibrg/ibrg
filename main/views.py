from django.shortcuts import render


def index(request):
    turn_on_block = True
    return render(request, 'index.html', {'turn_on_block': turn_on_block,})
