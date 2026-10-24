// dashboard.js

// Frontend behavior.

// Responsibilities:

// Call APIs
// Update charts
// Refresh data
// Show alerts

async function loadStats() {
    const response =
        await fetch("/api/stats");

    const stats =
        await response.json();

    cpuCard.textContent =
        stats.cpu_usage;
}