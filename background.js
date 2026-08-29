const API_URL = "http://127.0.0.1:5000/api/blocked-domains";

function toRule(id, domain) {
  const clean = String(domain || "").trim().toLowerCase().replace(/^www\./, "");
  const pattern = clean.startsWith("*.") ? clean.slice(2) : clean;
  return {
    id,
    priority: 1,
    action: { type: "block" },
    condition: {
      urlFilter: "||" + pattern + "^",
      resourceTypes: [
        "main_frame", "sub_frame", "xmlhttprequest",
        "script", "image", "font", "stylesheet", "media", "other"
      ]
    }
  };
}

async function syncFromBackend() {
  try {
    const response = await fetch(API_URL, {cache: "no-store"});
    if (!response.ok) throw new Error("Backend returned " + response.status);
    const payload = await response.json();
    const domains = Array.isArray(payload.domains) ? payload.domains : [];

    const oldRules = await chrome.declarativeNetRequest.getDynamicRules();
    const newRules = domains.slice(0, 1000).map((domain, index) => toRule(index + 1, domain));

    await chrome.declarativeNetRequest.updateDynamicRules({
      removeRuleIds: oldRules.map(rule => rule.id),
      addRules: newRules
    });

    await chrome.storage.local.set({
      sentrywallDomains: domains,
      lastSync: new Date().toISOString(),
      backendOnline: true
    });
  } catch (error) {
    console.warn("Sentrywall backend sync failed:", error);
    await chrome.storage.local.set({backendOnline: false});
  }
}

chrome.runtime.onInstalled.addListener(async () => {
  await chrome.alarms.create("sentrywallSync", {periodInMinutes: 1});
  await syncFromBackend();
});

chrome.runtime.onStartup.addListener(syncFromBackend);

chrome.alarms.onAlarm.addListener(alarm => {
  if (alarm.name === "sentrywallSync") syncFromBackend();
});

// Dashboard can ask an installed extension to refresh immediately.
// No fixed extension ID is required for backend-based synchronization.
chrome.runtime.onMessageExternal.addListener((message, sender, sendResponse) => {
  if (message && message.type === "SYNC_POLICY") {
    syncFromBackend().then(async () => {
      const data = await chrome.storage.local.get("sentrywallDomains");
      sendResponse({ok: true, count: (data.sentrywallDomains || []).length});
    }).catch(() => sendResponse({ok: false}));
    return true;
  }
});
