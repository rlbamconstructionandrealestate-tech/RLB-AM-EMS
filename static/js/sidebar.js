document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("sidebarToggle");
    const closeBtn = document.getElementById("sidebarClose");

    if (!sidebar) return;

    console.log("%c📋 RLB-AM Sidebar Ready", "color:#2563eb;font-weight:700;");

    // Toggle Button (Desktop + Mobile)
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
            document.body.classList.toggle("sidebar-collapsed");
            localStorage.setItem("sidebar-state", sidebar.classList.contains("collapsed") ? "collapsed" : "expanded");
        });
    }

    // Close Button (Mobile)
    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            sidebar.classList.remove("show");
        });
    }

    // Restore collapsed state
    if (localStorage.getItem("sidebar-state") === "collapsed") {
        sidebar.classList.add("collapsed");
        document.body.classList.add("sidebar-collapsed");
    }

    // Active link highlighting
    const currentPath = window.location.pathname;
    document.querySelectorAll(".sidebar-nav a").forEach(link => {
        if (link.href.includes(currentPath) && currentPath !== "/") {
            link.classList.add("active");
        }
    });

    // Tooltips
    if (typeof bootstrap !== "undefined") {
        document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
            new bootstrap.Tooltip(el);
        });
    }
});