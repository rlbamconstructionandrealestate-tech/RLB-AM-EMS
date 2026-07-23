/* ==========================================================
   RLB-AM EMS V6.1
   PREMIUM DASHBOARD JAVASCRIPT
========================================================== */


/*
==========================================================
GLOBAL DASHBOARD INITIALIZATION
==========================================================
*/

document.addEventListener(
    "DOMContentLoaded",
    function(){


        initializeCharts();

        initializeCounters();

        initializeTooltips();

        initializeDashboardEffects();


    }
);





/*
==========================================================
CHART HANDLING
Supports:
- Owner Dashboard
- Director Dashboard
- Manager Dashboard
- Secretary Dashboard

Only creates charts if canvas exists.
==========================================================
*/


function initializeCharts(){



    const revenueCanvas =
        document.getElementById(
            "revenueChart"
        );



    if(revenueCanvas){


        let labels =
            JSON.parse(
                revenueCanvas.dataset.labels || "[]"
            );


        let values =
            JSON.parse(
                revenueCanvas.dataset.values || "[]"
            );



        new Chart(
            revenueCanvas,
            {


                type:"line",


                data:{


                    labels:labels,


                    datasets:[

                        {

                            label:
                            "Revenue Performance",


                            data:values,


                            borderWidth:3,


                            tension:.4,


                            fill:true,


                        }

                    ]

                },


                options:{


                    responsive:true,


                    maintainAspectRatio:false,


                    plugins:{


                        legend:{


                            display:true


                        }


                    },


                    scales:{


                        y:{


                            beginAtZero:true


                        }


                    }


                }


            }

        );

    }





    /*
    -----------------------------------------
    PROJECT STATUS CHART
    -----------------------------------------
    */


    const projectCanvas =
        document.getElementById(
            "projectChart"
        );



    if(projectCanvas){


        new Chart(

            projectCanvas,

            {


                type:"doughnut",


                data:{


                    labels:[

                        "Active",
                        "Completed",
                        "Pending"

                    ],


                    datasets:[

                        {

                            data:

                            [

                                projectCanvas.dataset.active || 0,

                                projectCanvas.dataset.completed || 0,

                                projectCanvas.dataset.pending || 0

                            ],


                            borderWidth:1

                        }

                    ]


                },


                options:{


                    responsive:true,


                    maintainAspectRatio:false


                }


            }

        );


    }







    /*
    -----------------------------------------
    EQUIPMENT STATUS CHART
    -----------------------------------------
    */


    const equipmentCanvas =
        document.getElementById(
            "equipmentChart"
        );



    if(equipmentCanvas){


        new Chart(

            equipmentCanvas,

            {


                type:"bar",


                data:{


                    labels:[

                        "Available",
                        "Rented",
                        "Maintenance"

                    ],


                    datasets:[

                        {


                            label:
                            "Equipment Status",


                            data:[


                                equipmentCanvas.dataset.available || 0,


                                equipmentCanvas.dataset.rented || 0,


                                equipmentCanvas.dataset.maintenance || 0,


                            ],


                            borderWidth:1


                        }

                    ]


                },


                options:{


                    responsive:true,


                    maintainAspectRatio:false


                }


            }


        );


    }



}









/*
==========================================================
NUMBER COUNTER ANIMATION
For KPI CARDS
==========================================================
*/


function initializeCounters(){



    const counters =
        document.querySelectorAll(
            "[data-counter]"
        );



    counters.forEach(

        counter=>{


            let target =
                Number(
                    counter.dataset.counter
                );



            let current = 0;


            let increment =
                Math.ceil(
                    target / 60
                );



            let timer =
                setInterval(

                    ()=>{


                        current += increment;



                        if(current >= target){


                            current = target;


                            clearInterval(timer);


                        }



                        counter.innerText =
                            current.toLocaleString();



                    },


                    20

                );


        }

    );


}









/*
==========================================================
BOOTSTRAP TOOLTIPS
==========================================================
*/


function initializeTooltips(){



    const tooltipTriggerList =
        document.querySelectorAll(

            '[data-bs-toggle="tooltip"]'

        );



    tooltipTriggerList.forEach(

        tooltipTriggerEl=>{


            new bootstrap.Tooltip(

                tooltipTriggerEl

            );


        }

    );


}









/*
==========================================================
DASHBOARD CARD EFFECTS
==========================================================
*/


function initializeDashboardEffects(){



    const cards =
        document.querySelectorAll(

            ".dashboard-card"

        );



    cards.forEach(

        card=>{


            card.addEventListener(

                "mouseenter",

                ()=>{


                    card.classList.add(
                        "active-card"
                    );


                }


            );



            card.addEventListener(

                "mouseleave",

                ()=>{


                    card.classList.remove(
                        "active-card"
                    );


                }

            );


        }

    );


}









/*
==========================================================
AUTO REFRESH SUPPORT
For live management dashboards
==========================================================
*/


function refreshDashboard(){


    window.location.reload();


}




/*
Optional:
Refresh every 5 minutes

Enable later if needed

setInterval(
    refreshDashboard,
    300000
);

*/


