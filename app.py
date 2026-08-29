from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path
from datetime import datetime
import json
import os

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATA_FILE = BASE_DIR / "data.json"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
CORS(app)

DEFAULT_DATA = {
    "blocked_domains": ["github.com", "facebook.com"],
    "policies": {
        "Chrome.exe": [
            {"domain": "*.college.edu", "proto": "TCP/443", "action": "allow"},
            {"domain": "*", "proto": "TCP/80", "action": "block"}
        ],
        "Zoom.exe": [
            {"domain": "*.zoom.us", "proto": "UDP/443", "action": "allow"}
        ],
        "LMSClient.exe": [
            {"domain": "*.college.edu", "proto": "TCP/443", "action": "allow"},
            {"domain": "*", "proto": "ANY", "action": "block"}
        ],
        "uTorrent.exe": [
            {"domain": "*", "proto": "ANY", "action": "block"}
        ],
        "WhatsApp.exe": [
            {"domain": "*.whatsapp.net", "proto": "TCP/443", "action": "allow"},
            {"domain": "*", "proto": "ANY", "action": "block"}
        ]
    },
    "logs": [],
    "endpoints": [
        {"name": "CSE-LAB-PC-01", "status": "online"},
        {"name": "CSE-LAB-PC-04", "status": "online"},
        {"name": "DEV-LAPTOP-02", "status": "online"}
    ]
}

def load_data():
    if not DATA_FILE.exists():
        save_data(DEFAULT_DATA)
        return json.loads(json.dumps(DEFAULT_DATA))
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return json.loads(json.dumps(DEFAULT_DATA))

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def normalize_domain(value):
    value = str(value or "").strip().lower()
    value = value.replace("https://", "").replace("http://", "")
    value = value.split("/")[0].split(":")[0]
    if value.startswith("www."):
        value = value[4:]
    return value

def wildcard_match(pattern, value):
    pattern = str(pattern or "").strip().lower()
    value = normalize_domain(value)
    if pattern == "*":
        return True
    if pattern.startswith("*."):
        base = pattern[2:]
        return value == base or value.endswith("." + base)
    return value == normalize_domain(pattern)

def protocol_match(rule_proto, protocol):
    rp = str(rule_proto or "ANY").lower()
    p = str(protocol or "ANY").lower()
    return rp == "any" or rp == p

def evaluate(application, destination, protocol):
    data = load_data()
    rules = data.get("policies", {}).get(application, [])
    for rule in rules:
        if wildcard_match(rule.get("domain"), destination) and protocol_match(rule.get("proto"), protocol):
            return {
                "action": rule.get("action", "block"),
                "matched_rule": rule,
                "reason": "Matched application-context policy"
            }

    # Browser enforcement list is an additional centralized block layer.
    domain = normalize_domain(destination)
    for blocked in data.get("blocked_domains", []):
        if wildcard_match(blocked, domain):
            return {
                "action": "block",
                "matched_rule": {"domain": blocked, "proto": "ANY", "action": "block"},
                "reason": "Matched centralized browser block list"
            }

    return {
        "action": "block",
        "matched_rule": {"domain": "DEFAULT", "proto": "ANY", "action": "block"},
        "reason": "Zero-trust default deny: no matching allow rule"
    }

@app.get("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.get("/api/health")
def health():
    data = load_data()
    return jsonify({
        "status": "online",
        "service": "Sentrywall Central Policy Engine",
        "endpoints": len(data.get("endpoints", []))
    })

@app.get("/api/policies")
def get_policies():
    return jsonify({"policies": load_data().get("policies", {})})

@app.put("/api/policies/<application>")
def set_policy(application):
    body = request.get_json(silent=True) or {}
    rules = body.get("rules")
    if not isinstance(rules, list):
        return jsonify({"error": "rules must be a list"}), 400

    data = load_data()
    clean = []
    for rule in rules:
        domain = str(rule.get("domain", "")).strip()
        proto = str(rule.get("proto", "ANY")).strip()
        action = str(rule.get("action", "block")).strip().lower()
        if not domain or action not in {"allow", "block"}:
            return jsonify({"error": "Each rule needs domain and allow/block action"}), 400
        clean.append({"domain": domain, "proto": proto or "ANY", "action": action})

    data.setdefault("policies", {})[application] = clean
    save_data(data)
    return jsonify({"ok": True, "application": application, "rules": clean})

@app.post("/api/decide")
def decide():
    body = request.get_json(silent=True) or {}
    application = str(body.get("application", "")).strip()
    destination = str(body.get("destination", "")).strip()
    protocol = str(body.get("protocol", "ANY")).strip()

    if not application or not destination:
        return jsonify({"error": "application and destination are required"}), 400

    result = evaluate(application, destination, protocol)
    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "application": application,
        "destination": normalize_domain(destination),
        "protocol": protocol,
        "action": result["action"],
        "matched_rule": result["matched_rule"]["domain"]
    }

    data = load_data()
    data.setdefault("logs", []).insert(0, entry)
    data["logs"] = data["logs"][:500]
    save_data(data)
    return jsonify({**result, "log": entry})

@app.get("/api/logs")
def get_logs():
    limit = min(max(int(request.args.get("limit", 100)), 1), 500)
    return jsonify({"logs": load_data().get("logs", [])[:limit]})

@app.post("/api/logs")
def add_log():
    body = request.get_json(silent=True) or {}
    entry = {
        "time": body.get("time") or datetime.now().strftime("%H:%M:%S"),
        "application": str(body.get("application", "Unknown")),
        "destination": normalize_domain(body.get("destination", "unknown")),
        "protocol": str(body.get("protocol", "ANY")),
        "action": str(body.get("action", "block")).lower(),
        "matched_rule": str(body.get("matched_rule", "DEFAULT"))
    }
    data = load_data()
    data.setdefault("logs", []).insert(0, entry)
    data["logs"] = data["logs"][:500]
    save_data(data)
    return jsonify({"ok": True, "log": entry}), 201

@app.delete("/api/logs")
def clear_logs():
    data = load_data()
    data["logs"] = []
    save_data(data)
    return jsonify({"ok": True})

@app.get("/api/blocked-domains")
def get_blocked_domains():
    return jsonify({"domains": load_data().get("blocked_domains", [])})

@app.post("/api/blocked-domains")
def set_blocked_domains():
    body = request.get_json(silent=True) or {}
    domains = body.get("domains", [])
    if not isinstance(domains, list):
        return jsonify({"error": "domains must be a list"}), 400

    clean = []
    for domain in domains:
        d = normalize_domain(domain)
        if d and d not in clean:
            clean.append(d)

    data = load_data()
    data["blocked_domains"] = clean
    save_data(data)
    return jsonify({"ok": True, "domains": clean})

if __name__ == "__main__":
    # debug=False avoids duplicate processes and makes the demo simpler.
    app.run(host="0.0.0.0", port=5001, debug=False)
