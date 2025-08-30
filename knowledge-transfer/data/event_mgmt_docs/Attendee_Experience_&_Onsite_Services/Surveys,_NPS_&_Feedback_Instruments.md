# Surveys, NPS & Feedback Instruments
Attendee Experience & Onsite Services

Document title: Surveys, NPS & Feedback Instruments  
Document description: Establishes survey design, timing (in-app, onsite, post), incentives, and reporting. Format: question bank, distribution plan, and analytics template.

---

## Overview

This playbook defines how to design, deploy, and analyze attendee feedback for events, with a focus on onsite services and attendee experience. It includes:

- A question bank (NPS, CSAT, CES, session and service feedback)
- Distribution plan (in-app, onsite, post-event)
- Incentives strategy and compliance
- Analytics and reporting templates
- Roles, timelines, and dependencies

Primary objectives:

1. Measure overall event advocacy (NPS), satisfaction (CSAT), and effort (CES).
2. Capture actionable insights on onsite operations (registration, wayfinding, F&B, accessibility, help desk, safety, transportation).
3. Validate content/session quality and speaker performance.
4. Identify detractor pain points in near real-time for same-day remediation.
5. Provide executive-ready reporting within 7 days post-event.

Scope: Applies to live, hybrid, and virtual events of 200–10,000 attendees.

---

## Key Details and Steps

### 1) Timeline

- T–8 weeks: Define objectives, KPIs, segments, and data schema; draft surveys.
- T–6 weeks: Translations and accessibility review; legal/privacy and incentive rules.
- T–4 weeks: Build surveys in tools; integration tests (app, CRM, BI).
- T–3 weeks: Pilot with 30 internal/external testers; revise timing and copy.
- T–2 weeks: Finalize distribution plan; confirm kiosk hardware; print signage with QR codes.
- T–1 week: Load attendee tokens; QA all links, logic, routing; seed test responses.
- Event days: Run micro in-app and onsite pulse checks; daily reporting at 5 p.m. local.
- T+1 day: Send post-event survey (primary); monitor detractor escalations.
- T+7 days: Deliver executive summary and operational improvement plan.
- T+30 days: ROI/behavioral follow-up (e.g., intent to return, purchase influence).

### 2) Survey Types and Timing

- In-app micro surveys (10–30 seconds):
  - Triggers: session exit, after help desk chat, after scanning badge at exhibitor, after using shuttle.
  - Goal: immediate, contextual CSAT/CES.
- Onsite quick feedback:
  - Kiosk/tablet near registration, food stations, session exits with 1–3 questions.
  - QR codes on signage and table tents.
- Post-event (primary survey, 5–7 minutes):
  - Sent at T+24 hours; reminder at T+72 hours; final reminder at T+6 days.
  - Sections: overall NPS/CSAT, onsite services, content, app/tech, sponsors/networking, open ends.
- Follow-up (T+30 days, 2–3 minutes):
  - Net impact, value realization, intent to return, referrals.

Frequency caps:
- Max 1 in-app prompt per attendee per 3 hours; opt-out link included.
- Post-event reminders capped at 2.

### 3) Design Guidelines

- Mobile-first; completion time targets:
  - Micro: ≤30 sec (2–4 items)
  - Session exit: ≤60 sec (3–5 items)
  - Post-event: ≤7 min (max ~20 items with skip logic)
- Scales:
  - NPS: 0–10
  - CSAT: 1–5 (Very dissatisfied to Very satisfied)
  - CES: 1–7 (Very difficult to Very easy)
- Randomize item order within blocks to reduce bias; rotate positive/negative anchors consistently.
- Use skip logic by attendee role, track, and onsite/offsite attendance.
- Accessibility: WCAG 2.1 AA; keyboard navigation; text alternatives; high-contrast themes; large tap targets.
- Localization: Human-reviewed translations; region-specific examples; right-to-left support where applicable.
- Privacy: Minimize PII; state purpose and retention (default 12 months); lawful basis for processing (consent or legitimate interest); offer anonymity option on post-event survey; provide clear privacy notice.
- QA checklist: logic paths, device lab, broken links, timezones, duplicate protections, survey throttling, test data cleared before go-live.

### 4) Sample Size and Targets

- Example event size: N=3,000 onsite attendees.
- Target margins: ±5% at 95% confidence for overall NPS/CSAT → sample ~341 completes.
- Expected response rates:
  - In-app micro: 25–35%
  - Onsite QR/kiosk: 15–25%
  - Post-event email: 18–28% (with incentives)
- Send volume planning: For 20% post-event response, email all attendees; ensure reminders to non-responders only.
- Segment quotas: Minimum 100 completes per key segment for reliable comparisons (e.g., role, region, first-time vs. returning).

---

## Question Bank (Use and Adapt)

Note: Use only what’s needed; limit to essentials and rely on skip logic.

Core (all audiences)
- Q1 NPS: How likely are you to recommend [Event Name] to a friend or colleague? 0–10
- Q1a Why did you give that score? (Open text, required for ≤6; optional for 7–10)
- Q2 Overall, how satisfied are you with your experience at [Event Name]? 1–5 CSAT
- Q3 How likely are you to attend again next year? 1–5 scale (Very unlikely to Very likely)

Onsite Services
- Registration/Check-in
  - How easy was the check-in process? 1–7 CES
  - Wait time at check-in: Under 2 min, 2–5, 6–10, 11–20, 20+ minutes, Not applicable
- Wayfinding/Signage
  - It was easy to find my way around the venue. 1–5 agreement
  - Which areas were hard to find? Keynote hall, Breakouts, Expo, Restrooms, Registration, Other (open)
- Help Desk/Staff
  - Staff were friendly and helpful. 1–5 agreement
  - Did you get your issue resolved at first contact? Yes/No; If no, what was the issue? (open)
- Food & Beverage
  - Satisfaction with food and beverage options. 1–5 CSAT
  - Dietary needs accommodated? Yes fully / Partially / No / Not applicable
- Accessibility
  - Accessibility accommodations met my needs. 1–5 agreement; If not, describe. (open)
- Safety & Security
  - I felt safe at the event. 1–5 agreement
  - Any safety concerns to report? (open; route to Ops if submitted onsite)
- Transportation/Shuttles
  - Shuttle service reliability. 1–5 CSAT
  - Commute time to venue: <10, 10–20, 20–40, 40+ minutes, N/A
- Venue
  - Room comfort (temperature, seating, AV). 1–5 CSAT
  - Wi‑Fi reliability. 1–5 CSAT

Sessions & Content
- Session Exit (triggered)
  - Overall, how satisfied were you with this session? 1–5 CSAT
  - Speaker effectiveness. 1–5
  - Content matched the session description. 1–5 agreement
  - Would you recommend this session to a colleague? Yes/No
  - What could be improved? (open)
- Program-level (post-event)
  - The content was relevant to my interests. 1–5 agreement
  - Balance of foundational vs. advanced content was right. 1–5 agreement

Sponsors, Exhibitors, and Networking
- I found value in visiting sponsors/exhibitors. 1–5 agreement
- Did you make at least one valuable new connection? Yes/No
- Which networking formats worked best? Expo reception, 1:1 meetings, Roundtables, App matchmaking, Other (open)

Technology & App
- The mobile app made it easier to navigate the event. 1–5 agreement
- How easy was it to build your agenda? 1–7 CES
- App reliability (crashes, load times). 1–5 CSAT
- If you contacted support in-app, was it helpful? Yes/No/Open

Sustainability
- The event’s sustainability efforts were visible and meaningful. 1–5 agreement

Value & Outcomes
- The event was worth the time and expense. 1–5 agreement
- Primary outcome achieved: Learned new skills, Met vendors, Closed deals, Met peers, Got certified, Other (open)

Demographics/Segmentation (optional, keep brief)
- Role: Executive, Manager, IC, Student, Other
- Company size: 1–49, 50–249, 250–999, 1,000–4,999, 5,000+
- First-time attendee? Yes/No
- Region: Americas, EMEA, APAC, Other

Open Text
- What is one thing we should keep doing? (open)
- What is one thing we should change for next year? (open)

Micro/Kiosk Variants (≤3 taps)
- How satisfied are you with [location/service]? Very satisfied / Satisfied / Neutral / Dissatisfied / Very dissatisfied
- How easy was this? Very easy / Easy / Neutral / Difficult / Very difficult
- Smiley scale (5-point) for instant CSAT at exits

Routing examples:
- If NPS ≤6 and contact consent given, create service ticket.
- If dietary needs = Not accommodated → route to catering lead same day.

---

## Distribution Plan

Channels and triggers
- In-app:
  - Session exit: Trigger survey when attendee leaves session or after 45 min attendance.
  - Help desk/chat: Prompt 5 minutes post-resolution.
  - Exhibitor scan: Prompt after 2nd unique scan to avoid spamming.
- Onsite:
  - Kiosks/tablets at registration, info desk, session exit, food stations; staff invite participation.
  - QR codes on signage: “Tell us how we did—15 seconds” with short vanity URL and UTM tags.
- Email:
  - Post-event T+24 hours; reminders at T+72 hours and T+6 days.
  - Use unique, tokenized links to pre-fill name/role and prevent duplicate responses.
- SMS (where permitted):
  - Opt-in required at registration; send only the post-event link once.

Sample copy
- Push (session exit): “Got a minute? Rate ‘Kubernetes Deep Dive’ to help us improve.”
- Email subject (T+24h): “2–3 minutes: Help us improve [Event Name] + chance to win [Incentive]”
- SMS: “[Event Name]: Quick feedback on your experience. 3-min survey: {short.link}. Reply STOP to opt out.”

UTM and token scheme
- utm_source: app/email/sms/kiosk/qr
- utm_medium: push/edm/sms/onsite
- utm_campaign: eventYYYY_feedback
- token: attendee_id + event_id signed JWT or secure GUID

Sampling
- Send to all attendees for post-event; use channel randomization (e.g., 50% push, 50% email reminders) to compare channel performance.
- For micro-surveys, cap at 3 prompts per day per attendee; prioritize unique touchpoints.

---

## Incentives

Options and guidance
- Micro in-app/onsite: Instant reward (e.g., $5 coffee voucher in-app wallet) for first 1,000 completes; budget $5,000.
- Post-event: Raffle 3× $250 gift cards; alternate equivalent value items for regions where gift cards are restricted.
- Compliance:
  - Publish Official Rules and eligibility (no purchase; odds; start/end; drawing date).
  - Exclude government employees and any restricted professions as required.
  - Tax reporting where applicable; prize acceptance via form with consent.
- Equity:
  - Offer non-monetary alternative (e.g., donation to charity per complete) for those who decline personal incentives.

---

## Reporting and Analytics

Cadence
- Daily pulse (event days): 5 p.m. local distribution to Ops and Experience leads.
- T+7 Executive summary: Narrative, KPI dashboard, key drivers, actions.
- T+30 Impact memo: Changes implemented and follow-up metrics.

Core metrics
- NPS: %Promoters (9–10) – %Detractors (0–6)
- CSAT by touchpoint: mean and top-2 box (%4–5)
- CES: mean; %reporting easy (6–7)
- Response rate, completion rate, median completion time
- Drop-off by question, device mix, channel performance
- Segment performance: role, region, first-time vs. returning
- Text analytics: top themes, sentiment, word cloud

Alerting and detractor handling
- If NPS comment contains keywords (e.g., “unsafe,” “accessibility,” “harassment”): auto-create ticket in Zendesk/ServiceNow; SLA:
  - Critical safety/accessibility: 1-hour triage; 3-hour resolution or update.
  - Other detractors: outreach within 24 hours.
- Promoters (9–10): trigger thank-you email; optionally invite to testimonial or referral program.

Sample KPI targets (example)
- Overall NPS: +45
- Overall CSAT: 4.5/5
- Check-in CES: ≥6.2/7
- Wi‑Fi CSAT: ≥4.0/5
- Post-event response rate: ≥22%
- Session average CSAT: ≥4.4/5

Data retention and governance
- Retain raw responses 12 months; anonymize free-text after 90 days for long-term benchmarking if needed.
- Access roles: least privilege; PII encryption at rest and in transit.
- Right to access/erasure process documented.

---

## Responsibilities

- Attendee Experience Lead (Owner)
  - Define objectives/KPIs; approve question set; oversee execution and daily pulse actions.
- Research & Insights Analyst
  - Survey design, sampling, bias control; build and QA; analysis and reporting.
- Marketing Operations
  - Email/SMS deployment; tokenized links; UTM tagging; deliverability; reminder logic.
- Onsite Operations Manager
  - Kiosk setup; signage; staff training; daily hardware checks; sanitation and battery rotation.
- Technical PM / App Vendor Manager
  - App triggers; SDK/config; SSO/token integration; offline fallback.
- Data/BI Analyst
  - ETL to data warehouse; dashboard build (Tableau/Power BI); maintain data dictionary.
- Legal/Privacy Officer
  - Consent text; privacy notice; incentive rules; regional compliance.
- Catering & Venue Leads
  - Act on F&B and room comfort insights; post daily changes.
- Speaker Management
  - Distribute session feedback to speakers; coordinate coaching if needed.
- Sponsor/Exhibitor Liaison
  - Share aggregated expo insights; manage sponsor NPS and actions.

Escalation path
- Critical issues → Experience Lead → Ops Director within 30 min; Safety/Security looped immediately if relevant.

---

## Dependencies

- Event app platform supports:
  - Session exit triggers, push notifications, deep links, and offline caching.
- Registration/CRM integration for attendee tokens and segments.
- Wi‑Fi bandwidth and LTE coverage at kiosk locations.
- Legal review of incentives and data processing agreements with vendors.
- Procurement of gift cards or digital vouchers (lead time 2 weeks).
- Translation services (lead time 10 business days).
- BI tooling and data warehouse access; API keys for survey platform.
- Signage production (QR codes, vanity URLs); print lead time 5–7 business days.

---

## Onsite Execution Checklist

Hardware and placement
- 8–12 tablets with stands; locked to survey URL; auto-refresh; privacy screen filters.
- Portable battery packs; nightly charging schedule.
- Locations: Registration exit, Info desk, Top 5 session rooms, Expo hall entrance/exit, F&B areas.

Signage and prompts
- A-frame and counter cards with QR codes; copy: “Tell us in 15 seconds. Help us improve today.”
- Staff spiels: “Quick 2-tap survey helps us fix things same day. Thank you!”

Operational routines
- 3x daily check: battery >60%, Wi‑Fi, page load, sanitizer wipes.
- Daily 2 p.m. huddle: review pulse data; implement quick wins (e.g., add signage, adjust temp).

Offline fallback
- Paper cards with 5-point smiley scale and comment box; scanned and keyed-in by volunteers at day-end.

---

## References and Templates

Survey platform settings (example)
- Tool: Qualtrics/SurveyMonkey/Typeform (any modern platform)
- Settings: IP de-duplication on; prevent multiple completes per token; save & resume off for micro, on for post-event.

Email templates
- T+24h Subject: “Your feedback shapes next year’s [Event Name]”
- Body: Personalized greeting; 3 bullets on time commitment and why it matters; primary CTA; secondary plain-link; privacy link; unsubscribe.

Push notification schedule
- Morning reminder at 9:45 a.m.; session exit prompts within 5 minutes; avoid keynote start times.

Privacy notice (inline example)
- “We collect your feedback to improve event operations and content. Responses may be linked to your registration profile for analysis. View our Privacy Policy. You can request deletion at any time.”

Signage QR template components
- QR points to shortlink event.com/fb
- UTM parameters by location: utm_source=onsite&utm_medium=qr&utm_content=location_code

---

## Analytics Template (Copy into BI or Spreadsheet)

Dashboard sections

1) Executive Summary
- Overall NPS: +48 (Target +45) – Up 6 points vs. last year
- CSAT Overall: 4.6/5 (Target 4.5)
- Top drivers of satisfaction: Check-in speed, staff helpfulness, session relevance
- Top issues: Wi‑Fi reliability in Hall B, vegetarian options at Lunch Day 1

2) KPI Table
- Metric: Overall NPS; Definition: %9–10 − %0–6; Target: +45; Result: +48; Status: Green
- Metric: Overall CSAT; Definition: Mean 1–5; Target: 4.5; Result: 4.6; Status: Green
- Metric: Check-in CES; Definition: Mean 1–7; Target: 6.2; Result: 6.0; Status: Amber
- Metric: Wi‑Fi CSAT; Definition: Mean 1–5; Target: 4.0; Result: 3.6; Status: Red
- Metric: Post-event response rate; Definition: Completes/Sent; Target: 22%; Result: 24%; Status: Green

3) Segment NPS Snapshot (examples)
- First-time attendees: +42 (n=380)
- Returning attendees: +54 (n=290)
- APAC: +40 (n=110), EMEA: +46 (n=180), Americas: +50 (n=360)

4) Channel Performance
- In-app micro: 1,240 prompts; 420 completes; 34% conversion; median time 21 sec
- Onsite QR: 780 scans; 150 completes; 19% conversion
- Email post-event: 2,900 sent; 24% open; 9% click; 24% complete rate among clickers

5) Question-level Diagnostics
- Completion rate: 92%; median duration: 5m 12s; drop-off spike at Q14 (F&B open-end)
- Device mix: 72% mobile, 24% desktop, 4% tablet

6) Text Themes (top 5)
- “Wi‑Fi” (negative, 62 mentions)
- “Check-in fast” (positive, 54)
- “Signage confusing” (negative, 31)
- “Great speakers” (positive, 80)
- “Vegetarian options” (negative, 25)

7) Actions Log
- Day 1 2:30 p.m.: Added Wi‑Fi extenders to Hall B – Wi‑Fi CSAT improved from 3.2 to 3.9 by Day 2.
- Day 2 11:00 a.m.: Increased vegetarian stations – F&B CSAT from 3.8 to 4.3.

Data dictionary (fields)
- attendee_id (string), event_id (string), session_id (string, nullable), timestamp_local (datetime), channel (enum), nps_score (int), csat_touchpoint (1–5), ces_score (1–7), comment_text (text), language (string), segment_role (enum), segment_region (enum), consent_marketing (bool)

---

## Example Session Exit Survey (Micro)

- Q1 Overall, how satisfied were you with this session? 1–5
- Q2 The content matched the description. 1–5
- Q3 Speaker effectiveness. 1–5
- Q4 What could be improved? (optional open, ≤140 chars)

Total: ~30–45 seconds. Trigger: session exit. Frequency cap: 2 per day.

---

## Risk Log and Mitigations

- Low response rate → Add on-the-spot prompts; increase incentive; shorten survey; time send earlier in day.
- Wi‑Fi outages at kiosks → Enable offline mode; rotate to LTE hotspots; paper fallback.
- Deliverability issues → Warm sender domain; authenticate (SPF/DKIM/DMARC); resend to non-openers with new subject.
- Bias from over-sampling power users → Apply channel caps; weight responses by attendance patterns.
- Privacy complaints → Clear consent language; quick opt-out; provide deletion request process.

---

## Quick Start (If You’re New)

- Clone last event’s survey in the platform.
- Replace event branding and update objectives/KPIs.
- Select 15–20 questions max for post-event with skip logic; enable NPS and core CSAT/CES.
- Configure app triggers for session exit and help desk.
- Print 20 QR signs; deploy 8 tablets at high-traffic areas.
- Set up T+24h email; add 2 reminders; load incentives.
- Verify data flows to BI; schedule daily 5 p.m. pulse report.
- Brief onsite staff to invite feedback and note issues for same-day fixes.

---

End of document.