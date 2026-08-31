
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
Login Page
![Uploading Screenshot 2026-08-31 at 7.36.32 PM.png…]()


🏠 Dashboard
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 38 PM" src="https://github.com/user-attachments/assets/a159965a-b84f-46c4-83b1-9e45b245359d" />

Console
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 43 PM" src="https://github.com/user-attachments/assets/50179220-c605-4b5a-bfa6-34995997ee0c" />


🖥️ Endpoint Management
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 46 PM" src="https://github.com/user-attachments/assets/5e200f15-0b88-4c9f-89e7-d01484ca29e9" />

📜 Policy Management
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 49 PM" src="https://github.com/user-attachments/assets/dd991197-bfb4-45c8-81a8-69eedc138f44" />

DPI
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 52 PM" src="https://github.com/user-attachments/assets/eb492b4e-7796-42dd-82c8-900030fb1f08" />

Logs & Analytics
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 56 PM" src="https://github.com/user-attachments/assets/b7f6a919-77f4-4166-b619-6faed7c2a090" />

🚨 Security Alerts<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 36 59 PM" src="https://github.com/user-attachments/assets/c43eac0d-0ea4-40b8-bde8-e620877d34c3" />

Architecture
<img width="1470" height="956" alt="Screenshot 2026-08-31 at 7 37 02 PM" src="https://github.com/user-attachments/assets/f8e62f20-2709-4e18-8b21-42e649f4f649" />

📚 Project Documentation
The complete project documentation covers:
Abstract
Introduction
Problem Statement
Existing System
Proposed Solution
System Architecture
Endpoint Agent
Central Web Console
Policy Engine
Application Context Identification
System Design
Implementation
Use Cases
Testing & Validation
Innovation & Scalability
Future Scope
Results & Conclusion

🏆 Smart India Hackathon 2026
Details	Information
Event	Smart India Hackathon 2026
Project	SentryWall
Problem Statement ID	SIH1741
Theme	Cybersecurity
Category	Software
Team Name	HackOrbit
Institution	GITAM School of Science
Department	MCA


👥 Team HackOrbit
👨‍💻 Team Leader
Sanapathi Ganesh
👨‍💻 Team Members
Adyasha Behera
Roshani Bhoi
Priyanka Patra
G. Durga Prasad
CH. Revanth
👩‍🏫 Mentor
Anu Sharma


🎯 Conclusion
SentryWall demonstrates a centralized approach to application-aware network security.
Instead of only monitoring where network traffic is going, SentryWall adds the ability to understand:
Which application generated the traffic, where it is going, and whether the connection should be allowed or blocked.
By combining an Endpoint Agent, Policy Engine, Central Web Console, event logging, and security alerts, SentryWall provides a foundation for centralized application-aware endpoint security.














