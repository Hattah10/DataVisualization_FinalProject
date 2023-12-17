
let line = document.querySelector("#linechart");
line.height = 200;

let linechart = new Chart(line, {
    type: "line",
    data: {
        labels:{{ year_label|safe }} ,
        datasets: [
            {
                label: "Case",
                borderColor: "orange",
                borderWidth: "3",
                backgroundColor: "rgba(235, 247, 245, 0.5)",
                data: {{ year_cases|safe }}
            },

            {
                label: "Death",
                borderColor: "red",
                borderWidth: "3",
                backgroundColor: "rgba(235, 247, 245, 0.5)",
                data:{{ year_deaths|safe }},
                pointBackgroundColor: 'red', // Set the point color
                pointBorderColor: 'black', // Set the point border color
                pointRadius: 5, // Set the point radius
                pointHoverRadius: 7, // Set the point hover radius
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            datalabels: {
                display: 'auto',
                color: 'black',
                align: 'top',
                anchor: 'end'
            }
        }
    }
});



    var ctxRegion = document.getElementById('regioncharts').getContext('2d');
            var regionChart;

            function updateRegionChart() {
                var selectedRegion = document.getElementById('regionSelector').value;

                // Parse the JSON data
                var allRegionsData = JSON.parse("{{ all_regions_data_json|safe }}");

                // Use the selected region's data for the chart
                var selectedRegionData = {
                    label: allRegionsData[selectedRegion].label,
                    cases: allRegionsData[selectedRegion].cases,
                    deaths: allRegionsData[selectedRegion].deaths
                };

                 // Update the title with the selected region
                 document.getElementById('regionTitle').innerText = 'Dengue Cases in ' + selectedRegion;

                // Destroy existing chart (if any)
                if (regionChart) {
                    regionChart.destroy();
                }

                // Create a new chart with the selected region's data
                regionChart = new Chart(ctxRegion, {
                    type: 'bar',
                    data: {
                        labels: selectedRegionData.label,
                        datasets: [
                            {
                                label: 'Cases',
                                data: selectedRegionData.cases,
                                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                                borderColor: 'rgba(75, 192, 192, 1)',
                                borderWidth: 1
                            },
                            {
                                label: 'Deaths',
                                data: selectedRegionData.deaths,
                                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                borderColor: 'rgba(255, 99, 132, 1)',
                                borderWidth: 1
                            }
                        ]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }

            // Call the updateRegionChart function on page load
            updateRegionChart();

