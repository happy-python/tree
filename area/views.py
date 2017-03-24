from django.shortcuts import render_to_response
from .models import Area


def tree(request):
    nodes = Area.objects.all()
    return render_to_response('tree.html', {'nodes': nodes})
