from django.shortcuts import render
from django.http import HttpResponse
from .models import Univer

def first_view(request):
    univerlar = Univer.objects.all()
    html = "<h1>Universitetlar ro'yxati</h1><ul>"
    for unver in univerlar:
        html += f"<li>{unver.nomi}</li>"
    html += "</ul>"
    return HttpResponse(html)