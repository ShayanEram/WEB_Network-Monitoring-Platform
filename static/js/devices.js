class DeviceManager {
  constructor() {
    this.allDevices = [];
    this.init();
  }

  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.loadDevices();

      document
        .getElementById('device-search')
        .addEventListener('input', () => this.filterDevices());
      document
        .getElementById('status-filter')
        .addEventListener('change', () => this.filterDevices());
      document
        .getElementById('refresh-devices-btn')
        .addEventListener('click', () => this.loadDevices());
    });
  }

  async loadDevices() {
    try {
      const response = await fetch('/api/devices');
      this.allDevices = await response.json();
      this.renderDevices(this.allDevices);
    } catch (err) {
      console.error('Failed to load devices:', err);
      document.getElementById('devices-tbody').innerHTML =
        `<tr><td colspan="7" class="text-center text-danger">Error loading devices</td></tr>`;
    }
  }

  renderDevices(devices) {
    const tbody = document.getElementById('devices-tbody');
    if (!devices.length) {
      tbody.innerHTML = `<tr><td colspan="7" class="text-center">No active devices recorded</td></tr>`;
      return;
    }

    tbody.innerHTML = devices
      .map(
        (d) => `
            <tr>
                <td><span class="status-badge online">● Online</span></td>
                <td><strong>${d.ip}</strong></td>
                <td>${d.hostname || 'Unknown Device'}</td>
                <td><code>${d.mac || 'N/A'}</code></td>
                <td>${d.first_seen || 'N/A'}</td>
                <td>${d.last_seen || 'N/A'}</td>
                <td><button class="btn btn-secondary" style="padding: 0.25rem 0.5rem; font-size: 0.8rem;" onclick="alert('Inspecting endpoint: ${
                  d.ip
                }')">Inspect</button></td>
            </tr>
        `,
      )
      .join('');
  }

  filterDevices() {
    const query = document.getElementById('device-search').value.toLowerCase();
    const filtered = this.allDevices.filter((d) => {
      return (
        (d.ip && d.ip.toLowerCase().includes(query)) ||
        (d.hostname && d.hostname.toLowerCase().includes(query))
      );
    });
    this.renderDevices(filtered);
  }
}

//MAIN---------------------------------------------------------------------------------------------------------------------
new DeviceManager();
