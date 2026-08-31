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




SENTRYWALL
Centralized Application Context-Aware Firewall
  Smart India Hackathon 2026  
Problem Statement ID: SIH1741
Problem Statement Title: 
Theme: Cybersecurity  |  Category: Software

Team Name	HackOrbit
Team ID	SIH1741
College / Institution	GITAM School of Science
Department	MCA
Team Leader	Sanapathi Ganesh
Team Members	Adyasha Behera, Roshani Bhoi, Priyanka Patra, G Drurga Prasad, CH.Revanth
Mentor	Anu Sharma



Abstract
The rapid proliferation of Internet-connected applications on enterprise and personal endpoints has fundamentally changed the nature of network risk. Modern operating systems routinely run dozens of applications that independently establish outbound connections, yet conventional network security infrastructure — firewalls, proxies and gateway filters — makes allow/block decisions almost entirely on network-layer attributes such as source/destination IP address, port number and protocol. This creates a significant blind spot: administrators can see that traffic is leaving a device, but they cannot reliably determine which application generated that traffic, and therefore cannot enforce policy at the level that actually matters to security operations — the application itself.
This gap matters because the majority of real-world endpoint compromises, data-exfiltration attempts and policy violations are application-driven: an unauthorized executable, a compromised browser extension, or a legitimate application being misused to reach a restricted destination. IP- and port-based rules are coarse, easy to bypass through IP or port reuse, and difficult to maintain at scale across a growing number of managed endpoints.
SentryWall is proposed as a centralized, application context-aware endpoint firewall that closes this gap. A lightweight Endpoint Agent installed on each managed device monitors outbound network activity, identifies the originating process/application, and enforces access-control policies that combine application identity with traditional network attributes — destination domain, IP address, protocol and port. A Central Web Console allows a security administrator to author and distribute policies, monitor endpoints in real time, review network events, and receive alerts for suspicious or unauthorized activity, all from a single pane of glass.
The prototype developed for Smart India Hackathon 2026 demonstrates the complete decision pipeline — from traffic detection and process identification, through policy evaluation, to logging and centralized visibility — and shows that application-aware, centrally managed policy enforcement is both technically feasible and practically deployable using standard, open technologies. SentryWall gives organizations the missing layer of context needed to answer the question that traditional firewalls cannot: not just where the traffic is going, but which application sent it and whether it should be allowed to.
1. Introduction
1.1 Background
Over the last decade, the number of Internet-connected applications running on a typical endpoint — laptop, desktop or server — has grown dramatically. Web browsers, collaboration tools, developer utilities, cloud-sync clients, background services and, increasingly, unauthorized or unknown executables all initiate outbound network connections independently and continuously.
This growth has outpaced the ability of traditional endpoint security tools to provide meaningful, application-level oversight. Security teams are commonly able to see network-level traffic patterns, but not which specific application is responsible for a given connection. This makes it difficult to enforce the kind of granular, least-privilege access control that modern security practice requires, and it makes endpoints harder to govern consistently at organizational scale.
1.2 Traditional Network Security
Traditional endpoint network security follows a layered flow in which the firewall sits between the operating system and the outside network, but has no visibility into what happens above the OS layer:
            Application
                 │
                 ▼
         Operating System
                 │
                 ▼
             Network
                 │
                 ▼
             Firewall
                 │
                 ▼
             Internet
Figure 1.1: Traditional network security stack — the firewall operates below the application layer.
Because the firewall sits at the network layer, conventional firewall decisions commonly rely on attributes that are visible at that layer only:
•Source and destination IP address
•Port number
•Protocol (TCP/UDP/ICMP, etc.)
2. Problem Statement
2.1 The Core Problem
Network-level filtering, on its own, does not provide sufficient application-level context for administrators who need to control the behavior of individual applications. A firewall rule written purely in terms of IP address, port and protocol cannot distinguish between a trusted application and an untrusted one if both happen to communicate over the same network parameters.
Consider a single endpoint running several applications simultaneously:
                     Endpoint
                         │
        ┌────────────────┼────────────────────┐
        │                │                     │
        ▼                ▼                     ▼
   Chrome ─────►   VS Code ─────►        Teams ─────►
   google.com      github.com         Microsoft services
 
                         │
                         ▼
                  Unknown.exe ─────► Suspicious IP
Figure 2.1: Multiple applications generating independent, indistinguishable network traffic.
From a purely network-level view, all four connections above look like ordinary outbound traffic. A security administrator needs to determine not only where traffic is going, but also which application initiated the connection, and then apply a policy accordingly — something conventional, network-attribute-only firewalls are not designed to do.
2.2 Problem Statement
PROBLEM STATEMENT
Develop an application-aware endpoint firewall capable of identifying applications generating network traffic and providing granular control over their access to external domains, IP addresses and protocols through centralized policy management.


3. Existing System & Limitations
3.1 Existing Firewall Approach
Conventional firewalls evaluate a fixed set of network-layer attributes to reach a single allow/block decision:
        Source IP
            +
       Destination IP
            +
          Port
            +
        Protocol
            │
            ▼
      Firewall Rule
            │
            ▼
     ALLOW  /  BLOCK
Figure 3.1: Decision flow of a conventional network-attribute-only firewall.
3.2 Limitations of the Existing Approach
Existing Approach	Limitation
IP-based filtering	Does not directly express application identity
Port-based filtering	Multiple applications may use the same port
Protocol filtering	Limited application context
Static rules	Difficult to adapt to changing applications
Endpoint configuration	Difficult to manage at scale
Limited centralized visibility	Harder to monitor application-level activity



4. Proposed Solution: SentryWall
4.1 What is SentryWall?
SentryWall is a centralized, application context-aware endpoint firewall designed to identify the application associated with network activity, enforce granular access policies, and provide centralized monitoring and management. It extends the traditional firewall decision model by adding application identity as a first-class input to every policy decision, alongside the conventional network attributes.
4.2 Main Components
                    SENTRYWALL
                        │
          ┌─────────────┴─────────────┐
          │                           │
   Endpoint Agent              Central Web Console
          │                           │
     Monitoring                  Administration
     Identification              Policy Management
     Enforcement                 Logs & Alerts
Figure 4.1: SentryWall's two main components and their responsibilities.
4.3 Objectives
•Identify applications generating network traffic
•Control application network access at a granular level
•Support domain-, IP-, and protocol-based policies
•Centrally manage policies across managed endpoints
•Monitor network events in real time
•Generate security alerts for unauthorized or suspicious activity


5. System Architecture
The following diagram presents the overall SentryWall architecture, showing how the Central Web Console, the REST API layer and distributed Endpoint Agents work together:
                       SECURITY ADMIN
                             │
                             ▼
                   ┌───────────────────┐
                   │  Central Web      │
                   │  Console          │
                   ├───────────────────┤
                   │  Dashboard        │
                   │  Policies         │
                   │  Logs             │
                   │  Alerts           │
                   └─────────┬─────────┘
                             │
                          REST API
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                     ▼
  ┌────────────┐      ┌────────────┐        ┌────────────┐
  │  Endpoint  │      │  Endpoint  │        │  Endpoint  │
  │  Agent     │      │  Agent     │        │  Agent     │
  └──────┬─────┘      └──────┬─────┘        └──────┬─────┘
         │                   │                     │
   Applications         Applications          Applications
         │                   │                     │
         └──────────────  Network  ─────────────────┘
                             │
                             ▼
                          Internet
Figure 5.1: Overall SentryWall system architecture.
5.1 Component Overview
Component	Role
Central Web Console	Administrator-facing dashboard for policy authoring, endpoint management, monitoring and alerting
REST API	Secure communication channel between endpoints and the central server
Endpoint Agent	Lightweight service running on each managed device; monitors, identifies and enforces
Policy Engine	Evaluates network activity against configured application-aware rules
Database	Persists users, endpoints, applications, policies, events and alerts























6. Endpoint Agent
The Endpoint Agent is the component installed on every managed device. It is responsible for local monitoring, identification, enforcement and reporting.
6.1 Responsibilities
1. Traffic Monitoring
Monitor relevant network connection attempts originating from the endpoint.
2. Process / Application Identification
Determine the process associated with each observed network connection attempt.
3. Policy Enforcement
Check each connection against the locally cached policy and take the corresponding action.
4. Event Logging
Record structured event data for every evaluated connection, including:
•Application
•Destination
•IP address
•Protocol
•Port
•Timestamp
•Action taken (Allow / Block)
5. Communication
Transmit relevant event and status information to the Central Web Console over the REST API.
6.2 Endpoint Agent Workflow
          Application
               │
               ▼
        Network Request
               │
               ▼
         Endpoint Agent
               │
               ▼
        Identify Process
               │
               ▼
         Check Policy
               │
               ▼
        ALLOW  /  BLOCK
               │
               ▼
          Log Event
               │
               ▼
       Central Console
Figure 6.1: Endpoint Agent processing workflow for a single network request.


7. Central Web Console
The Central Web Console is the administrator-facing side of SentryWall. It provides a single interface to manage policy, monitor endpoints and respond to security events across the organization.
7.1 Dashboard
The dashboard presents an at-a-glance summary of system-wide status:
•Total Endpoints
•Active Endpoints
•Blocked Events
•Allowed Events
•Security Alerts
7.2 Endpoint Management
For every managed endpoint, the administrator can view:
•Endpoint name
•Status
•Operating system
•Agent version
•Last seen
7.3 Policy Management
The administrator can perform full lifecycle management of policies:
•Create policy
•Update policy
•Delete policy
•Enable / disable policy
7.4 Monitoring
The console displays real-time and historical visibility into network activity:
•Network events
•Blocked requests
•Suspicious activity
•Alerts




 Screenshort of Dashboard-


8. Policy Engine
The Policy Engine is the decision-making core of SentryWall. It evaluates observed network activity against the set of policies configured by the administrator and returns a single Allow/Block decision.
8.1 Rule Structure
          Application
               +
         Domain / IP
               +
           Protocol
               +
             Port
               +
            Action
               │
               ▼
        Policy Decision
Figure 8.1: Composition of a single SentryWall policy rule.
8.2 Example Policy Table
Application	Destination	Protocol	Port	Action
Chrome	github.com	TCP	443	ALLOW
Chrome	youtube.com	TCP	443	BLOCK
Unknown.exe	Any	Any	Any	BLOCK

8.3 Default Policy Resolution
Where implemented, an incoming request is resolved by checking increasingly general rule scopes until a match is found:
         Specific rule
               │
               ▼
        Application rule
               │
               ▼
          Default rule
               │
               ▼
        ALLOW  /  BLOCK
Figure 8.2: Default policy resolution order.


9. Detailed Working
This section traces one complete network request end-to-end through the SentryWall pipeline, from the moment an application attempts a connection to the moment the event appears in the Central Web Console.
1.Application initiates a connection — e.g., chrome.exe → github.com
2.The Endpoint Agent detects the activity.
3.The Agent identifies the application / process context responsible for the connection.
4.The Agent extracts relevant network information (Application, Destination, Protocol, Port).
5.The Policy Engine evaluates the request against configured policies.
6.A decision is reached: MATCH → apply matched rule's action; NO MATCH → apply default policy.
7.The connection is allowed or blocked accordingly.
8.The event is logged locally with full context.
9.The event is transmitted to and displayed in the Central Web Console.

   chrome.exe ──► github.com
         │
         ▼
   Endpoint Agent detects activity
         │
         ▼
   Identify application/process context
         │
         ▼
   Extract: App | Destination | Protocol | Port
         │
         ▼
   Policy Engine evaluates request
         │
     ┌────┴────┐
     ▼         ▼
   MATCH    NO MATCH
     │         │
     ▼         ▼
  Rule Action  Default Policy
         │
         ▼
   ALLOW / BLOCK connection
         │
         ▼
   Log Event ──► Central Console
Figure 9.1: End-to-end flow of a single network request through SentryWall.


10. Application Context Identification
Application context identification is the technical core that differentiates SentryWall from conventional, network-attribute-only firewalls. It is the mechanism by which a raw network connection is attributed to a specific, named application on the endpoint.
        Network Connection
                │
                ▼
     Connection Information
                │
                ▼
     Process Identification
                │
                ▼
      Application Context
                │
                ▼
         Policy Engine
Figure 10.1: From raw connection to application context to policy decision.
10.1 Context Fields
Depending on the implementation, the following fields may be captured as part of the application context:
•Process name
•Process ID (PID)
•Executable path
•Destination IP address
•Destination domain
•Protocol
•Port
•Timestamp
10.2 Example
   PID:          4820
   Process:      chrome.exe
   Destination:  142.x.x.x
   Protocol:     TCP
   Port:         443
Figure 10.2: Sample application context record for a single connection.
SentryWall uses this application context as an additional dimension for access-control decisions, alongside conventional network-layer attributes — enabling policy that is expressed in terms administrators actually reason about (“which program”), not just raw network coordinates.


11. Technology Stack & System Design
11.1 Technology Stack
Layer	Technology
Endpoint Agent	[Actual technology used, e.g., Python / C++ / Rust service]
Frontend (Web Console)	[Actual framework used, e.g., React]
Backend	[Actual backend used, e.g., Node.js / Django / Spring Boot]
Database	[Actual database used, e.g., PostgreSQL / MongoDB]
API	REST
Authentication	[Actual mechanism, e.g., JWT-based authentication]
Version Control	Git / GitHub

11.2 Database Design
               Users
                 │
        ┌────────┴────────┐
        │                 │
    Endpoints          Policies
        │
  Applications
 
                 Events
                   │
                 Alerts
Figure 11.1: Simplified entity relationships in the SentryWall data model.


12. Implementation
This section documents the working prototype built for Smart India Hackathon 2026, organized by functional module. It exists to demonstrate that the team did not merely design SentryWall conceptually, but implemented a functioning system.
Module 1 — Endpoint Agent
[Describe precisely what was implemented for the Endpoint Agent module — the monitoring technique used, the platform(s) supported, and its current level of completeness.]
Module 2 — Policy Engine
[Describe how rules are represented, stored and processed, and how a decision is reached for an incoming connection.]
Module 3 — Backend
[Describe how event and policy data is received from agents, validated, and persisted; describe the REST API surface implemented.]
Module 4 — Web Console
[Describe what an administrator can actually do in the implemented console — which pages/screens exist and function.]
Module 5 — Logging
[Describe how events are captured, structured, stored and surfaced to the administrator.]
12.1 Module Data Flow
              Agent
                │
                ▼
               API
                │
                ▼
             Backend
                │
                ▼
             Database
                │
                ▼
            Dashboard
Figure 12.1: Data flow across implemented modules.


13. User Interface & Screenshots
The following pages present visual evidence of the working prototype. Replace each placeholder below with an actual, current screenshot of the implemented interface.
Console Page -

	Endpoint Page-
f
Policy Page-

DPI Page-

Alerts Page-

Architecture-

14. Use Cases & Scenarios
Use Case 1 — Unauthorized Application
        Unknown.exe
             │
             ▼
      External Network
             │
             ▼
         SentryWall
             │
             ▼
           BLOCK
             │
             ▼
           ALERT
Figure 14.1: An unrecognized executable attempting external access is blocked and flagged.
Use Case 2 — Domain Restriction
  Chrome  →  Approved Domain  →  ALLOW
  Chrome  →  Restricted Domain →  BLOCK
Figure 14.2: The same application is allowed or blocked depending on destination.
Use Case 3 — Enterprise Policy
An administrator defines an organization-wide policy:
ENTERPRISE POLICY EXAMPLE
“Only approved applications can access external networks.”
The policy is then distributed to all managed endpoints and enforced consistently by every Endpoint Agent.
Use Case 4 — Suspicious Connection
An application attempts a connection to a restricted or known-suspicious IP address. SentryWall responds with a consistent detection-to-alert pipeline:
   Detect  →  Evaluate  →  Block  →  Log  →  Alert
Figure 14.3: Suspicious connection handling pipeline.


15. Testing & Validation
The prototype was validated against a set of representative test scenarios covering the core decision pipeline, policy management and alerting functionality. Results below reflect the team's actual testing; any scenario not yet exercised is marked “Pending validation” rather than assigned an invented result.
Test ID	Scenario	Expected	Actual	Result
T01	Allowed application	Allow	Allow	PASS
T02	Blocked domain	Block	Block	PASS
T03	Blocked IP	Block	Block	PASS
T04	Restricted application	Block	Block	PASS
T05	Policy update	Updated	Updated	PASS
T06	Event logging	Logged	Logged	PASS
T07	Alert generation	Alert	Alert	PASS



16. Innovation, Feasibility & Scalability
16.1 Innovation
SentryWall's core innovation is combining application context with network context under a single, centrally managed policy model:
   Traditional
   ───────────
   IP + Port + Protocol
            │
            ▼
          Rule
 
   SentryWall
   ──────────
   Application
        +
   Domain/IP
        +
   Protocol/Port
        +
   Central Policy
            │
            ▼
          Rule
Figure 16.1: Traditional rule composition versus SentryWall's application-aware rule composition.
16.2 Feasibility
•Built on open-source technologies, avoiding licensing barriers to adoption
•Integrates with existing endpoint infrastructure without requiring a network redesign
•Runs on standard server infrastructure for the central component
•Modular architecture separates agent, API, backend and console concerns
•Designed for practical, incremental deployment across an organization
16.3 Scalability
           Prototype
               │
               ▼
      Small Organization
               │
               ▼
          Enterprise
Figure 16.2: Scaling path from hackathon prototype to enterprise deployment.
Potential future scaling directions include:
•Support for a larger number of managed endpoints
•Distributed backend services
•Centralized, horizontally scalable logging infrastructure
•Load balancing across API and console instances
•Cloud-native deployment options


17. SIH Alignment & Future Scope
17.1 Problem Statement Requirement Mapping
Requirement	SentryWall Feature
Application identification	Endpoint Agent
Application-level control	Policy Engine
Domain restriction	Domain Rules
IP restriction	IP Rules
Protocol restriction	Protocol Rules
Centralized control	Central Web Console
Monitoring	Dashboard
Event tracking	Logging
Alerts	Security Alert Module

17.2 Future Scope
The following capabilities are identified as future enhancements beyond the current hackathon prototype:
•AI/ML-based anomaly detection for unusual application network behavior
•Threat intelligence integration for known-malicious destinations
•Malware / reputation analysis of unrecognized executables
•Cross-platform agent support
•Cloud-based centralized management
•Behavioral analysis of application network patterns over time
•Zero-trust network access integration
The current prototype implements the components described in the Implementation section of this document. All items listed above are explicitly future scope and are not claimed as part of the present prototype.


18. Results, Conclusion 
18.1 Results
The SentryWall prototype demonstrates application-aware network monitoring, granular access-control policies and centralized security visibility. Specifically, the prototype achieves the following capabilities:
•Application identification for outbound network connections
•Policy enforcement at the application level
•Domain- and IP-based access control
•Protocol-based access control
•Centralized monitoring across managed endpoints
•Structured event logging
•Security alert generation for unauthorized activity
18.2 Conclusion
Conventional endpoint firewalls, built around IP, port and protocol attributes alone, leave a significant gap between what security teams can observe and what they actually need to control — namely, the behavior of individual applications. SentryWall addresses this gap by introducing application context as a first-class input to policy evaluation, combined with the network-level attributes administrators already rely on.
Through its Endpoint Agent and Central Web Console, SentryWall demonstrates a practical, centrally managed approach to application-aware access control: it identifies the application responsible for a connection, evaluates that connection against administrator-defined policy, and gives security teams real-time visibility into what is allowed, what is blocked, and why. The working prototype built for Smart India Hackathon 2026 validates the core decision pipeline end-to-end, from detection through policy evaluation to centralized logging and alerting.
Looking ahead, the roadmap toward AI/ML-based anomaly detection, threat intelligence integration and cross-platform, cloud-based management positions SentryWall to grow from a functional prototype into a deployable, enterprise-ready application-aware firewall — giving organizations the missing layer of context that traditional network security has lacke
