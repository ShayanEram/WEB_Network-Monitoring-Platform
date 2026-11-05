class AlertsManager {
  constructor() {
    this.allAlerts = [];
    this.init();
  }

  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.loadAlerts();

      document.getElementById('alert-search').addEventListener('input', () => this.filterAlerts());
      document
        .getElementById('severity-filter')
        .addEventListener('change', () => this.loadAlerts());
      document
        .getElementById('acknowledge-all-btn')
        .addEventListener('click', () => alert('All alerts marked as acknowledged.'));
      document
        .getElementById('clear-alerts-btn')
        .addEventListener('click', () => alert('Alert history cleared.'));
    });
  }

  async loadAlerts() {
    try {
      const severity = document.getElementById('severity-filter').value;
      const response = await fetch(`/api/alerts?severity=${severity}`);
      this.allAlerts = await response.json();
      this.renderAlerts(this.allAlerts);
      this.updateAlertCounts(this.allAlerts);
    } catch (err) {
      console.error('Failed to load alerts:', err);
      document.getElementById('alerts-container').innerHTML =
        `<div class="alert-card"><p class="text-center text-danger">Error loading alerts</p></div>`;
    }
  }

  renderAlerts(alerts) {
    const container = document.getElementById('alerts-container');
    if (!alerts.length) {
      container.innerHTML = `<div class="alert-card"><p class="text-center" style="width:100%;">No security alerts found.</p></div>`;
      return;
    }

    container.innerHTML = alerts
      .map(
        (a) => `
            <div class="alert-card ${a.severity || 'info'}">
                <div class="alert-content">
                    <h4>${a.title}</h4>
                    <p>${a.message}</p>
                </div>
                <div class="alert-meta">
                    <span class="severity-badge ${a.severity || 'info'}">${
                      a.severity || 'info'
                    }</span>
                    <span class="alert-time">${a.created_at}</span>
                </div>
            </div>
        `,
      )
      .join('');
  }

  filterAlerts() {
    const query = document.getElementById('alert-search').value.toLowerCase();
    const filtered = this.allAlerts.filter(
      (a) =>
        (a.title && a.title.toLowerCase().includes(query)) ||
        (a.message && a.message.toLowerCase().includes(query)),
    );
    this.renderAlerts(filtered);
  }

  updateAlertCounts(alerts) {
    document.getElementById('stat-total-alerts').textContent = alerts.length;
    const criticalCount = alerts.filter(
      (a) => a.severity === 'critical' || a.severity === 'warning',
    ).length;
    document.getElementById('stat-critical-alerts').textContent = criticalCount;
    document.getElementById('stat-unack-alerts').textContent = alerts.length;
  }
}

//MAIN---------------------------------------------------------------------------------------------------------------------
new AlertsManager();
