from django.shortcuts import render
from datavisualization_app.models import Dengue
from datavisualization_app.models import Education
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear, ExtractMonth
import json
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
    ).order_by('Region')

    region_label = []
    region_cases = []
    region_deaths = []

    for region_data in regions_data:
        region_label.append(region_data['Region'])
        region_cases.append(region_data['total_cases'])
        region_deaths.append(region_data['total_deaths'])

    
# line graph query
    years_data = Dengue.objects.annotate(
        year=ExtractYear('Date')
    ).values('year').annotate(
        total_cases=Sum('Cases'),
        total_deaths=Sum('Deaths')
    )

    total_yearly_cases = {}

    year_label = []
    year_cases = []
    year_deaths = []

    total_cases = 0
    total_deaths = 0
    for year_data in years_data:
        year_label.append(year_data['year'])
        year_cases.append(year_data['total_cases'])
        year_deaths.append(year_data['total_deaths'])

         # Accumulate total cases and deaths
        total_cases += year_data['total_cases']
        total_deaths += year_data['total_deaths']

        # Add to total_yearly_cases dictionary
        total_yearly_cases[year_data['year']] = {
            'cases': year_data['total_cases'],
            'deaths': year_data['total_deaths'],
        }

    total_yearly_cases_json = json.dumps(total_yearly_cases)


    # Get total cases for the year 2021
    total_cases_2021 = Dengue.objects.filter(Date__year=2021).aggregate(Sum('Cases'))['Cases__sum'] or 0
    total_deaths_2021 = Dengue.objects.filter(Date__year=2021).aggregate(Sum('Deaths'))['Deaths__sum'] or 0

 # Get dengue cases and deaths for each location within a specific region
    all_regions_data = {}
    for region_name in region_label:
        region_data = Dengue.objects.filter(Region=region_name).values('Location').annotate(
            total_cases=Sum('Cases'),
            total_deaths=Sum('Deaths')
        ).order_by('Location')

        locations = []
        cases = []
        deaths = []

        for data in region_data:
            locations.append(data['Location'])
            cases.append(data['total_cases'])
            deaths.append(data['total_deaths'])

        all_regions_data[region_name] = {
            'label': locations,
            'cases': cases,
            'deaths': deaths,
        }
    all_regions_data_json = json.dumps(all_regions_data)

    # Get cases by region for each year


    region_yearly_data = Dengue.objects.annotate(
        year=ExtractYear('Date')
    ).values('year', 'Region').annotate(
        total_cases=Sum('Cases'),
        total_deaths=Sum('Deaths')
    ).order_by('-total_cases')
    
    region_yearly_cases = {}
    for region_year_data in region_yearly_data:
        year = region_year_data['year']
        region = region_year_data['Region']
        cases = region_year_data['total_cases']

    # Initialize dictionary for the year if not already present
        if year not in region_yearly_cases:
            region_yearly_cases[year] = {}

        region_yearly_cases[year][region] = cases
    region_yearly_cases_json = json.dumps(region_yearly_cases)



    monthly_data = Dengue.objects.annotate(
        year=ExtractYear('Date'),
        month=ExtractMonth('Date')
        ).values('year', 'month').annotate(
        total_cases=Sum('Cases'),
                total_deaths=Sum('Deaths')
            ).order_by('month')

    monthly_cases = {}
    for data in monthly_data:
        year = data['year']
        month = data['month']
        cases = data['total_cases']

        if year not in monthly_cases:
            monthly_cases[year] = {}

        monthly_cases[year][month] = cases

    monthly_cases_json = json.dumps(monthly_cases)

    return render(request, 'index.html',
                   {'dengue_data': dengue_data,'region_label': region_label, 'region_cases': region_cases, 'region_deaths': region_deaths,
                    'year_label': year_label, 'year_cases': year_cases, 'year_deaths':year_deaths,
                      'total_cases': total_cases, 'total_deaths': total_deaths, 'total_cases_2021': total_cases_2021, 
                    'total_deaths_2021': total_deaths_2021, 'all_regions_data': all_regions_data, 'region_yearly_cases_json': region_yearly_cases_json,
                      'all_regions_data_json': all_regions_data_json, 'monthly_cases_json': monthly_cases_json,
                    'total_yearly_cases_json': total_yearly_cases_json,
                    })



def education_base(request):
    return render(request, "project3/proj3_base.html")


def education_datavis(request):
    return render(request, "project3/proj3_datavisualization.html")


def education_dataset(request):
    return render(request, "project3/proj3_dataset.html")

def education_model_view(request):
    # Query all objects from the "education_dataset" database
    objective = Education.objects.using('education_dataset').all()

    # Calculate the total entries for each gender
    total_male = objective.filter(gender='Boy').count()
    total_female = objective.filter(gender='Girl').count()

    # Pass the counts to the template
    context = {
        'total_male': total_male,
        'total_female': total_female,
    }
    
    return render(request, 'project3/proj3_base.html', context)