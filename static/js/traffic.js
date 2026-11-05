class TrafficManager {
  constructor() {
    this.isPaused = false;
    this.init();
  }

  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.loadTrafficLogs();

      // Poll traffic stream every 3 seconds if not paused
      setInterval(() => {
        if (!this.isPaused) this.loadTrafficLogs();
      }, 3000);

      document
        .getElementById('toggle-stream-btn')
        .addEventListener('click', () => this.toggleStream());
      document
        .getElementById('apply-filters-btn')
        .addEventListener('click', () => this.loadTrafficLogs());
      document
        .getElementById('reset-filters-btn')
        .addEventListener('click', () => this.resetFilters());
    });
  }

  toggleStream() {
    this.isPaused = !this.isPaused;
    const btn = document.getElementById('toggle-stream-btn');
    if (this.isPaused) {
      btn.textContent = 'Resume Stream';
      btn.classList.remove('active');
    } else {
      btn.textContent = 'Pause Stream';
      btn.classList.add('active');
      this.loadTrafficLogs();
    }
  }

  async loadTrafficLogs() {
    try {
      const src = document.getElementById('filter-src-ip').value;
      const dest = document.getElementById('filter-dest-ip').value;
      const proto = document.getElementById('filter-protocol').value;

      const response = await fetch('/api/traffic?limit=100');
      let logs = await response.json();

      // Client-side filtering pass
      if (src) logs = logs.filter((l) => l.source_ip.includes(src));
      if (dest) logs = logs.filter((l) => l.destination_ip.includes(dest));
      if (proto) logs = logs.filter((l) => l.protocol === proto);

      this.renderTraffic(logs);
    } catch (err) {
      console.error('Failed to fetch traffic logs:', err);
    }
  }

  renderTraffic(logs) {
    const tbody = document.getElementById('traffic-tbody');
    if (!logs.length) {
      tbody.innerHTML = `<tr><td colspan="5" class="text-center">No traffic logs matching criteria</td></tr>`;
      return;
    }

    tbody.innerHTML = logs
      .map((l) => {
        let protoClass = 'protocol-tcp';
        if (l.protocol === 'UDP') protoClass = 'protocol-udp';
        if (l.protocol === 'ICMP') protoClass = 'protocol-icmp';

        return `
                <tr>
                    <td>${l.timestamp}</td>
                    <td><code>${l.source_ip}</code></td>
                    <td><code>${l.destination_ip}</code></td>
                    <td><span class="protocol-badge ${protoClass}">${l.protocol}</span></td>
                    <td>${l.packet_size} bytes</td>
                </tr>
            `;
      })
      .join('');
  }

  resetFilters() {
    document.getElementById('filter-src-ip').value = '';
    document.getElementById('filter-dest-ip').value = '';
    document.getElementById('filter-protocol').value = '';
    this.loadTrafficLogs();
  }
}

//MAIN---------------------------------------------------------------------------------------------------------------------
new TrafficManager();
