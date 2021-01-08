from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Widget


def index(request):
    todos = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})


class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"
