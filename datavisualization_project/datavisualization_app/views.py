from django.shortcuts import render
from datavisualization_app.models import Dengue
from datavisualization_app.models import Education
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear

# from django.http import HttpResponse



# def index(request):
#     labels = []
#     data = []

#     queryset = Dengue.objects.all()[:4]
#     for dataset in queryset:
#         labels.append(dataset.Location)
#         data.append(dataset.Cases)
#     return render(request, 'index.html', {'labels': labels, 'data': data})

def index(request):
    # get all data

    dengue_data = Dengue.objects.order_by('Date')

    # bar graph for region data
    regions_data = Dengue.objects.values('Region').annotate(
        total_cases=Sum('Cases'),
        total_deaths=Sum('Deaths')
    )

    labels = []
    total_cases = []
    total_deaths = []

    for region_data in regions_data:
        labels.append(region_data['Region'])
        total_cases.append(region_data['total_cases'])
        total_deaths.append(region_data['total_deaths'])

    
# line graph query
    years_data = Dengue.objects.annotate(
        year=ExtractYear('Date')
    ).values('year').annotate(
        total_cases=Sum('Cases'),
        total_deaths=Sum('Deaths')
    )

    year_label = []
    year_cases = []
    year_deaths = []

    for year_data in years_data:
        year_label.append(year_data['year'])
        year_cases.append(year_data['total_cases'])
        year_deaths.append(year_data['total_deaths'])

    return render(request, 'index.html',
                   {'dengue_data': dengue_data,'labels': labels, 'total_cases': total_cases, 'total_deaths': total_deaths,
                    'year_label': year_label, 'year_cases': year_cases, 'year_deaths': year_deaths
                    })

def education_base(request):
    return render(request, "project3/proj3_base.html")


def education_datavis(request):
    return render(request, "project3/proj3_datavisualization.html")


def education_dataset(request):
    return render(request, "project3/proj3_dataset.html")
