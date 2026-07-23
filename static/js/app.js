/* =====================================================
   RLB-AM EMS V6.1
   ENTERPRISE CORE JAVASCRIPT
   app.js - Stabilized & Optimized
===================================================== */

document.addEventListener("DOMContentLoaded", () => {
    console.log("%cRLB-AM EMS V6.1 Loaded Successfully", "color:#2563eb;font-weight:800;font-size:13px");

    initLoader();
    initTheme();
    initNavbar();
    initSearch();
    initTooltips();
    initPasswordToggle();
    initDeleteConfirm();
    initMessages();
    initCounters();
    initClock();
    initActiveMenu();
    initFullscreen();
});

/* =====================================================
   PAGE LOADER
===================================================== */

function initLoader() {
    const loader = document.getElementById("page-loader");
    if (!loader) return;

    window.addEventListener("load", () => {
        setTimeout(() => {
            loader.classList.add("hide");
        }, 280);
    });
}

function showLoader() {
    const loader = document.getElementById("page-loader");
    if (loader) loader.classList.remove("hide");
}

window.showLoader = showLoader;

/* =====================================================
   THEME SYSTEM
===================================================== */

function initTheme() {
    const savedTheme = localStorage.getItem("rlbam-theme");
    if (savedTheme) {
        document.documentElement.setAttribute("data-bs-theme", savedTheme);
    }
}

function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute("data-bs-theme");
    const nextTheme = current === "dark" ? "light" : "dark";

    html.setAttribute("data-bs-theme", nextTheme);
    localStorage.setItem("rlbam-theme", nextTheme);
}

window.toggleTheme = toggleTheme;

/* =====================================================
   NAVBAR & SIDEBAR
===================================================== */

function initNavbar() {
    // Theme toggle is handled in base.html
    const sidebarToggle = document.getElementById("sidebarToggle");
    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", () => {
            document.getElementById("sidebar").classList.toggle("show");
        });
    }
}

/* =====================================================
   GLOBAL SEARCH
===================================================== */

function initSearch() {
    const searchInput = document.getElementById("globalSearchInput");
    if (!searchInput) return;

    searchInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            const value = searchInput.value.trim();
            if (value) {
                showToast(`Searching for: ${value}`, "primary");
                // Add actual search logic here
            }
        }
    });
}

/* =====================================================
   TOOLTIPS
===================================================== */

function initTooltips() {
    if (typeof bootstrap === "undefined") return;

    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
        new bootstrap.Tooltip(el);
    });
}

/* =====================================================
   PASSWORD TOGGLE
===================================================== */

function initPasswordToggle() {
    document.querySelectorAll(".toggle-password").forEach(btn => {
        btn.addEventListener("click", () => {
            const input = btn.closest(".input-group")?.querySelector("input");
            if (input) {
                input.type = input.type === "password" ? "text" : "password";
            }
        });
    });
}

/* =====================================================
   DELETE CONFIRMATION
===================================================== */

function initDeleteConfirm() {
    document.querySelectorAll(".delete-confirm").forEach(btn => {
        btn.addEventListener("click", (e) => {
            if (!confirm("Are you sure you want to delete this item?")) {
                e.preventDefault();
            }
        });
    });
}

/* =====================================================
   AUTO-HIDE MESSAGES
===================================================== */

function initMessages() {
    setTimeout(() => {
        document.querySelectorAll(".alert").forEach(alert => {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";

            setTimeout(() => alert.remove(), 600);
        });
    }, 5000);
}

/* =====================================================
   ACTIVE MENU HIGHLIGHT
===================================================== */

function initActiveMenu() {
    const currentPath = window.location.pathname;
    document.querySelectorAll(".sidebar-nav a").forEach(link => {
        if (link.href.includes(currentPath) && currentPath !== "/") {
            link.classList.add("active");
        }
    });
}

/* =====================================================
   LIVE CLOCK
===================================================== */

function initClock() {
    const dateEl = document.getElementById("navbarDate");
    const timeEl = document.getElementById("navbarTime");

    if (!timeEl) return;

    function updateClock() {
        const now = new Date();
        
        if (dateEl) {
            dateEl.textContent = now.toLocaleDateString('en-US', { 
                weekday: 'short', 
                month: 'short', 
                day: 'numeric' 
            });
        }
        
        timeEl.textContent = now.toLocaleTimeString('en-US', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
    }

    updateClock();
    setInterval(updateClock, 1000);
}

/* =====================================================
   FULLSCREEN
===================================================== */

function initFullscreen() {
    const btn = document.getElementById("fullscreenToggle");
    if (!btn) return;

    btn.addEventListener("click", () => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
            btn.innerHTML = `<i class="bi bi-fullscreen-exit"></i>`;
        } else {
            document.exitFullscreen();
            btn.innerHTML = `<i class="bi bi-arrows-fullscreen"></i>`;
        }
    });
}

/* =====================================================
   TOAST SYSTEM
===================================================== */

function showToast(message, type = "primary") {
    const toastContainer = document.querySelector(".toast-container") || createToastContainer();
    
    const toast = document.createElement("div");
    toast.className = `toast align-items-center text-bg-${type} border-0`;
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;

    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast, { delay: 4500 });
    bsToast.show();

    toast.addEventListener("hidden.bs.toast", () => toast.remove());
}

function createToastContainer() {
    const container = document.createElement("div");
    container.className = "toast-container position-fixed bottom-0 end-0 p-3";
    container.style.zIndex = "1100";
    document.body.appendChild(container);
    return container;
}

window.showToast = showToast;

/* =====================================================
   CSRF TOKEN
===================================================== */

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        document.cookie.split(";").forEach(cookie => {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            }
        });
    }
    return cookieValue;
}

window.csrfToken = getCookie("csrftoken");