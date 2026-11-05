class DashboardManager {
  constructor() {
    this.protocolChartInstance = null;
    this.init();
  }

  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.fetchStats();
      this.fetchProtocolsChart();
      this.fetchRecentPreviews();

      // Auto-refresh dashboard telemetry every 5 seconds
      setInterval(() => {
        this.fetchStats();
        this.fetchProtocolsChart();
      }, 5000);
    });
  }

  async fetchStats() {
    try {
      const response = await fetch('/api/stats');
      const data = await response.json();
      document.getElementById('stat-packets').textContent = data.packets;
      document.getElementById('stat-devices').textContent = data.devices;
      document.getElementById('stat-bandwidth').textContent = data.bandwidth;
      document.getElementById('stat-protocol').textContent = data.top_protocol;
    } catch (err) {
      console.error('Failed to fetch dashboard stats:', err);
    }
  }

  async fetchProtocolsChart() {
    try {
      const response = await fetch('/api/protocols');
      const data = await response.json();

      const labels = Object.keys(data);
      const values = Object.values(data);
      const ctx = document.getElementById('protocolDistributionChart').getContext('2d');

      if (this.protocolChartInstance) {
        this.protocolChartInstance.data.labels = labels;
        this.protocolChartInstance.data.datasets[0].data = values;
        this.protocolChartInstance.update();
      } else {
        this.protocolChartInstance = new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: labels,
            datasets: [
              {
                data: values,
                backgroundColor: ['#38bdf8', '#f59e0b', '#22c55e', '#a855f7', '#ef4444'],
                borderWidth: 0,
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { color: '#94a3b8' } },
            },
          },
        });
      }
    } catch (err) {
      console.error('Failed to fetch protocol distribution:', err);
    }
  }

  async fetchRecentPreviews() {
    try {
      const devRes = await fetch('/api/devices');
      const devices = await devRes.json();
      const devTbody = document.getElementById('top-devices-tbody');
      devTbody.innerHTML =
        devices
          .slice(0, 5)
          .map(
            (d) => `
                <tr>
                    <td>${d.ip}</td>
                    <td>${d.hostname || 'Unknown'}</td>
                    <td>${d.last_seen || 'N/A'}</td>
                </tr>
            `,
          )
          .join('') || '<tr><td colspan="3" class="text-center">No devices found</td></tr>';

      const alertRes = await fetch('/api/alerts');
      const alerts = await alertRes.json();
      const alertTbody = document.getElementById('recent-alerts-tbody');
      alertTbody.innerHTML =
        alerts
          .slice(0, 5)
          .map(
            (a) => `
                <tr>
                    <td><span class="severity-badge ${a.severity}">${a.severity}</span></td>
                    <td>${a.title}</td>
                    <td>${a.created_at}</td>
                </tr>
            `,
          )
          .join('') || '<tr><td colspan="3" class="text-center">No recent alerts</td></tr>';
    } catch (err) {
      console.error('Failed to fetch dashboard previews:', err);
    }
  }
}

//MAIN---------------------------------------------------------------------------------------------------------------------
new DashboardManager();
