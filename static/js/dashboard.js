/* =====================================================
   RLB-AM EMS V6.1
   ENTERPRISE DASHBOARD CONTROLLER
   dashboard.js - Stabilized
===================================================== */

document.addEventListener("DOMContentLoaded", function () {
    // Only run on dashboard pages
    if (!document.body.classList.contains("dashboard-page") && 
        !document.getElementById("revenueChart")) {
        return;
    }

    console.log("%c📊 RLB-AM Dashboard Initialized", "color:#2563eb;font-weight:800;font-size:14px");

    Dashboard.init();
});

const Dashboard = {

    init() {
        this.animateCards();
        this.animateCounters();
        this.initCharts();
        this.initQuickActions();
        this.initRefresh();
    },

    // =========================================
    // CARD ENTRANCE ANIMATION
    // =========================================
    animateCards() {
        const cards = document.querySelectorAll(".dashboard-card, .stat-card, .card");

        cards.forEach((card, index) => {
            card.style.opacity = "0";
            card.style.transform = "translateY(25px)";

            setTimeout(() => {
                card.style.transition = "all 0.6s cubic-bezier(0.4, 0, 0.2, 1)";
                card.style.opacity = "1";
                card.style.transform = "translateY(0)";
            }, index * 80);
        });
    },

    // =========================================
    // NUMBER COUNTERS
    // =========================================
    animateCounters() {
        const counters = document.querySelectorAll(".counter, .stat-value");

        counters.forEach(counter => {
            const text = counter.innerText.replace(/[^0-9.]/g, "");
            if (!text) return;

            const target = parseFloat(text);
            let current = 0;
            const increment = Math.ceil(target / 45);

            const timer = setInterval(() => {
                current += increment;

                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }

                // Format with commas for large numbers
                counter.innerText = Number(current).toLocaleString();
            }, 35);
        });
    },

    // =========================================
    // CHARTS (Revenue)
    // =========================================
    initCharts() {
        const canvas = document.getElementById("revenueChart");
        if (!canvas || typeof Chart === "undefined") return;

        new Chart(canvas, {
            type: "line",
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
                datasets: [{
                    label: "Monthly Revenue",
                    data: [12400000, 15800000, 9800000, 21300000, 18700000, 24500000, 0, 0],
                    borderColor: "#2563eb",
                    backgroundColor: "rgba(37, 99, 235, 0.1)",
                    borderWidth: 3,
                    tension: 0.4,
                    fill: true,
                    pointRadius: 4,
                    pointHoverRadius: 7
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: "#0f172a",
                        padding: 12,
                        displayColors: false,
                        callbacks: {
                            label: (ctx) => "TZS " + Number(ctx.raw).toLocaleString()
                        }
                    }
                },
                scales: {
                    x: { grid: { display: false } },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: (value) => "TZS " + Number(value / 1000000) + "M"
                        }
                    }
                }
            }
        });
    },

    // =========================================
    // QUICK ACTIONS
    // =========================================
    initQuickActions() {
        document.querySelectorAll(".action-card, .quick-card").forEach(card => {
            card.addEventListener("mouseenter", () => {
                card.style.transform = "translateY(-6px)";
            });

            card.addEventListener("mouseleave", () => {
                card.style.transform = "translateY(0)";
            });
        });
    },

    // =========================================
    // REFRESH BUTTON
    // =========================================
    initRefresh() {
        const refreshBtn = document.querySelector("[data-refresh]");
        if (!refreshBtn) return;

        refreshBtn.addEventListener("click", () => {
            const originalText = refreshBtn.innerHTML;

            refreshBtn.innerHTML = `
                <i class="bi bi-arrow-repeat spin"></i> 
                Updating...
            `;
            refreshBtn.disabled = true;

            setTimeout(() => {
                refreshBtn.innerHTML = originalText;
                refreshBtn.disabled = false;
                this.toast("Dashboard refreshed successfully", "success");
            }, 1200);
        });
    },

    // =========================================
    // TOAST NOTIFICATION
    // =========================================
    toast(message, type = "success") {
        if (typeof window.showToast === "function") {
            window.showToast(message, type);
            return;
        }

        // Fallback toast
        const toast = document.createElement("div");
        toast.className = `alert alert-${type} position-fixed bottom-0 end-0 m-3 shadow`;
        toast.style.zIndex = "9999";
        toast.innerHTML = message;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.transition = "all 0.4s";
            toast.style.opacity = "0";
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    }
};

window.Dashboard = Dashboard;