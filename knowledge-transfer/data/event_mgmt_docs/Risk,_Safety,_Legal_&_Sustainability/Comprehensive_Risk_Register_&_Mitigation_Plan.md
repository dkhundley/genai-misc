# Comprehensive Risk Register & Mitigation Plan
Topic: Risk, Safety, Legal & Sustainability

## Overview
This document provides a complete, ready-to-use approach to identify, assess, mitigate, and monitor operational, financial, reputational, legal/compliance, and environmental/sustainability risks for events. It includes:

- A standardized risk register structure (spreadsheet-ready)
- A scoring model (likelihood x impact) with a visual heat map
- Clear roles and responsibilities
- Sample, realistic risks and mitigations
- Cadence for review and escalation
- References and templates aligned to recognized standards

Intended users: Event managers, operations, health & safety (HSE), legal, IT, sustainability, finance, security, and vendor management.

Outputs:
- “Risk Register” spreadsheet with heat map
- Weekly/monthly risk summary for leadership
- Integrated Emergency Response and Sustainability Action Plans

## Key Details or Steps

### 1) Set up the Risk Register (Spreadsheet)
Create a workbook with these sheets:
- Risk Register (master log)
- Heat Map (pivot/visualization)
- Controls Library (preventive, detective, corrective controls)
- Risk Scales & Data Validation (drop-down lists and definitions)
- Change Log (audit trail of edits)
- Archive (closed risks)

Recommended columns for the Risk Register:
1. Risk ID (RR-###)
2. Category (Operational; Safety; Financial; Legal/Compliance; Reputational; IT/Cyber; Environmental/Sustainability; Vendor/Supply)
3. Risk Statement (event that may happen)
4. Cause
5. Consequence/Impact
6. Likelihood (1–5)
7. Impact (1–5)
8. Inherent Risk Score (auto: Likelihood x Impact)
9. Inherent Rating (High/Medium/Low)
10. Treatment Strategy (Avoid/Reduce/Transfer/Accept)
11. Mitigation Actions (preventive measures)
12. Contingency/Response Plan (what to do if it happens)
13. Owner (role/person)
14. Due Date (mitigation completion)
15. Status (Open; In Progress; Mitigated; Accepted; Transferred; Closed)
16. Early Warning Indicators (triggers/thresholds)
17. Linked Controls (from Controls Library)
18. Budget Impact (estimate)
19. Residual Likelihood (1–5, after mitigation)
20. Residual Impact (1–5, after mitigation)
21. Residual Score (auto)
22. Residual Rating
23. Dependencies (vendors, permits, systems)
24. Last Reviewed (date)
25. Notes/Updates

Data validation lists:
- Category
- Treatment Strategy
- Status
- Owner (standard role list)
- Rating (calculated; do not edit)

Formulas (Excel/Google Sheets):
- Inherent Score: =F2*G2
- Inherent Rating: =IF(H2>=15,"High",IF(H2>=8,"Medium","Low"))
- Residual Score: =S2*T2
- Residual Rating: =IF(U2>=15,"High",IF(U2>=8,"Medium","Low"))

Conditional formatting (Risk Register):
- Inherent Score and Residual Score cells:
  - Red if >=15
  - Amber if between 8 and 14
  - Green if <=7

### 2) Define the Scales (include in “Risk Scales” sheet)

Likelihood (select one):
- 1 Rare: ≤5% chance
- 2 Unlikely: >5–20%
- 3 Possible: >20–50%
- 4 Likely: >50–80%
- 5 Almost Certain: >80%

Impact (choose the highest applicable dimension):
- 1 Insignificant: No injury; ≤2 hours delay; ≤$5k cost; negligible media; no environmental harm
- 2 Minor: First aid only; ≤1 day delay; $5k–$25k; limited complaints; minor, contained environmental impact
- 3 Moderate: Medical treatment; ≤3 days delay; $25k–$100k; local negative press; reportable spill/waste issue
- 4 Major: Serious injury; 1–2 weeks delay; $100k–$500k; national negative media; significant environmental harm with regulatory involvement
- 5 Severe/Catastrophic: Fatality; event cancellation/significant duration impact; >$500k; sustained national/international scrutiny; major environmental damage, sanctions

Risk Appetite:
- High (Red): ≥15 — requires senior approval and immediate action
- Medium (Amber): 8–14 — active mitigation and monitoring
- Low (Green): ≤7 — monitor and accept if within tolerance

### 3) Identify Risks
- Host a 60–90 minute cross-functional workshop at T–12 weeks (earlier for large events).
- Use prompt lists: Safety, Operations, Legal/Permits, Finance/Insurance, IT/Cyber, Reputation/Media, Environment/Sustainability, Vendor/Supply, Security/Threats, Weather/Transport.
- Include known historical issues and close calls from prior events.

### 4) Assess and Score
- Document risk statement, cause, consequence.
- Apply Likelihood and Impact using defined scales.
- Calculate Inherent Score and Rating.

### 5) Plan Treatments
- Choose a strategy: Avoid, Reduce, Transfer, Accept.
- Define specific mitigation actions with owners and due dates.
- Define contingency/response actions in case risk materializes.
- Estimate residual risk and confirm it meets risk appetite.

Types of controls:
- Preventive: training, design changes, redundancies, permits, SLAs
- Detective: monitoring, inspections, alarms, dashboards
- Corrective: incident response, backups, recovery procedures

### 6) Build the Heat Map (Visualization)
- Create a 5x5 matrix with Likelihood (rows 1–5) vs Impact (columns 1–5).
- Use a pivot table from the Risk Register: Count of open risks grouped by Likelihood and Impact.
- Apply conditional formatting to cells:
  - Score (row x column) ≥15: Red
  - 8–14: Amber
  - ≤7: Green
- Display counts per cell and total high/medium/low risks.
- Update weekly (or daily during event week).

### 7) Monitor, Report, and Escalate
Cadence:
- T–10 to T–2 weeks: weekly risk review (30–45 minutes)
- T–1 week to Event Day: daily 15-minute risk huddles; update heat map
- Event Day: operational control room maintains live log; twice-daily leadership updates
- T+1 week: post-event review; close or reclassify residual risks; capture lessons learned

Escalation triggers:
- Any High risk (inherent or residual)
- Material changes to safety profile, permits, or security threat level
- EWI trip (e.g., wind forecast >25 mph for outdoor staging; ticket refund spike >5%/week)
- Critical dependency failure (e.g., generator delivery missed)

### 8) Close and Learn
- Mark risk Closed when mitigation complete and event exposure has passed.
- Document what worked, what failed, response performance, and recommended controls for future events.
- Update the Controls Library accordingly.

## Responsibilities
- Event Director (Accountable): Approves high-risk acceptance, resources, and major treatment decisions.
- Risk Lead/PMO (Responsible): Maintains register/heat map; runs reviews; ensures updates.
- HSE Manager (Responsible): Safety risk assessments (crowd, fire, structures), medical plan, evacuation, compliance.
- Legal Counsel (Consulted): Permits, contracts, insurance, data protection, T&Cs.
- Finance Controller (Consulted): Budget impacts, insurance procurement, contingency funds.
- Sustainability Lead (Responsible): Environmental risks, waste, energy, supplier sustainability compliance, reporting (e.g., ISO 20121).
- Security Lead (Responsible): Threat assessment, crowd security, VIP protection, screening protocols.
- IT/Cyber Lead (Responsible): Ticketing/registration platforms, data security, backups, incident response.
- Vendor Manager (Responsible): SLAs, performance monitoring, redundancy planning.
- Communications Lead (Consulted): Stakeholder messaging, media response, community management.
- All Risk Owners (Responsible): Deliver mitigations by due dates and update status.

RACI shorthand:
- A: Event Director
- R: Risk Lead + specific domain lead (HSE, IT, etc.)
- C: Legal, Finance, Comms
- I: All team members via weekly summaries

## Dependencies
- Venue/operator approvals; site access times; power and water availability
- Permits and licenses: public assembly, temporary structures, noise, health/food, alcohol, street closure, drone/UAS as required
- Emergency services liaison (police, fire, EMS); medical provider availability
- Critical vendors: staging, AV, generators, catering, ticketing, fencing, waste hauling
- Insurance policies: public liability, workers’ comp, event cancellation/weather, cyber, equipment
- Weather forecasting service; transport authority updates
- IT integrations: payment gateways, CRM, scanning hardware, Wi-Fi/cellular coverage
- Community stakeholders: local residents, council, businesses

## Example Risk Register Snapshot (sample data)
Note: Enter these into your spreadsheet. Scores auto-calc from Likelihood x Impact.

| ID | Category | Risk Statement | L | I | Score | Treatment | Key Mitigations | Owner | Due | Residual (L/I/S) | Status | EW Indicators |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RR-001 | Safety | Crowd crush at main entrance during peak ingress | 3 | 5 | 15 | Reduce | Staggered entry windows; barrier plan; 2 extra lanes; realtime density monitoring; staff training; radio comms | HSE Manager | T-14d | 2/4/8 | In Progress | Entry queue >50m; density >4 ppl/m² |
| RR-002 | Operational | Power failure to main stage | 3 | 4 | 12 | Reduce/Transfer | Dual generators + UPS; load test; fuel contract; on-call electrician | Ops Lead | T-10d | 2/3/6 | In Progress | Voltage dips; fuel delay notice |
| RR-003 | Environmental | Waste overflow causing fines and complaints | 3 | 3 | 9 | Reduce | 30% more bins; staffed eco-stations; vendor waste plan; hauler on standby; signage | Sustainability Lead | T-7d | 2/2/4 | In Progress | Bin fill >80%; wind forecast on site |
| RR-004 | Legal/Compliance | Public assembly permit delayed or rejected | 2 | 5 | 10 | Reduce/Avoid | Early submission; completeness check; pre-meet authority; alternate venue layout | Legal Counsel | T-30d | 1/4/4 | Open | Authority request for info |
| RR-005 | IT/Cyber | Ticketing platform outage on event day | 2 | 4 | 8 | Reduce/Transfer | Offline lists; handheld scanners; hot-spot backup; vendor SLA penalties | IT Lead | T-5d | 1/3/3 | In Progress | Latency >500ms; vendor status amber |
| RR-006 | Financial | Sponsor withdraws within 2 weeks | 2 | 4 | 8 | Transfer/Reduce | Contract with withdrawal penalties; backup sponsor list; adjust deliverables | Finance Controller | T-21d | 1/3/3 | Open | Late payment; reduced engagement |
| RR-007 | Safety | Severe weather (wind >25 mph) impacting structures | 3 | 5 | 15 | Avoid/Reduce | Engineering sign-off; wind action plan; anemometers; staged shutdown criteria | HSE Manager | T-10d | 2/4/8 | In Progress | Forecast gusts >20 mph |
| RR-008 | Reputational | Social media backlash over accessibility | 3 | 3 | 9 | Reduce | Accessibility audit; ASL interpreters; clear access info; feedback channel | Comms Lead | T-12d | 2/2/4 | In Progress | Complaints >3/day |
| RR-009 | Vendor/Supply | Catering vendor no-show or shortfall | 2 | 4 | 8 | Reduce/Transfer | Secondary vendor on call; stock buffer; service-level clauses | Vendor Manager | T-7d | 1/3/3 | Open | Delivery ETA slips |
| RR-010 | Legal/Privacy | Data breach of attendee PII | 2 | 5 | 10 | Reduce/Transfer | MFA; encryption; DPA with vendor; incident response plan; DPIA | IT Lead | T-14d | 1/4/4 | In Progress | Unusual access logs |

Key: L = Likelihood, I = Impact, S = Score, T-#d = days before event.

## Safety, Legal & Sustainability Checkpoints (Incorporate as Risks/Controls)
Safety (examples; verify local requirements):
- Crowd safety: maximum density ≤4 persons/m²; ingress/egress flow plan; egress routes clear; steward ratios aligned with expected attendance; radio channels and backup power.
- Structures: engineered sign-off for stages/truss; wind and weather action thresholds; daily inspection logs.
- Fire: extinguishers by risk; no-smoking controls; hot works permits; evacuation routes; trained marshals.
- Medical: minimum coverage guideline often ≥1 first aider per 250 attendees (check local law); AEDs; ambulance access; medical control point; incident reporting.
- Emergency: integrated Emergency Response Plan (ERP), including evacuation, shelter-in-place, missing child, security threat, severe weather, and comms templates.

Legal/Compliance:
- Permits/licenses: public assembly, temporary structures, noise, food handling, alcohol, street closure, signage, drone/UAS, pyrotechnics (as applicable).
- Contracts: indemnity, insurance requirements, force majeure, safety and sustainability clauses, SLAs, data processing agreements.
- Insurance: public liability, employer’s liability/workers’ comp, event cancellation/weather, equipment, cyber.
- Privacy: GDPR/CCPA where applicable; purpose limitation; consent where required; data minimization; retention schedule; privacy notice and secure deletion post-event.
- Accessibility: ADA/local accessibility compliance; ramps, viewing platforms, toilets, communication access.

Sustainability:
- KPIs: waste diversion % (target ≥70%), energy use (kWh or fuel liters), travel emissions (tCO2e), water consumption, reusable/recyclable share, food waste diverted/donated.
- Actions: LED lighting; generator right-sizing and HVO/biofuel options; refill water stations; no single-use plastics where possible; reuse stage materials; sustainable procurement; local suppliers; carbon reporting and offsetting hierarchy (avoid > reduce > offset).
- Compliance/standards: align with ISO 20121 (sustainable events) and ISO 14001 practices as feasible.

## Timeline and Governance
- T–12 weeks: Kickoff risk workshop; set up register and scales; identify top 20 risks.
- T–10 weeks: Baseline register approved; assign owners and due dates.
- T–8 to T–2 weeks: Weekly risk reviews; update heat map; test critical controls (power, comms, medical).
- T–1 week: Daily risk huddles; confirm permits/insurance; finalize ERP; readiness checks with vendors.
- Event Day(s): Live risk monitoring, logs, and twice-daily leadership updates; immediate escalation for High risks.
- T+1 week: Post-event review; close items; update lessons and controls library; archive register.

## References or Templates

Standards and guidance (for orientation; verify local laws):
- ISO 31000: Risk Management — Principles and Guidelines
- ISO 45001: Occupational Health & Safety Management
- ISO 20121: Sustainable Events Management
- ISO 14001: Environmental Management
- NFPA 101 Life Safety Code (where applicable)
- Local authority permitting guides and building/fire codes
- Data protection regulations (e.g., GDPR/CCPA)

Template: Risk Register CSV (copy into a sheet)
Risk ID,Category,Risk Statement,Cause,Consequence,Likelihood (1-5),Impact (1-5),Inherent Score,Inherent Rating,Treatment Strategy,Mitigation Actions,Contingency/Response,Owner,Due Date,Status,Early Warning Indicators,Linked Controls,Budget Impact (USD),Residual Likelihood,Residual Impact,Residual Score,Residual Rating,Dependencies,Last Reviewed,Notes
RR-001,Safety,"Crowd crush at main entrance","Single entry bottleneck","Serious injury, media scrutiny, fines",3,5,,,"Reduce","Staggered entry; add lanes; density monitoring; staff training","Hold gates; activate overflow queuing; pause transport inflow","HSE Manager",2025-09-05,In Progress,"Queue >50m; density >4/m2","Crowd plan v2; steward SOP",4500,2,4,,,"Venue staffing; barrier delivery",2025-08-20,""
RR-002,Operational,"Power failure to main stage","Single generator dependency","Show stoppage; refunds; safety concerns",3,4,,,"Reduce/Transfer","Dual gens + UPS; load test; fuel contract","Switch to backup; partial stage shutdown","Ops Lead",2025-09-01,In Progress,"Voltage dips; fuel delay","Redundant power design",8200,2,3,,,"Generator vendor; fuel supplier",2025-08-20,""

Add formulas in your sheet for Inherent/Residual Scores and Ratings as described above.

Heat Map Setup (Google Sheets/Excel):
- Insert Pivot Table from Risk Register.
- Rows: Likelihood (1–5). Columns: Impact (1–5). Values: COUNT of Risk ID (Status not equal to Closed).
- Add a helper table with Score = Row x Column to apply red/amber/green conditional formatting.
- Display totals for High (≥15), Medium (8–14), Low (≤7).

Controls Library (examples):
- Preventive: “Wind action plan v1.2,” “Ticketing SLA with 99.9% uptime,” “Food safety SOP,” “Waste management plan,” “Accessibility pathway map”
- Detective: “Real-time queue monitoring feed,” “Anemometer alerts at 20/25/30 mph,” “Power load meter alarms”
- Corrective: “Stage partial shutdown SOP,” “Medical incident response flow,” “Cyber incident response runbook”

Reporting Templates:
- Weekly Risk Summary: top 10 risks, heat map snapshot, new/closed risks, overdue actions, decision requests.
- Event-Day Risk SitRep: changes to High/Medium risks, incidents, control status, next 12-hour outlook.

Notes and reminders:
- Keep entries concise but specific; avoid vague mitigations.
- Assign one accountable owner per risk.
- Use Early Warning Indicators to trigger proactive actions (e.g., thresholds, vendor alerts, forecast metrics).
- Reassess Residual Risks after mitigations and before event go/no-go decisions.

If you need an editable spreadsheet, create a new workbook with the sheets and fields above, copy in the CSV header, and paste the example rows. Apply formulas and conditional formatting per this guide.