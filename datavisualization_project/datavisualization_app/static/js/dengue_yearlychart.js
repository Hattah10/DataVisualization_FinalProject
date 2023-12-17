
// Monthly chart
var ctxMonthly = document.getElementById('monthly_chart').getContext('2d');
// ctxMonthly.height = 200;
// ctxMonthly.width = 200;
var monthlyChart;
var monthlyCases = JSON.parse('{{ monthly_cases_json|escapejs|safe }}');

// Yearly region chart
var ctxYearRegion = document.getElementById('year_regionchart');
ctxYearRegion.height = 320;
ctxYearRegion.width = 300;



var yearRegionChart;
var regionYearlyCases = JSON.parse('{{ region_yearly_cases_json|escapejs|safe }}');

console.log('Monthly Cases:', monthlyCases);
console.log('Region Yearly Cases:', regionYearlyCases);
console.log('Total Yearly Cases:', totalYearlyCases);
// Total yearly chart
var ctxTotalYear = document.getElementById('total_year_chart').getContext('2d');
ctxTotalYear.height = 200;
ctxTotalYear.width = 200;
var totalYearChart;
var totalYearlyCases = JSON.parse('{{ total_yearly_cases_json|escapejs|safe }}');

YearlyChart();

// Function to update both charts
function YearlyChart() {
    var selectedYear = document.getElementById('chartSelector').value;

    document.getElementById('monthly_title').innerText = selectedYear + ' Trends in Dengue Incidents';

    // Update monthly chart
    var selectedYearDataMonthly = monthlyCases[selectedYear];
    if (monthlyChart) {
        monthlyChart.destroy();
    }
    monthlyChart = new Chart(ctxMonthly, {
        type: 'bar',
        data: {
            labels: Object.keys(selectedYearDataMonthly),
            datasets: [
                {
                    label: 'Dengue Cases',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: Object.values(selectedYearDataMonthly),
                },
            ],
        }, 
        options: {

          maintainAspectRatio: false, // Set to false to control the height manually
        aspectRatio: 2,
            responsive: true,

            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false, // Hide grid lines for the x-axis
                    },
                },
                x: {
                    grid: {
                        display: false, // Hide grid lines for the x-axis
                    },
                },
            },

              plugins: {
          datalabels: {
            anchor: 'end',
            align: 'end',
            labels: {
              value: {
                color: 'black'
                          }
                        }

                  }
                },
        },

        plugins: [ChartDataLabels]
    });

    // Update yearly region chart
    var selectedYearDataRegion = regionYearlyCases[selectedYear];

    if (yearRegionChart) {
        yearRegionChart.destroy();
    }
    yearRegionChart = new Chart(ctxYearRegion, {
        type: 'bar',
        data: {
            labels: Object.keys(selectedYearDataRegion),
            datasets: [
                {
                    label: 'Dengue Cases',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: Object.values(selectedYearDataRegion)
                },
            ],
        },
            options: {
              
            responsive: true,
            indexAxis: 'y',
            scales: {
                x: {
                    grid: {
                        display: false, // Hide grid lines for the x-axis
                    },
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false, // Hide grid lines for the y-axis
                    },
                },
            },

            plugins: {
        datalabels: {
          anchor: 'end',
          align: 'end',
          labels: {
            value: {
              color: 'black'
            }
          }

        }
      },
        }, 
        plugins: [ChartDataLabels]
    });

    //update total cases yearly 

    // Get data for the selected year
    var selectedYearData = totalYearlyCases[selectedYear];

    var prevYear = getPrevYear(selectedYear);

      if (totalYearlyCases[prevYear]) {
        document.getElementById('stat_box').style.display = 'block';

          var prevYearData = totalYearlyCases[prevYear];

          // Calculate the percentage change for Dengue cases
          var dengueCasesPercentageChange = calculatePercentageChange(selectedYearData.cases, prevYearData.cases);
          var deathPercentageChange = calculatePercentageChange(selectedYearData.deaths, prevYearData.deaths);
          // Check the sign of the percentage change
          if (dengueCasesPercentageChange > 0) {

                document.getElementById('caseChange')
                .innerHTML =  dengueCasesPercentageChange.toFixed(0) + "% <i class='bx bx-trending-up' style='color: green;' ></i>";
                console.log("Percentage Increase in Dengue Cases: " + dengueCasesPercentageChange + "%");
            } else if (dengueCasesPercentageChange < 0) {
                
              document.getElementById('caseChange')
                .innerHTML = Math.abs(dengueCasesPercentageChange).toFixed(0) + "% <i class='bx bx-trending-down' style='color: red;'></i>";
                
              console.log("Percentage Decrease in Dengue Cases: " + Math.abs(dengueCasesPercentageChange) + "%");
            } else {
                console.log("No Change in Dengue Cases");
            }  

            // death display
            if (deathPercentageChange > 0) {

                  document.getElementById('deathChange')
                  .innerHTML = deathPercentageChange.toFixed(0) + "% <i class='bx bx-trending-up' style='color: green;' ></i>";
                  console.log("Percentage Increase in Death Cases: " + deathPercentageChange + "%");
              } else if (deathPercentageChange < 0) {
                      document.getElementById('deathChange')
                      .innerHTML = "" + Math.abs(deathPercentageChange).toFixed(0) + "% <i class='bx bx-trending-down' style='color: red;'></i>";
                      console.log("Percentage decrease in Death Cases: " + deathPercentageChange + "%");
                    } else {
                     
                      console.log("No Change in Dengue Cases");
                  }  
                 
     } else {
      document.getElementById('stat_box').style.display = 'none';
      }

      // Function to calculate percentage change
      function calculatePercentageChange( newValue, oldValue) {
          return ((newValue - oldValue) / oldValue) * 100;
      }
     
      // Function to get the next year
      function getPrevYear(currentYear) {
          return currentYear - 1;
      }

    // Destroy existing chart (if any)
    if (totalYearChart) {
        totalYearChart.destroy();
    }

    // Create a new pie chart with the selected year's data
    totalYearChart = new Chart(ctxTotalYear, {
        type: 'doughnut',
        data: {
            labels: ['Cases', 'Deaths'],
            datasets: [
                {
                    data: [selectedYearData.cases, selectedYearData.deaths],
                    backgroundColor: ['rgb(255, 99, 132, 0.5)', 'rgb(54, 162, 235)'],
                    borderColor: ['orange', 'rgba(255, 99, 132, 1)'],
                    borderWidth: 1,
                },
            ],
        },
        options: {
          maintainAspectRatio: false,
            responsive: true,
  
        },
        plugins: [ChartDataLabels]
    });


    interpret(selectedYear);

    function interpret(year){
      if (year === '2016') {

        var interpretationText =
        "In 2016, there were 209,544 reported Dengue cases with 8,127 associated deaths. " +
        "The peak monthly incidence in August underscores the significance of targeted interventions. " +
        "Notably, Region 7 stood out with the highest Dengue incidence, emphasizing the necessity of focused attention on regional patterns for effective public health strategies.";

      document.getElementById('interpretation').innerText = interpretationText;
      }
      else if (year === '2017') {
        var interpretationText =
        "In 2017, both Dengue cases and related deaths saw a significant decline from the previous year, offering a positive trend. " +
        "The peak monthly incidence in August underscores the importance of targeted interventions. " +
        "Notably, NCR emerged with the highest Dengue incidence, emphasizing the need for focused attention on regional patterns for effective public health strategies.";
        document.getElementById('interpretation').innerText = interpretationText;
      
      }
      else if (year === '2018') {
        var interpretationText =
      "In 2018, there was a 63% increase in Dengue cases, marking a negative trend for this year. " +
      "However, associated deaths decreased by 73% from the previous year. " +
      "While, July, August, and September exhibited peak Dengue cases, highlighting the critical need for targeted interventions. " +
      "Notably, Central Luzon recorded the highest Dengue incidence in the Philippines during this year.";
      document.getElementById('interpretation').innerText = interpretationText;
 
    }

      else if (year === '2019') {
        var interpretationText =
      "In 2019, Dengue cases increased by 76%, indicating a significant rise compared to the previous year. " +
      "The associated death reports also increased by 41%. " +
      "August and September stood out as peak months for Dengue incidence, emphasizing the urgency of targeted interventions. " +
      "Calabarzon emerged as the region with the highest Dengue cases in this year.";
      document.getElementById('interpretation').innerText = interpretationText;
  
      }
      else if (year === '2020') {
        var interpretationText =
      "In 2020, there was a remarkable 79% decrease in Dengue incidence, as well as a decrease in associated deaths, signifying a notable improvement from the previous year. " +
      "While, January and February were identified as the peak months for Dengue incidence, necessitating heightened vigilance during this period. " +
      "Moreover, Central Luzon reported the highest Dengue cases, indicating a regional focus for public health strategies.";
      document.getElementById('interpretation').innerText = interpretationText;
  
      }
      else {
        var interpretationText =
          "In 2021, only January captured Dengue cases, totaling 2,087 with 8 reported deaths. " +
          "Central Luzon emerged as the region with the highest Dengue incidence for this month, emphasizing the need for continued monitoring and intervention.";
         document.getElementById('interpretation').innerText = interpretationText;
  
      }
    }


}

// Call the updateChart function on page load
