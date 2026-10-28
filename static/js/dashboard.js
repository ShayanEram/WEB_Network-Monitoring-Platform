async function loadStats() {
  // Fetch stats
}

async function loadDevices() {
  // Fetch devices
}

async function loadProtocols() {
  // Fetch chart data
}

function refreshDashboard() {
  loadStats();
  loadDevices();
  loadProtocols();
}

refreshDashboard();

setInterval(refreshDashboard, 5000);
