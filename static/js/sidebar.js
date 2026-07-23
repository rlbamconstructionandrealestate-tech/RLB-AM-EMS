/* ==========================================================
   RLB-AM EMS V6.1
   ENTERPRISE SIDEBAR CONTROLLER
========================================================== */


document.addEventListener("DOMContentLoaded", function () {


    const sidebar = document.getElementById("sidebar");
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebarClose = document.getElementById("sidebarClose");


    if (!sidebar) {
        console.warn("Sidebar element not found");
        return;
    }


    console.log(
        "%cRLB-AM Sidebar Initialized",
        "color:#2563eb;font-weight:700;"
    );



    /* ======================================================
       DESKTOP SIDEBAR COLLAPSE
    ====================================================== */


    if (sidebarToggle) {


        sidebarToggle.addEventListener(
            "click",
            function () {


                const isMobile =
                    window.innerWidth <= 992;



                if (isMobile) {


                    sidebar.classList.toggle(
                        "show"
                    );


                } 
                else {


                    sidebar.classList.toggle(
                        "collapsed"
                    );


                    document.body.classList.toggle(
                        "sidebar-collapsed"
                    );



                    localStorage.setItem(
                        "sidebar-state",
                        sidebar.classList.contains("collapsed")
                        ?
                        "collapsed"
                        :
                        "expanded"
                    );


                }


            }
        );


    }



    /* ======================================================
       MOBILE CLOSE BUTTON
    ====================================================== */


    if (sidebarClose) {


        sidebarClose.addEventListener(
            "click",
            function () {


                sidebar.classList.remove(
                    "show"
                );


            }
        );


    }





    /* ======================================================
       RESTORE SIDEBAR STATE
    ====================================================== */


    const savedState =
        localStorage.getItem(
            "sidebar-state"
        );



    if (
        savedState === "collapsed"
        &&
        window.innerWidth > 992
    ) {


        sidebar.classList.add(
            "collapsed"
        );


        document.body.classList.add(
            "sidebar-collapsed"
        );


    }





    /* ======================================================
       ACTIVE MENU HIGHLIGHT
    ====================================================== */


    const currentPath =
        window.location.pathname;



    const menuLinks =
        document.querySelectorAll(
            ".sidebar-nav a"
        );



    menuLinks.forEach(
        function(link){


            const linkPath =
                new URL(
                    link.href
                ).pathname;



            if (
                linkPath === currentPath
            ) {


                link.classList.add(
                    "active"
                );


            }



            link.addEventListener(
                "click",
                function(){


                    menuLinks.forEach(
                        item =>
                        item.classList.remove(
                            "active"
                        )
                    );


                    this.classList.add(
                        "active"
                    );


                }
            );


        }
    );







    /* ======================================================
       CLOSE SIDEBAR WHEN CLICKING OUTSIDE (MOBILE)
    ====================================================== */


    document.addEventListener(
        "click",
        function(event){


            if(
                window.innerWidth <= 992
                &&
                sidebar.classList.contains("show")
            ){


                const clickedInside =
                    sidebar.contains(event.target);



                const clickedToggle =
                    sidebarToggle &&
                    sidebarToggle.contains(event.target);



                if(
                    !clickedInside
                    &&
                    !clickedToggle
                ){


                    sidebar.classList.remove(
                        "show"
                    );


                }


            }


        }
    );







    /* ======================================================
       WINDOW RESIZE HANDLER
    ====================================================== */


    window.addEventListener(
        "resize",
        function(){


            if(window.innerWidth > 992){


                sidebar.classList.remove(
                    "show"
                );


                if(
                    localStorage.getItem(
                        "sidebar-state"
                    )
                    ===
                    "collapsed"
                ){


                    sidebar.classList.add(
                        "collapsed"
                    );


                }


            }


        }
    );







    /* ======================================================
       BOOTSTRAP TOOLTIP SUPPORT
    ====================================================== */


    if(typeof bootstrap !== "undefined"){


        const tooltipElements =
            document.querySelectorAll(
                '[data-bs-toggle="tooltip"]'
            );



        tooltipElements.forEach(
            function(element){


                new bootstrap.Tooltip(
                    element
                );


            }
        );


    }





});