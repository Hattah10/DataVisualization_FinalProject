from django.shortcuts import render
from datavisualization_app.models import Dengue
from django.http import HttpResponse

def index(request):
    labels = []
    data = []

    queryset = Dengue.objects.all()[:5]
    for dataset in queryset:
        labels.append(dataset.Location)
        data.append(dataset.Cases)


    return render(request, 'index.html', {'labels':labels, 'data':data})

