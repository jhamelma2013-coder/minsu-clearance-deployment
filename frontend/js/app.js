// MinSU Clearance System - Frontend
const API_URL = "";
let currentUser = null;

const API = {
    async call(endpoint, options = {}) {
        const r = await fetch(`/api${endpoint}`, {
            ...options,
            headers: { 'Content-Type': 'application/json' }
        });
        return await r.json();
    },
    async login(c) { return this.call('/auth/login', { method:'POST', body:JSON.stringify(c) }); },
    async getStats(uid) { return this.call(`/stats?uid_=${uid}`); },
    async getClearances(uid) { return this.call(`/clearances/list?uid_=${uid}`); }
};

function renderApp() {
    const a = document.getElementById('app');
    a.innerHTML = `<h1>MinSU Clearance</h1><p>Deployed successfully!</p>`;
}

renderApp();
