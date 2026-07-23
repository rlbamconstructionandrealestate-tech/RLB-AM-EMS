/* =====================================================
   RLB-AM EMS V6.1
   ENTERPRISE SIDEBAR CONTROLLER
   sidebar.js - Stabilized
===================================================== */

document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("sidebarToggle");
    const closeBtn = document.getElementById("sidebarClose");
    const collapseBtn = document.querySelector(".sidebar-collapse");

    if (!sidebar) return;

    console.log("%c📋 RLB-AM EMS Sidebar Ready", "color:#2563eb;font-weight:700;");

    initMobileSidebar();
    initDesktopCollapse();
    initActiveLinks();
    initTooltips();

    // =====================================================
    // MOBILE SIDEBAR
    // =====================================================
    function initMobileSidebar() {
        if (toggleBtn) {
            toggleBtn.addEventListener("click", (e) => {
                e.stopPropagation();
                sidebar.classList.toggle("show");
                createOverlay();
            });
        }

        if (closeBtn) {
            closeBtn.addEventListener("click", closeMobileSidebar);
        }

        // Close on outside click
        document.addEventListener("click", (e) => {
            if (window.innerWidth <= 992) {
                if (!sidebar.contains(e.target) && !toggleBtn?.contains(e.target)) {
                    closeMobileSidebar();
                }
            }
        });
    }

    function closeMobileSidebar() {
        sidebar.classList.remove("show");
        removeOverlay();
    }

    // =====================================================
    // DESKTOP COLLAPSE
    // =====================================================
    function initDesktopCollapse() {
        if (!collapseBtn) return;

        collapseBtn.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
            document.body.classList.toggle("sidebar-collapsed");
            saveSidebarState();
        });
    }

    // =====================================================
    // RESTORE COLLAPSE STATE
    // =====================================================
    function restoreSidebarState() {
        const saved = localStorage.getItem("sidebar-state");
        if (saved === "collapsed") {
            sidebar.classList.add("collapsed");
            document.body.classList.add("sidebar-collapsed");
        }
    }

    function saveSidebarState() {
        const state = sidebar.classList.contains("collapsed") ? "collapsed" : "expanded";
        localStorage.setItem("sidebar-state", state);
    }

    // =====================================================
    // ACTIVE MENU LINKS
    // =====================================================
    function initActiveLinks() {
        const currentPath = window.location.pathname;

        document.querySelectorAll(".sidebar-nav a").forEach(link => {
            if (link.href.includes(currentPath) && currentPath !== "/") {
                link.classList.add("active");
            }

            link.addEventListener("click", () => {
                document.querySelectorAll(".sidebar-nav a").forEach(item => {
                    item.classList.remove("active");
                });
                link.classList.add("active");
            });
        });
    }

    // =====================================================
    // TOOLTIPS
    // =====================================================
    function initTooltips() {
        if (typeof bootstrap === "undefined") return;

        document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
            new bootstrap.Tooltip(el);
        });
    }

    // =====================================================
    // OVERLAY HELPERS
    // =====================================================
    function createOverlay() {
        if (document.querySelector(".sidebar-overlay")) return;

        const overlay = document.createElement("div");
        overlay.className = "sidebar-overlay";
        document.body.appendChild(overlay);

        overlay.addEventListener("click", closeMobileSidebar);
    }

    function removeOverlay() {
        const overlay = document.querySelector(".sidebar-overlay");
        if (overlay) overlay.remove();
    }

    // Initialize saved state
    restoreSidebarState();
});

window.Sidebar = { init: () => {} }; // For potential future use