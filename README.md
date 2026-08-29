# SENTRYWALL — Final Working Prototype

This package keeps your existing dashboard design and adds:

1. **Flask central backend**
2. **Centralized policy engine**
3. **Persistent policy/log storage**
4. **REST APIs**
5. **Browser enforcement extension**
6. **Dashboard → backend log synchronization**
7. **Dashboard blocked-domain list → backend → extension synchronization**

## Run the project

Open Terminal inside this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Load the real browser enforcement prototype

1. Open Chrome or Edge.
2. Go to the Extensions page.
3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select the `extension` folder inside this project.
6. Keep the Flask backend running.
7. Add a domain in the Sentrywall dashboard's extension/domain area.
8. The dashboard syncs the list to the backend.
9. The extension reads the backend list and installs browser blocking rules.

For a quick immediate sync after adding a domain, wait for the extension's periodic sync (up to about one minute) or reload the extension.

## Important demo scope

The extension is a real browser-level enforcement prototype: it blocks configured network requests inside Chrome/Edge.

The current prototype does **not** claim to intercept every application on the operating system. The dashboard and backend demonstrate the centralized application-context policy architecture; the extension proves real enforcement for browser traffic.

## API endpoints

- `GET /api/health`
- `GET /api/policies`
- `PUT /api/policies/<application>`
- `POST /api/decide`
- `GET /api/logs`
- `POST /api/logs`
- `DELETE /api/logs`
- `GET /api/blocked-domains`
- `POST /api/blocked-domains`

## Demo flow for judges

**Admin creates centralized policy**
→ **Endpoint/application attempts destination**
→ **Policy engine evaluates application + destination + protocol**
→ **ALLOW/BLOCK decision**
→ **Decision is logged**
→ **Dashboard shows logs/analytics**

For browser enforcement:

**Dashboard domain list**
→ **Flask backend**
→ **Sentrywall Enforcer extension**
→ **Chrome/Edge request is blocked**
