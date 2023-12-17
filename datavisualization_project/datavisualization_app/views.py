from django.shortcuts import render, redirect
from datavisualization_app.models import Dengue
from datavisualization_app.models import Education
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear, ExtractMonth
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token

from django.contrib.auth.models import User

from django.contrib import messages
from calendar import month_name

# from django.http import HttpResponse



# def index(request):
#     labels = []
#     data = []

#     queryset = Dengue.objects.all()[:4]
#     for dataset in queryset:
#         labels.append(dataset.Location)
#         data.append(dataset.Cases)
#     return render(request, 'index.html', {'labels': labels, 'data': data})
# @login_required 
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
        region_data = Dengue.objects.filter(Region=region_name).values('Location', 'Date').annotate(
            total_cases=Sum('Cases'),
            total_deaths=Sum('Deaths')
        ).order_by('Location', 'Date')

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
         # Convert numeric month to month name
        month_name_str = month_name[month]
        monthly_cases[year][month_name_str] = cases

    monthly_cases_json = json.dumps(monthly_cases)


    return render(request, 'dengue.html',
                   {'dengue_data': dengue_data,'region_label': region_label, 'region_cases': region_cases, 'region_deaths': region_deaths,
                    'year_label': year_label, 'year_cases': year_cases, 'year_deaths':year_deaths,
                      'total_cases': total_cases, 'total_deaths':total_deaths, 'total_deaths': total_deaths, 'total_cases_2021': total_cases_2021, 
                    'total_deaths_2021': total_deaths_2021, 'all_regions_data': all_regions_data, 'region_yearly_cases_json': region_yearly_cases_json,
                       'monthly_cases_json': monthly_cases_json,
                    'total_yearly_cases_json': total_yearly_cases_json,
                    })


####################################################################


def education_model_view(request):
    # Query all objects from the "education_dataset" database
    education_data = Education.objects.all()

    # Calculate the total entries
    education_report = Education.objects.all().count()
    total_male = Education.objects.filter(gender='Boy').count()
    total_female = Education.objects.filter(gender='Girl').count()

    # starting point of graph
    # total adaptability of students
    adapt_low = Education.objects.filter(adaptivity_level='Low').count()
    adapt_mod = Education.objects.filter(adaptivity_level='Moderate').count()
    adapt_high = Education.objects.filter(adaptivity_level='High').count()

    adapt_low = int(adapt_low)
    adapt_mod = int(adapt_mod)
    adapt_high = int(adapt_high)

    adapt_bins = ['Low', 'Moderate', 'High']
    adapt_lists = [adapt_low, adapt_mod, adapt_high]

    # Internet Type | Students
    network_2g = Education.objects.filter(network_type='2G').count()
    network_3g = Education.objects.filter(network_type='3G').count()
    network_4g = Education.objects.filter(network_type='4G').count()
    
    network_2g = int(network_2g)
    network_3g = int(network_3g)
    network_4g = int(network_4g)

    network_label = ['2G', '3G', '4G']
    network_lists = [network_2g, network_3g, network_4g]
    
    # Condition of students
    rich = Education.objects.filter(financial_condition='Rich').count()
    mid = Education.objects.filter(financial_condition='Mid').count()
    poor = Education.objects.filter(financial_condition='Poor').count()
    
    rich = int(rich)
    mid = int(mid)
    poor = int(poor)
    
    cond_label = ['Rich', 'Mid', 'Poor']
    cond_lists = [rich, mid, poor]
    
    
    # count of each education level
    educ_univ = Education.objects.filter(education_level='University').count()
    educ_col = Education.objects.filter(education_level='College').count()
    educ_sch = Education.objects.filter(education_level='School').count()
    
    educ_univ = int(educ_univ)
    educ_col = int(educ_col)
    educ_sch = int(educ_sch)
    
    educ_label = ['University', 'College', 'School']
    educ_lists = [educ_univ, educ_col, educ_sch]
    
    # learning management system
    NO = Education.objects.filter(self_lms='No').count()
    YES = Education.objects.filter(self_lms='Yes').count()
    
    NO = int(NO)
    YES = int(YES)
    
    lms_label = ['No', 'Yes']
    lms_lists = [NO, YES]

    # educ_data = Education.objects.values('adaptivity_level').annotate(
    #     total_level=Sum('education_level'),
    #     total_lms=Sum('self_lms')
    # ).order_by('adaptivity_level')

    # educ_label = []
    # educ_level = []
    # educ_lms = []

    # for educ_data in educ_data:
    #     educ_label.append(educ_data['adaptivity_level'])
    #     educ_level.append(educ_data['total_level'])
    #     educ_lms.append(educ_data['total_lms'])
    
    
    
    # education_counts = Education.objects.values('education_level', 'self_lms').annotate(count=Count('id'))

    # # Prepare data for the chart
    # education_levels = set(data['education_level'] for data in education_counts)
    # lms = set(data['self_lms'] for data in education_counts)

    # chart_data = {education: {self_lms: 0 for self_lms in lms} for education in education_levels}
    # # for data in education_counts:
    #     education_level = data['education_level']
    #     self_lms = data['self_lms']
    #     count = data['count']
    #     chart_data[education_level][self_lms] = count
    
    
    # # Calculate the count of each age and gender
    # age_gender_counts = Education.objects.values('age', 'gender').annotate(count=Count('id'))

    # # Prepare data for the pie chart
    # chart_data = {f"{data['age']} - {data['gender']}": data['count'] for data in age_gender_counts}
    
    # # Calculate the count of each education level and institution type
    # education_institution_counts = Education.objects.values('education_level', 'institution_type').annotate(count=Count('id'))

    # # Prepare data for the bar chart
    # chart_data = {f"{data['education_level']}": data['count'] for data in education_institution_counts}

    # Pass the counts to the template
    context = {
        'education_report': education_report,
        'education_data': education_data,
        'total_male': total_male,
        'total_female': total_female,
        # 'education_levels': list(education_levels),
        # 'lms': list(lms),
        # 'chart_data': json.dumps(chart_data),
        
        'network_label': network_label,
        'network_lists': network_lists,
        'adapt_bins': adapt_bins,
        'adapt_lists': adapt_lists,
        'cond_label': cond_label,
        'cond_lists': cond_lists,
        # 'educ_label': educ_label,
        # 'educ_level': educ_level,
        # 'educ_lms': educ_lms,
        'educ_label': educ_label,
        'educ_lists': educ_lists,
        'lms_label': lms_label,
        'lms_lists': lms_lists,
        
    }



 



    return render(request, 'education.html', context)


