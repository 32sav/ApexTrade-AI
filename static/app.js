let currentId = null;

const stateEl = document.getElementById("state");
const messageEl = document.getElementById("message");

function showMessage(text, ok) {
  messageEl.className = "message " + (ok ? "ok" : "error");
  messageEl.textContent = text;
}

function renderPortfolio(p) {
  currentId = p.id;
  document.getElementById("portfolioId").value = p.id;

  const rows = Object.entries(p.positions)
    .map(([symbol, qty]) => `<tr><td>${symbol}</td><td>${qty}</td></tr>`)
    .join("");

  stateEl.innerHTML = `
    <p><strong>Portfolio ${p.id}</strong> &middot; Cash: ${Number(p.cash).toFixed(2)}</p>
    <table>
      <tr><th>Symbol</th><th>Shares</th></tr>
      ${rows || '<tr><td colspan="2">No positions</td></tr>'}
    </table>`;
}

async function callApi(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || "Request failed");
  }
  return data;
}

document.getElementById("createBtn").addEventListener("click", async () => {
  try {
    const cash = Number(document.getElementById("startCash").value);
    const p = await callApi("/portfolios", {
      method: "POST",
      body: JSON.stringify({ cash }),
    });
    renderPortfolio(p);
    showMessage(`Created portfolio ${p.id}.`, true);
  } catch (err) {
    showMessage(err.message, false);
  }
});

document.getElementById("loadBtn").addEventListener("click", async () => {
  try {
    const id = document.getElementById("portfolioId").value;
    const p = await callApi(`/portfolios/${id}`);
    renderPortfolio(p);
    showMessage(`Loaded portfolio ${p.id}.`, true);
  } catch (err) {
    showMessage(err.message, false);
  }
});

document.getElementById("orderBtn").addEventListener("click", async () => {
  if (currentId === null) {
    showMessage("Create or load a portfolio first.", false);
    return;
  }
  try {
    const order = {
      symbol: document.getElementById("symbol").value.trim().toUpperCase(),
      side: document.getElementById("side").value,
      quantity: Number(document.getElementById("quantity").value),
      price: Number(document.getElementById("price").value),
    };
    const p = await callApi(`/portfolios/${currentId}/orders`, {
      method: "POST",
      body: JSON.stringify(order),
    });
    renderPortfolio(p);
    showMessage(`${order.side.toUpperCase()} ${order.quantity} ${order.symbol} placed.`, true);
  } catch (err) {
    showMessage(err.message, false);
  }
});