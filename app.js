// Illustrative quotes only. No live data connection or trading signals.
const quotes = [
  ['S&P 500', '5,000.00', '+0.42%'], ['NASDAQ', '16,000.00', '+0.65%'],
  ['FTSE 100', '8,000.00', '−0.18%'], ['EURO STOXX 50', '4,800.00', '+0.30%'],
  ['NIKKEI 225', '38,000.00', '−0.24%'], ['HANG SENG', '18,000.00', '+0.55%'],
  ['FBM KLCI', '1,600.00', '+0.12%'],
  ['USD/MYR', '4.4500', '+0.10%'], ['EUR/MYR', '4.8200', '−0.15%'],
  ['GBP/MYR', '5.6500', '+0.08%'], ['JPY/MYR', '0.0297', '−0.20%'],
  ['CHF/MYR', '5.0200', '+0.12%'], ['CAD/MYR', '3.2800', '−0.09%'],
  ['AUD/MYR', '2.9300', '+0.22%'], ['NZD/MYR', '2.7200', '−0.11%']
];
const track = document.querySelector('#ticker-track');
if (track) {
  for (let copy = 0; copy < 2; copy++) {
    const group = document.createElement('div');
    group.className = 'ticker-group';
    if (copy) group.setAttribute('aria-hidden', 'true');
    quotes.forEach(([label, value, change]) => {
      const item = document.createElement('span');
      item.className = 'quote';
      const name = document.createElement('b'); name.textContent = label;
      const price = document.createElement('span'); price.textContent = value;
      const move = document.createElement('span'); move.textContent = change;
      move.className = change.startsWith('+') ? 'positive' : 'negative';
      item.append(name, price, move); group.append(item);
    });
    track.append(group);
  }
}
const pause = document.querySelector('#ticker-pause');
pause?.addEventListener('click', () => {
  const paused = pause.getAttribute('aria-pressed') !== 'true';
  pause.setAttribute('aria-pressed', String(paused));
  pause.textContent = paused ? 'Resume' : 'Pause';
  track.classList.toggle('paused', paused);
});
const themeButton = document.querySelector('#theme-toggle');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
let preference;
try { preference = localStorage.getItem('portfolio-theme'); } catch {}
function applyTheme(dark) {
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
  if (themeButton) {
    themeButton.textContent = dark ? 'Light mode' : 'Dark mode';
    themeButton.setAttribute('aria-pressed', String(dark));
    themeButton.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }
}
applyTheme(preference ? preference === 'dark' : systemTheme.matches);
themeButton?.addEventListener('click', () => {
  const dark = document.documentElement.dataset.theme !== 'dark';
  preference = dark ? 'dark' : 'light'; applyTheme(dark);
  try { localStorage.setItem('portfolio-theme', preference); } catch {}
});
systemTheme.addEventListener('change', e => { if (!preference) applyTheme(e.matches); });
