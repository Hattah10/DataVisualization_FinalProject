
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
arrow[i].addEventListener("click", (e)=>{
let arrowParent = e.target.parentElement.parentElement; //selecting main parent of arrow
arrowParent.classList.toggle("showMenu");
});
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-category");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", ()=>{
sidebar.classList.toggle("close");
});

let ctx = document.querySelector("#registrationChart");
ctx.height = 200;

let line = document.querySelector("#linechart");
line.height = 200;

let linechart = new Chart(line, {
    type: "line",
    data: {
        labels: year_label,
        datasets: [
            {
                label: "Case",
                borderColor: "orange",
                borderWidth: "3",
                backgroundColor: "rgba(235, 247, 245, 0.5)",
                data: year_cases|safe
            },

            {
                label: "Death",
                borderColor: "red",
                borderWidth: "3",
                backgroundColor: "rgba(235, 247, 245, 0.5)",
                data: year_deaths|safe
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: {
              beginAtZero: true
            }
          }
    }
});

// //  const ctx = document.getElementById('myChart');
// new Chart(ctx, {
//     type: 'bar',
//     data: {
//     labels: {{ region_label|safe }},
//     datasets: [{
//                 label: "Dengue Cases",
//                 borderColor: "orange",
//                 borderWidth: "3",
//                 backgroundColor: "rgba(235, 247, 245, 0.5)",
//                 data:  {{ region_cases|safe }}
//             },

//             {
//                 label: "Death",
//                 borderColor: "red",
//                 borderWidth: "3",
//                 backgroundColor: "rgba(235, 247, 245, 0.5)",
//                 data:  {{ region_deaths|safe }}
//             }]
//     },
//     options: {
//     responsive: true,
//     scales: {
//         y: {
//         beginAtZero: true
//         }
//     }
//     }
// });


// let pie = document.querySelector("#piechart");
// line.height = 200;

// let piechart = new Chart(pie, {
//     type: "pie",
//     data: {
//         labels: {{ year_label|safe }},
//         datasets: [
//             {
//                 label: "Case",
//                 backgroundColor: [
//                     'rgb(255, 99, 132, 0.5)',
//                     'rgb(54, 162, 235)',
//                     'rgb(255, 205, 86)'
//                     ],
//                 hoverOffset: 4,
//                 data: {{ year_cases|safe }}
//             }
//         ]
//     },
//     options: {
//         responsive: true,
//     }
// });

