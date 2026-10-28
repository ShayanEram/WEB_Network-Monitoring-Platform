async function loadStats() {
  const response = await fetch('/api/stats');
  const data = await response.json();

  document.getElementById('packets').textContent = `Packets: ${data.packets}`;

  document.getElementById('devices-count').textContent = `Devices: ${data.devices}`;

  document.getElementById('protocol').textContent = `Top Protocol: ${data.top_protocol}`;
}

async function loadDevices() {
  const response = await fetch('/api/devices');
  const devices = await response.json();

  const tbody = document.querySelector('#device-table tbody');

  tbody.innerHTML = '';

  devices.forEach((device) => {
    tbody.innerHTML += `
        <tr>
            <td>${device.ip}</td>
            <td>${device.hostname}</td>
            <td>${device.last_seen}</td>
        </tr>
    `;
  });
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
