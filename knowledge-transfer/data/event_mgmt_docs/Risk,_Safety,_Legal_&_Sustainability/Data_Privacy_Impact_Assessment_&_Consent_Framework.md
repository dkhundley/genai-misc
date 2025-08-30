# Data Privacy Impact Assessment (DPIA) & Consent Framework

Document type: Operational playbook, DPIA report template, data flow diagram, and consent language library  
Topic: Risk, Safety, Legal & Sustainability  
Audience: Product, Engineering, Legal/Privacy, InfoSec, Marketing, Vendor Management

Note: This document provides operational guidance and templates. Consult your legal counsel for jurisdiction-specific advice.

---

## Overview

Purpose:
- Provide a repeatable, end-to-end approach to assess and mitigate privacy risks for any processing of personal data (PII/Personal Data), including cross-border transfers and vendor use.
- Establish a consent framework that is user-friendly, compliant across major regimes (GDPR/UK GDPR, CPRA, ePrivacy, LGPD, CASL, CAN-SPAM, COPPA/UK AADC), and auditable.
- Embed sustainability by minimizing data collection and storage, thereby reducing energy use and environmental impact.

When to use:
- New product or feature that collects or infers personal data.
- New vendor or sub-processor with access to personal data.
- New or changed data transfer across borders (e.g., EEA/UK → US).
- Processing sensitive data or data of minors.
- Significant change to retention, analytics, or marketing stack.
- Annual re-assessment for high-risk processing.

Definitions (plain terms):
- Controller: Decides why and how personal data is processed.
- Processor: Processes data on behalf of a controller.
- Personal data (PII): Any data relating to an identified or identifiable person.
- Special/sensitive data: e.g., health, biometrics, precise location, racial/ethnic origin, political opinions.
- Consent: Freely given, specific, informed, unambiguous indication (explicit if sensitive data).
- DPIA: Formal assessment of risks to individuals and mitigations.

Timeline (typical):
- Discovery & data mapping: 5–10 business days
- Legal bases & controls design: 5–7 business days
- Vendor/DPA & transfer assessments: 5–7 business days
- UX/consent implementation & testing: 5–10 business days
- Sign-offs & launch gates: 2–3 business days
Total: ~4–6 weeks; fast track minor changes in ~2 weeks if low risk.

---

## Key Steps

1) Initiation and Scoping
- Assign a Processing Owner (usually the Product Manager) and a Privacy Lead (DPO or Privacy Counsel).
- Record basic facts:
  - Name: “Customer Insights Analytics v2”
  - Processing purpose: measure product usage and personalize in-app tips
  - Jurisdictions: EU/UK, US, Canada, Brazil, Australia
  - Data subjects: prospects, customers, admin users
  - Systems/vendors: Web app, mobile app, Snowflake, Segment, Google Analytics 4 (BigQuery export), Braze, Zendesk
  - Launch target: 2025-10-15
- DPIA trigger? Yes if any of: large-scale tracking, sensitive data, cross-border transfers, novel tech, minors, automated decision-making with legal effects.

2) Data Mapping and Flow Diagram
- Inventory data elements and sources, identify storage locations, and depict flow. Example flow (textual):
  - User Browser/Mobile App
    -> CDN (edge logs, IP, user agent)
    -> Web App Frontend (first-party cookies, device ID)
    -> API Gateway (TLS, rate-limiting)
    -> App Service (user ID, email, preferences)
    -> Auth Provider (OIDC; tokens; IP)
    -> Primary DB (PostgreSQL; account profile, hashed password)
    -> Event Collector (Segment) (event name, timestamp, pseudonymous ID)
    -> Analytics (GA4 with BigQuery export; region: EU)
    -> Marketing (Braze; email, consent flags)
    -> CRM (Salesforce; lead and opportunity data)
    -> Support (Zendesk; tickets may include PII)
    -> Data Warehouse (Snowflake; EU region for EEA/UK data)
    -> BI Tool (read-only; role-based access)
- For each node, record: purpose, data categories, retention, access roles, location, and security controls.

3) Identify Purposes, Legal Bases, and Necessity
- Example mapping:
  - Account creation and service delivery: contract necessity (GDPR Art. 6(1)(b)); retention 2 years after inactivity.
  - Security/fraud detection: legitimate interests (Art. 6(1)(f)); conduct Legitimate Interests Assessment (LIA).
  - Product analytics (non-essential): consent in EU/UK (ePrivacy + GDPR), opt-out in US (CPRA “Do Not Sell/Share” if adtech identifiers shared).
  - Marketing emails/SMS: consent (GDPR/CASL); opt-out acceptable under CAN-SPAM but use opt-in globally for consistency.
  - Personalization using behavioral data: consent in EU/UK; LIA outside EU if strictly necessary and proportionate.
  - Children (<16 EU default, adapt per country; <13 US): parental consent and age-appropriate design controls.
- Necessity/proportionality: minimize data collected; avoid sensitive categories unless strictly necessary; consider on-device processing.

4) Risk Assessment (Rights and Freedoms)
- Risks to individuals: unauthorized access, unanticipated secondary use, re-identification, bias/discrimination, cross-border surveillance, profiling without transparency, data breach harms.
- Scoring model (1–5 scale):
  - Impact: 1 negligible → 5 severe (financial loss, discrimination, safety risk).
  - Likelihood: 1 rare → 5 very likely.
  - Risk rating = Impact x Likelihood; High ≥ 12.
- Example:
  - Cross-border analytics (EEA→US): Impact 3, Likelihood 3 = 9 (Medium); mitigations may reduce to 6.
  - Behavioral profiling for marketing: Impact 3, Likelihood 4 = 12 (High); require explicit consent and easy opt-out, transparency.

5) Controls and Mitigations
- Technical:
  - Encryption in transit (TLS 1.2+) and at rest (AES-256).
  - Pseudonymize analytics identifiers; separate keys stored in EU HSM/KMS.
  - Data minimization: collect only event names and coarse timestamps; redact PII from logs by default.
  - Access control: SSO + MFA, least privilege, quarterly access reviews.
  - Differential access tiers: production vs analytics sandbox; prohibition of direct PII in analytics tables.
  - Data retention enforcement: lifecycle policies and automated deletion, including backups.
  - Anonymization for reporting; privacy checks in CI/CD (schema linting).
- Organizational:
  - Privacy by design checklist in PRD; change management gates.
  - Vendor DPAs and TIAs before enabling data flows.
  - Training annually for staff with data access.
  - Incident response runbooks and playbooks, including 72-hour GDPR reporting.
- UX/Transparency:
  - Layered privacy notices; just-in-time notices on collection points.
  - Consent and preference center with purpose-level granularity and global application across devices.
  - Avoid dark patterns; equal prominence for “Reject” and “Accept”.

6) Vendor Management and DPA
- DPA needed if vendor processes personal data as a processor.
- Minimum DPA terms:
  - Process only on documented instructions; confidentiality; security measures (TOMs).
  - Subprocessor control and notice; flow-down obligations.
  - Assistance with data subject rights, DPIA, and breach notifications (e.g., within 48 hours of discovery).
  - Deletion/return on termination; audit rights; data localization options.
- Verify vendor posture:
  - SOC 2 Type II or ISO 27001, penetration tests, security whitepaper.
  - Data residency; encryption; key management; incident response.
  - Ability to support SCCs/UK IDTA and purpose-specific processing.

7) Cross-Border Transfers and TIA
- Identify transfers (e.g., EEA/UK personal data → US analytics, support, marketing).
- Transfer tools:
  - EU SCCs Modules 2 (controller-processor) and 3 (processor-processor).
  - UK IDTA or UK Addendum to SCCs.
  - For Brazil (LGPD): contractual clauses + adequacy where available.
- TIA elements:
  - Map data, purposes, sensitivity, volumes.
  - Assess destination country laws (government access risks, redress).
  - Supplementary measures:
    - Strong encryption; keys controlled in EEA/UK.
    - Data minimization and pseudonymization.
    - Split processing (EU data stays in EU warehouse; only aggregated metrics exported).
- Decision: proceed if residual risk acceptable and documented by DPO.

8) Retention and Deletion Schedule (examples)
- Account data (name, email, login): active lifecycle + 24 months after last activity; backups: 90 days rolling.
- Billing records: 7 years (tax/audit).
- Support tickets: 24 months, then anonymize conversation text.
- Marketing leads without engagement: 12 months, then delete.
- Analytics events: 13 months (EU default to align with ePrivacy norms) or less if possible.
- Device identifiers/cookies: expire after 6–13 months; set lower where feasible (e.g., 6 months).
- Implement automated policies; verify deletion in data warehouse and vendor systems.

9) Consent Framework (Web, Mobile, Offline)
- Principles: specific, granular per purpose; affirmative action; no pre-ticked boxes; easily withdrawable; documented.
- Purposes to present at minimum:
  - Strictly necessary (no consent).
  - Analytics (non-essential).
  - Personalization.
  - Marketing communications (email, SMS, push).
  - Advertising/retargeting and “sharing” (CPRA).
  - Precise geolocation (sensitive).
- Web:
  - CMP with geo-based rules: in EU/UK, block non-essential scripts until consent. Provide Accept All / Reject All / Manage Options at equal prominence.
  - Cookie list and vendor disclosure; store consent with timestamp, jurisdiction, and version.
- Mobile:
  - Present system prompts (e.g., iOS ATT) aligned with in-app just-in-time notices; implement SDK gating until consent.
  - Purpose toggles in settings; sync with backend.
- Email/SMS:
  - Double opt-in in EU/Canada; record source, time, IP. One-click unsubscribe and preference center links in every message.
- Offline/events:
  - Paper or tablet forms must mirror consent language; provide copy of notice; capture proof of consent.

10) Data Subject Rights (DSR) Handling
- Intake via portal/email; verify identity proportionate to request.
- Timelines:
  - GDPR/UK: 1 month (extendable by 2 months for complexity).
  - CPRA: 45 days (extendable by 45 days with notice).
- Supported rights: access, rectification, erasure, restriction, portability, objection, opt-out of sale/share, limit SPI.
- Log requests and outcomes; propagate downstream to processors; confirm deletion in backups when feasible or note technical limits.

11) Testing, Launch Gates, and Monitoring
- Pre-launch checks:
  - DPIA completed; DPO/Privacy Counsel sign-off.
  - DPA signed with vendors; SCCs/IDTA in place; TIA recorded.
  - Consent UX QA across devices and locales; scripts blocked until consent where required.
  - Telemetry verified for minimization and no PII leakage in URLs/logs.
- Post-launch:
  - Metrics: consent opt-in rates by region; DSR SLA adherence; deletion job success; access review completion.
  - Audits: quarterly review of purposes and vendor list; annual DPIA refresh for high-risk processing.
  - Incident response drills bi-annually.

12) Breach Response (summary)
- Detect, contain, eradicate; assess risk to individuals.
- Notify supervisory authority within 72 hours (GDPR) if risk; notify affected individuals when high risk.
- Coordinate with vendors per DPA; maintain evidence and timelines.

13) Sustainability Considerations
- Minimize data points, sampling analytics where possible.
- Shorter retention reduces storage/compute.
- Prefer regional processing to reduce long-haul transfers.
- Choose cloud regions/data centers with published renewable energy mix.
- Avoid heavy third-party tracking; prefer first-party, on-device processing.

---

## Responsibilities

- Product/Processing Owner
  - Owns DPIA initiation, scope, timelines, and implementation of mitigations.
- Privacy Lead (DPO/Privacy Counsel)
  - Advises on lawful bases, consent, DPAs; signs off DPIA and TIAs.
- Security Lead
  - Defines technical controls, reviews vendor security, approves architecture.
- Engineering Lead
  - Implements data minimization, retention automation, consent gating; maintains data flow documentation.
- Marketing Lead
  - Ensures compliant marketing consents; maintains preference center; aligns copy and campaigns.
- Vendor Management/Procurement
  - Ensures DPAs/SCCs/IDTA and risk assessments completed before onboarding vendors.
- Data Analyst/BI
  - Ensures no PII in analytics tables; maintains anonymization; enforces role-based access.
- Customer Support
  - Handles DSR workflows and identity verification; escalates complex cases.
- Compliance/PMO
  - Tracks milestones, evidence, and audit artifacts.

---

## Dependencies

- Records of Processing Activities (RoPA).
- Consent Management Platform (CMP) with geo-targeting and audit logs.
- Identity/SSO and role-based access controls.
- Data catalog/lineage tooling (e.g., OpenLineage, built-in warehouse lineage).
- Legal templates: Privacy Notice, DPA/SCCs/IDTA, TIA and LIA methodologies.
- Secure logging and SIEM for monitoring; ticketing for DSRs.
- Localization resources for consent text and notices.

---

## References or Templates

1) DPIA Report Template (copy/paste)
- Processing Name:
- Owner:
- Summary:
- Scope and Systems:
- Data Subjects:
- Data Categories:
- Purposes and Legal Bases:
- Data Flow Description:
- Necessity and Proportionality:
- Risks to Individuals (with ratings):
- Controls and Mitigations:
- Vendors and DPAs:
- Cross-Border Transfers and TIA Summary:
- Retention and Deletion:
- Consent UX and Records:
- DSR Handling Plan:
- Residual Risk:
- Approvals (Owner, Security, DPO/Legal, Exec if high risk):
- Review Cadence/Next Review Date:

2) Legitimate Interests Assessment (LIA) Outline
- Purpose and benefits to organization/users.
- Necessity test (is there a less intrusive means?).
- Balancing test (impact on individuals, expectations, safeguards).
- Outcome (proceed with safeguards / seek consent instead).

3) TIA Checklist (abridged)
- Data types, volumes, frequency, sensitivity.
- Parties and roles; onward transfers/subprocessors.
- Destination country laws and practices (government access, redress).
- Technical and organizational measures (encryption, key control, access).
- Residual risk and decision; documentation and sign-off.

4) DPA Checklist
- Scope and instructions clearly defined.
- Security measures (TOMs) annexed and specific.
- Subprocessor approval and list transparency.
- Data breach notification timeframes.
- Assistance with DSRs and DPIA.
- Deletion/return of data and verification.
- Audit rights and frequency.
- Transfer mechanism clauses (SCCs/IDTA).

5) Retention Schedule Template
- Category: [Account Data] – Purpose: Service delivery – Retention: [24 months post inactivity]
- Category: [Billing] – Purpose: Legal compliance – Retention: [7 years]
- Category: [Support Tickets] – Purpose: Support – Retention: [24 months then anonymize]
- Category: [Marketing Leads] – Purpose: Marketing – Retention: [12 months no engagement]
- Category: [Analytics Events] – Purpose: Product insights – Retention: [13 months]
- Backup retention and deletion windows stated.

6) Consent Record Schema (example)
- Fields:
  - subject_id (user_id or device_id), jurisdiction, purpose_id, consent_status (granted/denied/withdrawn), timestamp (UTC), source (web/mobile/offline), version (notice CMP version), ip_address, user_agent, evidence_uri (screenshot/hash), processor/vendor_id (if applicable).

7) Consent Language Library (examples; localize as needed)
- Global privacy notice (layered, short form):
  - “We use cookies and similar technologies to provide our service, improve performance, personalize content, and for advertising. Manage your choices anytime in Settings. See our Privacy Notice.”
- Cookie banner (EU/UK; ePrivacy + GDPR):
  - Title: “Your privacy choices”
  - Body: “We use cookies to make our site work and to improve it. You can accept all cookies, reject non-essential cookies, or manage your choices.”
  - Buttons: “Accept all” | “Reject non-essential” | “Manage settings”
  - Categories:
    - Strictly necessary (always active)
    - Analytics (off by default)
    - Personalization (off by default)
    - Advertising (off by default)
- Web form (EU marketing consent):
  - Checkbox (unchecked): “I agree to receive marketing emails about products, services, and events from [Company]. You can withdraw at any time.”
  - Consent proof text: “By ticking, you consent to [Company] processing your personal data for marketing. See Privacy Notice.”
- CPRA Do Not Sell/Share (US-CA):
  - Link text in footer and banner: “Do Not Sell or Share My Personal Information” and “Limit the Use of My Sensitive Personal Information.”
  - Toggle copy: “Turn off sharing of your personal information for cross-context behavioral advertising.”
- SMS (US/CAN):
  - “By entering your number and clicking Subscribe, you agree to receive recurring marketing texts from [Company] at the number provided. Msg & data rates may apply. Reply STOP to cancel, HELP for help. Consent not required to buy. Terms & Privacy.”
- Geolocation (precise):
  - “Allow [App] to use your precise location to show nearby offers. You can change this later in Settings. We will not access your location without your permission.”
- Children (parental consent):
  - “We require a parent or guardian’s permission to create this account. Please provide a parent’s email so we can request consent.”

8) Sample Privacy Notice Clause (purposes and legal bases)
- “We process your personal data to create and manage your account (contract), to secure our services (legitimate interests), and—subject to your consent—for analytics, personalization, and marketing communications. You may withdraw consent at any time without affecting the lawfulness of processing before withdrawal.”

9) Data Flow Diagram Template (describe in text)
- Nodes: Data Subjects → Collection Points → Edge/CDN → Application → Identity/Access → Databases → Event Collection → Analytics → Marketing/CRM → Support → Data Warehouse → BI
- For each edge: define data items, legal basis, storage location, transfer mechanism (if cross-border).

10) Evidence for Audits (keep organized)
- DPIA report and approval
- DPA/SCCs/IDTA signed copies
- TIA and LIA assessments
- Consent capture logs and screenshots
- Retention/deletion job logs
- Access reviews and training records
- Incident response drill records

---

## Example: Mini DPIA Summary (for orientation)

- Processing: Product Analytics and Personalized Tips
- Legal bases: Consent (EU/UK) for analytics/personalization; Contract for service delivery.
- Data: pseudonymous device ID, event names, timestamps, coarse location (country), account ID; no free-text PII in events.
- Vendors: Segment (EU region), GA4 (EU data region controls), Snowflake (EU), Braze (EU data center), Zendesk (US; SCCs + encryption; keys in EU).
- Transfers: EEA/UK → US (Zendesk); SCCs Module 2 + UK Addendum; TIA completed; end-to-end TLS; encryption at rest; limited fields; EU-hosted key management.
- Retention: Events 12 months; consent logs 5 years; support tickets 24 months.
- Risk rating pre-mitigation: 12 (High). Post-mitigation: 6 (Medium).
- Residual risk: Acceptable with consent gating and minimization. DPO sign-off dated 2025-09-15.

---

## Practical Next Steps (90-day plan)

- Weeks 1–2: Kickoff; complete data mapping; draft DPIA; identify vendors; draft consent UX.
- Weeks 3–4: Finalize legal bases; execute DPA/SCCs/IDTA; complete TIA/LIA; implement retention policies.
- Weeks 5–6: Build consent gating in web/mobile; integrate CMP; deploy preference center; QA.
- Weeks 7–8: Access reviews; run incident tabletop; finalize privacy notices; train support on DSRs.
- Weeks 9–10: Pilot release in EU opt-in cohort; monitor opt-in rates and telemetry; adjust copy.
- Weeks 11–12: Global rollout with regional rules; archive evidence; schedule quarterly privacy reviews.

---

This framework provides a complete, actionable pathway to assess privacy risks, implement compliant consent, manage vendors and transfers, and reduce environmental impact through data minimization and smart retention. Use the templates to produce auditable artifacts for each processing activity.