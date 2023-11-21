from django.shortcuts import render
from datavisualization_app.models import Dengue
from datavisualization_app.models import Education
from django.http import HttpResponse


def index(request):
    labels = []
    data = []

    queryset = Dengue.objects.all()[:4]
    for dataset in queryset:
        labels.append(dataset.Location)
        data.append(dataset.Cases)
    return render(request, 'index.html', {'labels': labels, 'data': data})


def education_base(request):
    return render(request, "project3/proj3_base.html")


def education_datavis(request):
    return render(request, "project3/proj3_datavisualization.html")


def education_dataset(request):
    return render(request, "project3/proj3_dataset.html")
