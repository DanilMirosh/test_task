from django.shortcuts import render

INDEX_HTML = 'task/index.html'


def index(request):
    return render(request, INDEX_HTML)
