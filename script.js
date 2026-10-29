// Synthetic sample coordinates for a browser-only educational demo.
const rows = [
  {t: 0,  sat: [7000, 0, 0],     debris: [7000, 2, 0]},
  {t: 10, sat: [6999.95, 75, 0], debris: [6999.90, 76.5, 0.2]},
  {t: 20, sat: [6999, 150, 0],   debris: [6998.8, 151, 0.4]},
  {t: 30, sat: [6997.2, 225, 0], debris: [6997, 225.8, 0.5]},
  {t: 40, sat: [6994.5, 300, 0], debris: [6994.4, 300.4, 0.6]}
];
const threshold = 1.0;
const distance = (a, b) => Math.sqrt(a.reduce((sum, value, i) => sum + (value - b[i]) ** 2, 0));
const calculated = rows.map(r => ({...r, d: distance(r.sat, r.debris)}));
const minD = Math.min(...calculated.map(r => r.d));
document.getElementById('sampleCount').textContent = calculated.length;
document.getElementById('minDistance').textContent = `${minD.toFixed(3)} km`;
document.getElementById('threshold').textContent = `${threshold.toFixed(2)} km`;
document.getElementById('status').textContent = minD <= threshold ? 'DEMO ALERT' : 'NOMINAL';
const tbody = document.getElementById('records');
calculated.forEach(r => {
  const alert = r.d <= threshold;
  const tr = document.createElement('tr');
  tr.innerHTML = `<td>${r.t}</td><td>${r.d.toFixed(3)}</td><td class="${alert ? 'status-alert' : 'status-ok'}">${alert ? 'DEMO ALERT' : 'NOMINAL'}</td>`;
  tbody.appendChild(tr);
});

// Canvas chart without external libraries.
const canvas = document.getElementById('chart');
const ctx = canvas.getContext('2d');
function drawChart() {
  const ratio = window.devicePixelRatio || 1;
  const width = canvas.clientWidth || 900;
  const height = 300;
  canvas.width = width * ratio;
  canvas.height = height * ratio;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  ctx.clearRect(0, 0, width, height);
  const pad = {l: 55, r: 20, t: 20, b: 42};
  const maxX = Math.max(...calculated.map(r => r.t)) || 1;
  const maxY = Math.max(threshold * 1.25, ...calculated.map(r => r.d)) * 1.15;
  const x = v => pad.l + (v / maxX) * (width - pad.l - pad.r);
  const y = v => height - pad.b - (v / maxY) * (height - pad.t - pad.b);
  ctx.lineWidth = 1;
  ctx.strokeStyle = '#34445f';
  ctx.fillStyle = '#aab8d3';
  ctx.font = '12px Segoe UI, Arial';
  for (let i = 0; i <= 4; i++) {
    const val = maxY * i / 4;
    ctx.beginPath(); ctx.moveTo(pad.l, y(val)); ctx.lineTo(width-pad.r, y(val)); ctx.stroke();
    ctx.fillText(val.toFixed(1), 8, y(val)+4);
  }
  ctx.beginPath(); ctx.setLineDash([6, 5]); ctx.strokeStyle = '#ffba68';
  ctx.moveTo(pad.l, y(threshold)); ctx.lineTo(width-pad.r, y(threshold)); ctx.stroke(); ctx.setLineDash([]);
  ctx.fillStyle = '#ffcf8a'; ctx.fillText('Demo threshold', pad.l + 8, y(threshold)-7);
  ctx.beginPath(); ctx.lineWidth = 3; ctx.strokeStyle = '#70c7ff';
  calculated.forEach((r, i) => i ? ctx.lineTo(x(r.t), y(r.d)) : ctx.moveTo(x(r.t), y(r.d)));
  ctx.stroke();
  calculated.forEach(r => { ctx.beginPath(); ctx.fillStyle = '#9ce6c1'; ctx.arc(x(r.t), y(r.d), 4, 0, Math.PI*2); ctx.fill(); });
  ctx.fillStyle = '#aab8d3'; ctx.fillText('Time (s)', width/2-20, height-8);
}
drawChart();
window.addEventListener('resize', drawChart);
