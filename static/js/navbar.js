const Navbar = {
    init() {
        this.cache();
        this.bindEvents();
        this.initClock();
        this.initKeyboard();
        this.initTooltips();
    },

    cache() {
        this.searchInput = document.getElementById("globalSearchInput");
        this.themeToggle = document.getElementById("themeToggle");
        this.navbarDate = document.getElementById("navbarDate");
        this.navbarTime = document.getElementById("navbarTime");
    },

    bindEvents() {
        if (this.themeToggle) this.themeToggle.addEventListener("click", toggleTheme);
    },

    initClock() {
        if (!this.navbarTime) return;
        const update = () => {
            const now = new Date();
            if (this.navbarDate) this.navbarDate.textContent = now.toLocaleDateString('en-US', {weekday:'short', month:'short', day:'numeric'});
            this.navbarTime.textContent = now.toLocaleTimeString('en-US', {hour:'numeric', minute:'2-digit', hour12:true});
        };
        update();
        setInterval(update, 1000);
    },

    initKeyboard() {
        document.addEventListener("keydown", e => {
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
                e.preventDefault();
                this.searchInput?.focus();
            }
        });
    },

    initTooltips() {
        if (typeof bootstrap !== "undefined") {
            document.querySelectorAll('[title]').forEach(el => new bootstrap.Tooltip(el));
        }
    }
};

document.addEventListener("DOMContentLoaded", () => Navbar.init());