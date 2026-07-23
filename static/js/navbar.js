/* =====================================================
   RLB-AM EMS V6.1
   ENTERPRISE NAVBAR CONTROLLER
   navbar.js
===================================================== */

const Navbar = {

    init() {
        this.cacheElements();
        this.bindEvents();
        this.initLiveClock();
        this.initKeyboardShortcuts();
        this.initTooltips();
    },

    cacheElements() {
        this.sidebarToggle = document.getElementById("sidebarToggle");
        this.globalSearchInput = document.getElementById("globalSearchInput");
        this.navbarDate = document.getElementById("navbarDate");
        this.navbarTime = document.getElementById("navbarTime");
    },

    bindEvents() {
        // Sidebar Toggle
        if (this.sidebarToggle) {
            this.sidebarToggle.addEventListener("click", () => {
                const sidebar = document.getElementById("sidebar");
                if (sidebar) sidebar.classList.toggle("show");
            });
        }

        // Global Search
        if (this.globalSearchInput) {
            this.globalSearchInput.addEventListener("keypress", (e) => {
                if (e.key === "Enter") {
                    const query = this.globalSearchInput.value.trim();
                    if (query) {
                        window.showToast?.(`Searching for: "${query}"`, "primary");
                        // Add your search logic here
                    }
                }
            });
        }
    },

    // =====================================================
    // LIVE CLOCK
    // =====================================================
    initLiveClock() {
        if (!this.navbarTime) return;

        const updateClock = () => {
            const now = new Date();

            // Date
            if (this.navbarDate) {
                this.navbarDate.textContent = now.toLocaleDateString('en-US', {
                    weekday: 'short',
                    month: 'short',
                    day: 'numeric'
                });
            }

            // Time
            this.navbarTime.textContent = now.toLocaleTimeString('en-US', {
                hour: 'numeric',
                minute: '2-digit',
                hour12: true
            });
        };

        updateClock();
        setInterval(updateClock, 1000);
    },

    // =====================================================
    // KEYBOARD SHORTCUTS
    // =====================================================
    initKeyboardShortcuts() {
        document.addEventListener("keydown", (e) => {
            // Ctrl/Cmd + K → Focus Search
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
                e.preventDefault();
                if (this.globalSearchInput) {
                    this.globalSearchInput.focus();
                    this.globalSearchInput.select();
                }
            }
        });
    },

    // =====================================================
    // TOOLTIPS
    // =====================================================
    initTooltips() {
        if (typeof bootstrap === "undefined") return;

        document.querySelectorAll('[title]').forEach(el => {
            new bootstrap.Tooltip(el, { placement: "bottom" });
        });
    }
};

// Auto-initialize
document.addEventListener("DOMContentLoaded", () => {
    Navbar.init();
});

window.Navbar = Navbar;