
# SentryWall

## 🚀 Project Overview
SentryWall is a centralized security and policy monitoring system.

## 📄 Project Documents

- Problem Statement
- Project Presentation
- Technical Documentation
- Architecture Diagram
- Demo Video
- Screenshots

## 🛠 Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## 👥 Team Members
S.Ganesh
G.Durga pradesh
Ch.Revanth
Adyasha Behara
Roshini bhoi
Priyanka priyadharshani para


# 🛡️ SENTRYWALL

### Centralized Application Context-Aware Firewall

**Smart India Hackathon 2026**

🎯 Problem Statement ID: **SIH1741**  
🛡️ Theme: **Cybersecurity**  
💻 Category: **Software**

---

> **Not just where the traffic is going — but which application sent it and whether it should be allowed.**

</div>

---

# 📌 About SentryWall

Modern computers run many applications simultaneously, and each application can independently connect to the internet.

Traditional firewalls mainly make decisions using:

- IP Address
- Port Number
- Protocol

However, these methods do not always provide enough information about **which application actually generated the network request**.

## 🔥 The Problem

Imagine multiple applications running on the same computer:

```text
Chrome       → google.com
VS Code      → github.com
Teams        → Microsoft Services
Unknown.exe  → Suspicious IP

💡 Our Solution
SentryWall is a centralized, application context-aware endpoint firewall.
Instead of making decisions only based on:IP + Port + Protocol
SentryWall adds application identity:Application
     +
Domain / IP
     +
Protocol / Port
     +
Centralized Policy
     ↓
ALLOW / BLOCK

🎯 Project Objectives
🔍 Identify applications generating network traffic
🛡️ Control application network access
🌐 Support domain-based policies
📡 Support IP-based policies
🔗 Support protocol and port-based policies
🏢 Centrally manage security policies
📊 Monitor network events
🚨 Generate alerts for suspicious or unauthorized activity

                         SECURITY ADMIN
                                │
                                ▼
                    ┌──────────────────────┐
                    │  CENTRAL WEB CONSOLE │
                    │──────────────────────│
                    │  📊 Dashboard        │
                    │  📜 Policies         │
                    │  📋 Logs             │
                    │  🚨 Alerts           │
                    └──────────┬───────────┘
                               │
                            REST API
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
 ┌──────────────┐       ┌──────────────┐      ┌──────────────┐
 │ Endpoint     │       │ Endpoint     │      │ Endpoint     │
 │ Agent        │       │ Agent        │      │ Agent        │
 └──────┬───────┘       └──────┬───────┘      └──────┬───────┘
        │                      │                      │
        └────────── Applications & Network ──────────┘
                               │
                               ▼

⚙️ Core Components
🖥️ Endpoint Agent
The Endpoint Agent runs on managed devices.
Its responsibilities include:
Monitoring network connection attempts
Identifying the application or process
Checking configured policies
Allowing or blocking requests
Logging network events
Sending relevant information to the Central Web Console

Endpoint Agent Workflow:
Application
     ↓
Network Request
     ↓
Endpoint Agent
     ↓
Identify Process
     ↓
Check Policy
     ↓
ALLOW / BLOCK
     ↓
Log Event
     ↓
Central Web Console
                            INTERNET

🌐 Central Web Console
The Central Web Console provides centralized management and monitoring.
Features
📊 Dashboard
🖥️ Endpoint Management
📜 Policy Management
📋 Network Event Monitoring
🚨 Security Alerts
The administrator can manage policies and monitor activity across endpoints from a centralized interface.
🧠 Policy Engine
The Policy Engine is the decision-making core of SentryWall.
It evaluates:
Application
+
Domain / IP
+
Protocol
+
Port
+
Configured Policy
        ↓
ALLOW / BLOCK

Example Policies
Application	Destination	Protocol	Port	Action
Chrome	github.com	TCP	443	✅ ALLOW
Chrome	youtube.com	TCP	443	🚫 BLOCK
Unknown.exe	Any	Any	Any	🚫 BLOCK

🔄 How SentryWall Works
1️⃣ Application initiates a network connection

        ↓

2️⃣ Endpoint Agent detects the activity

        ↓

3️⃣ Application / Process is identified

        ↓

4️⃣ Network information is extracted

   Application
   Destination
   Protocol
   Port

        ↓

5️⃣ Policy Engine evaluates the request

        ↓

6️⃣ Policy Match?

     YES                 NO
      │                   │
      ▼                   ▼

Apply Rule          Default Policy

      │                   │
      └─────────┬─────────┘
                ▼

          ALLOW / BLOCK

                ↓

            Log Event

                ↓

       Central Web Console

📊 Application Context
SentryWall focuses on identifying the application associated with a network connection.
Possible context fields include:
Process Name
Process ID
Executable Path
Destination IP
Destination Domain
Protocol
Port
Timestamp
Example:
Process: chrome.exe
PID: 4820
Destination: github.com
Protocol: TCP
Port: 443

🚨 Security Use Cases
1️⃣ Unauthorized Application
Unknown.exe
     ↓
External Network
     ↓
SentryWall
     ↓
🚫 BLOCK
     ↓
🚨 ALERT

2️⃣ Domain Restriction
Chrome → Approved Domain   → ✅ ALLOW

Chrome → Restricted Domain → 🚫 BLOCK

3️⃣ Enterprise Policy
An administrator can define organization-wide policies such as:
Only approved applications can access external networks.
The policies can then be centrally managed across endpoints.

4️⃣ Suspicious Connection
Detect
  ↓
Evaluate
  ↓
Block
  ↓
Log
  ↓
Alert

🧪 Testing & Validation
The prototype was tested using representative scenarios.
Test ID	Scenario	Expected	Actual	Result
T01	Allowed Application	Allow	Allow	✅ PASS
T02	Blocked Domain	Block	Block	✅ PASS
T03	Blocked IP	Block	Block	✅ PASS
T04	Restricted Application	Block	Block	✅ PASS
T05	Policy Update	Updated	Updated	✅ PASS
T06	Event Logging	Logged	Logged	✅ PASS
T07	Alert Generation	Alert	Alert	✅ PASS

✨ Key Features
🔍 Application-aware network monitoring
🛡️ Application-level access control
🌐 Domain restriction
📍 IP restriction
🔌 Protocol and port-based policies
🏢 Centralized policy management
📊 Centralized monitoring
📝 Structured event logging
🚨 Security alert generation

🚀 Innovation
Traditional Firewall
IP + Port + Protocol
        ↓
Firewall Rule
        ↓
ALLOW / BLOCK

SentryWall
Application
      +
Domain / IP
      +
Protocol / Port
      +
Centralized Policy
        ↓
ALLOW / BLOCK

🔮 Future Scope
Potential future enhancements include:
🤖 AI/ML-based anomaly detection
🧠 Behavioral analysis of application network patterns
🛡️ Threat intelligence integration
🔍 Malware and reputation analysis
💻 Cross-platform Endpoint Agent support
☁️ Cloud-based centralized management
🔐 Zero-Trust Network Access integration
📈 Enterprise-scale deployment support

🛠️ System Design
Endpoint Agent
      ↓
REST API
      ↓
Backend
      ↓
Database
      ↓
Central Dashboard

📂 Project Structure
SentryWall/
│
├── 📄 README.md
│
├── 📁 frontend/
│   └── Central Web Console
│
├── 📁 backend/
│   └── API and Backend Services
│
├── 📁 endpoint-agent/
│   └── Endpoint Monitoring Agent
│
├── 📁 docs/
│   └── Project Documentation
│
├── 📁 screenshots/
│   └── Application Screenshots
│
└── 📁 architecture/
    └── System Architecture
##
Login Page
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 32 PM" src="https://github.com/user-attachments/assets/6f683f17-2bee-4685-82c4-150e86ee69b6" />















