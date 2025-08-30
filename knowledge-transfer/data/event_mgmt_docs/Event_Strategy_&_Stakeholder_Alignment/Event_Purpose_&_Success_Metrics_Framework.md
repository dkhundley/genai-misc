# Event Purpose & Success Metrics Framework
Version: 1.0 | Owner: Event Strategy Lead | Last updated: 2025-08-22

## Overview
This document defines how to set, measure, and report on the business impact of a strategic event. It aligns event goals to corporate strategy, establishes clear success metrics (pipeline, revenue influence, satisfaction), and outlines how data will be captured, analyzed, and acted upon.

Who should use this:
- Event/Field Marketing, Demand Gen, Sales, Marketing Ops, RevOps, Finance, Customer Marketing, and Executive Sponsors.

When to use:
- For annual flagship events, regional roadshows, or partner/customer summits where pipeline and revenue impact are expected.

Expected outputs:
- Approved Event Purpose Statement
- KPI Matrix with targets and measurement methods
- Stakeholder alignment and responsibilities (RACI)
- Reporting cadence and dashboard plan
- Post-event close plan and revenue influence tracking

---

## Event Purpose (Template + Example)
Use this to articulate the “why” and connect to corporate strategy.

Purpose template:
- Business outcome(s): [Pipeline creation | Revenue acceleration | Expansion | Adoption | Brand leadership]
- Target audience: [ICP segments, regions, tiers]
- Value proposition: [Problem, solution narrative, and proof]
- Strategic alignment: [Which corporate OKRs does this event support?]
- Timeframe for impact: [Pre, at-event, 30/60/90/180 days post]
- Primary KPIs: [Top 3–5]
- Guardrails: [Budget, capacity, compliance]
- Go/No-Go criteria: [Must-hit prereqs]

Example purpose statement:
- Business outcomes: Create $3.5M in sourced pipeline and influence $1.2M in Closed-Won revenue within two quarters; drive 10% feature adoption uplift among existing customers; grow brand consideration in EMEA.
- Audience: Enterprise IT and Security leaders at ICP Tier 1–2 accounts in NA/EMEA; key partners.
- Value proposition: Showcase our unified security platform that reduces incident resolution time by 35% and total cost of ownership by 22%.
- Strategic alignment: Supports FY25 OKRs: (1) +25% Enterprise ARR, (2) +30% EMEA expansion, (3) +15% product module adoption, (4) NPS 50+.
- Timeframe: Pre-event (awareness, meetings); Event week (meetings, trials); 30–180 days post (SQLs, pipeline creation, revenue).
- Primary KPIs: Sourced pipeline, influenced revenue, SQLs, show rate and ICP mix, Event NPS/CSAT.
- Guardrails: Total budget ≤ $500k; capacity 1,200 registrations.
- Go/No-Go: ≥5 platinum speakers confirmed and ≥30 Tier-1 accounts registered by T-21 days.

---

## Business Objectives and How They Map to Corporate Strategy
- Pipeline creation: Drive new logo and expansion opportunities to reach ARR growth targets.
- Revenue acceleration/influence: Shorten sales cycles via executive meetings, product validation, and urgency.
- Market expansion: Localized content and press/analyst engagement to enter or grow EMEA.
- Customer expansion & adoption: Hands-on labs and roadmap sessions to drive module upsell and feature adoption.
- Partner ecosystem: Co-sell motions and lead sharing to increase partner-sourced pipeline by X%.
- Brand leadership: Thought leadership sessions to increase share of voice and consideration.

---

## KPI Matrix (Targets and Measurement Methods)
Targets below assume a $500k event budget and Enterprise ICP. Adjust per event tier/region.

| KPI | Definition | Target | Measurement Method & Data Source | Owner | Cadence |
|---|---|---|---|---|---|
| Sourced Pipeline | Sum of opportunity amounts created with Event Campaign as Primary Campaign Source and Stage ≥ 2 within 60 days post-event | $3.5M | Salesforce (Campaigns, Opportunities); Campaign hierarchy; Opp filters; QA by RevOps | RevOps | Weekly (T+1 to T+8 weeks) |
| Influenced Revenue | Closed-Won revenue where Event Campaign is a touchpoint per chosen attribution model within 2 quarters post-event | $1.2M | Multi-touch attribution (e.g., W-shaped in Bizible/Marketo Measure); Salesforce; Finance validation | Marketing Ops + Finance | Monthly (through Q+2) |
| SQLs | Sales-accepted opportunities created from event-sourced leads or meetings | 180 | Lead status transitions, MQL→SAL→SQL tracking in CRM; Sales Ops acceptance rules | SDR Manager | Weekly |
| Meetings Booked | Net new logo meetings booked with ICP Tier 1–2 accounts at or within 14 days after event | 120 | Calendaring tool + CRM tasks tagged to Event Campaign; Onsite scans + meeting scheduler | Event Lead + SDR Manager | Daily during event; weekly post |
| Registrations | Total registrants; include ICP % and region mix | 1,200 (≥60% ICP; NA:EMEA 60:40) | Registration platform (Cvent/ON24) with firmographic enrichment (Clearbit/6sense) | Event Ops | Weekly (pre), daily (T-7 to event) |
| Attendance (Show Rate) | Unique attendees / registrants | 67% | Badge scans/virtual attendance; de-dupe and bot filters | Event Ops + MOPs | Daily during event |
| Session Engagement | Avg. session dwell time and CTA clicks | ≥22 min avg; ≥12% CTA CTR | Session platform analytics; UTM tracking | Content Lead + MOPs | Event week + T+1 |
| Trials/POCs Started | Trials/POCs initiated from attendees within 30 days post | 70 trials/POCs | Product analytics + CRM trial field; UTM/campaign ID | Product Growth + MOPs | Weekly (T+1 to T+4) |
| Customer Expansion Pipeline | Expansion opps created with event touchpoint | $800k | Salesforce opp type = Expansion; attribution touchpoint | Customer Marketing + CS Ops | Bi-weekly |
| Event NPS | “How likely to recommend this event?” (0–10) | ≥45 | Post-event survey (Qualtrics); NPS calculation | CX Research | T+3–10 days |
| CSAT (Overall) | 5-point satisfaction rating | ≥4.4/5 | Post-event survey | CX Research | T+3–10 days |
| Speaker & Content Rating | Avg. session rating | ≥4.3/5 | Session survey | Content Lead | Event week + T+7 |
| Sponsor Satisfaction | 5-point rating; lead delivery | ≥4.3/5; ≥200 MQL-equivalent leads to sponsors | Sponsor survey; lead reports | Partner Marketing | T+7 and T+30 |
| Follow-up SLA Compliance | % prioritized leads actioned within 3 business days | 100% | CRM task completion; SLA dashboard | SDR Manager | Daily (T+1 to T+10) |
| ROMI | Pipeline $ / Total Event Cost (and Revenue $ / Cost at Q+2) | ≥7:1 (pipeline); ≥2.4:1 (revenue influence by Q+2) | Cost sheet (Finance) + pipeline/revenue | Finance + RevOps | T+14; Monthly thereafter |

Notes:
- Attribution model: W-shaped (30% first touch, 30% lead creation, 30% opportunity creation, 10% evenly split across other touches). Documented in Data Dictionary.
- Segmentation: Report KPIs by ICP tier, region, industry, and new vs. customer.

---

## Measurement Plan and Data Foundations
- Campaign hierarchy:
  - Parent campaign: “FY25-EMEA+NA Flagship Summit”
  - Child campaigns: Registration, Onsite Attendance, Each Session, Meetings, Trials, Partner Activities.
- Tagging & UTMs:
  - Standard UTM schema; require campaign ID on all links and QR codes.
  - All scans, meetings, and sessions must map to child campaigns.
- Data capture:
  - Registration form with firmographic enrichment; GDPR/CCPA consent collection.
  - Onsite badge scanning with real-time sync to CRM (15-min window).
  - Session attendance tracked via scans or virtual platform logs.
  - Meeting scheduler integrated with CRM (auto-create contact/lead + meeting task).
- Baselines:
  - Prior year sourced pipeline: $2.8M; influenced revenue: $900k; NPS: 41; show rate: 62%.
- QA & governance:
  - Dry run at T-4 weeks to validate campaign IDs, UTMs, and dashboards.
  - Daily data QA during event; de-dupe rules; bot filtering on virtual sessions.
- Reporting:
  - Live dashboards (Tableau/Looker) for registrations, attendance, meetings, and pipeline.
  - Executive weekly scorecard with KPI RAG status and variance analysis.

---

## Process: Key Steps
1) Align on purpose and strategy (T-16 to T-14 weeks)
- Run a 90-minute Stakeholder Alignment Workshop.
- Confirm corporate OKRs and translate into event objectives.
- Draft and approve Event Purpose Statement.

2) Define targets and baselines (T-14 to T-12)
- Pull prior event data; set stretch but achievable targets (+15–25% YoY).
- Lock primary KPIs (max 5) and secondary KPIs (supporting).

3) Build the measurement architecture (T-12 to T-10)
- Create campaign hierarchy in CRM/MAP.
- Publish UTM schema and tracking guide.
- Configure attribution model and dashboards.

4) Sales and partner enablement (T-10 to T-6)
- Publish meeting booking playbook and talk tracks.
- Assign account lists; prospecting cadence begins.
- Define sponsor lead delivery and SLAs.

5) Content and experience design (T-10 to T-4)
- Agenda mapped to buyer pains and product proof.
- Hands-on labs to drive trial/POC KPIs.
- Survey instruments finalized (NPS, CSAT, session ratings).

6) Dry runs and data QA (T-4)
- End-to-end test: registration → scan → CRM → dashboard.
- Fix data gaps; re-test.

7) Event execution (Event week)
- Daily stand-up to review registrations, attendance, meetings, and hot leads.
- Real-time escalation path for tracking issues.

8) Post-event follow-up and pipeline creation (T+1 to T+4 weeks)
- Enforce 3-day SLA on lead follow-up; monitor compliance.
- Run targeted nurture and SDR cadences based on session interest and intent.
- First readout at T+7 days; update targets if external factors materially change.

9) Revenue influence tracking and close (T+4 to Q+2)
- Monthly attribution updates; validate with Sales + Finance.
- Final performance pack at Q+2 with learnings and next-event recommendations.

---

## Roles and Responsibilities
- Executive Sponsor: Approves purpose, budget, and targets; resolves escalations.
- Event Strategy Lead (Doc Owner): Orchestrates framework, workshops, timeline; owns KPI delivery.
- Marketing Ops: Builds campaign hierarchy, UTMs, forms, integrations; manages attribution and dashboards.
- RevOps/Sales Ops: Opportunity definitions, SLA rules, pipeline tracking; QA on CRM data.
- SDR Manager: Meeting goals, follow-up SLA adherence, cadence enablement.
- Sales Leaders/AEs: Target account engagement; meeting ownership; opportunity creation hygiene.
- Content Lead/Product Marketing: Agenda, value narratives, demos; session ratings.
- Customer Marketing/CS Ops: Customer invites, expansion plays, adoption metrics.
- Partner Marketing: Sponsor packages, lead delivery, sponsor satisfaction.
- Finance: Budget owner; ROMI calculation; revenue validation.
- CX Research: NPS, CSAT survey design and analysis.
- Data Analyst: Variance analysis, cohorting, and insight generation.

RACI Example (abbreviated):
- Define KPIs: A = Event Strategy Lead, R = MOPs/RevOps, C = Sales/Finance, I = Exec Sponsor
- Build Tracking: A/R = MOPs, C = RevOps, I = All
- Follow-up SLAs: A = SDR Manager, R = SDRs, C = Sales Leaders, I = Event Lead
- Final Readout: A = Event Lead, R = Data Analyst, C = Finance/Sales, I = Exec Sponsor

---

## Dependencies and Risks
Critical dependencies:
- Tools: Salesforce (CRM), Marketo/HubSpot (MAP), Cvent/ON24 (reg/virtual), Attribution (Bizible/Marketo Measure), Looker/Tableau (BI), Outreach/Salesloft (sales engagement), Gainsight (CS).
- Integrations: Real-time sync between reg platform and CRM; campaign/touchpoint ingestion for attribution.
- Data: Account/Contact enrichment, ICP tiering, dedupe, consent management.
- Content: Final agenda and assets at least T-21 days; speaker confirmations at T-30 days.
- Budget & Contracts: Sponsor agreements, venue/platform SOWs executed by T-45 days.

Top risks and mitigations:
- Tracking gaps: Run T-4 QA; publish a “No ID, no asset” rule for all links and badges.
- Poor follow-up: Enforce 3-day SLA; surface non-compliance daily; exec support for enforcement.
- Misaligned definitions: Publish a Data Dictionary; lock KPI definitions before launch.
- Attribution disputes: Agree on model upfront; include a “single-touch sanity check” alongside multi-touch.
- Data latency: Set expectations on when numbers stabilize (e.g., pipeline T+14, revenue Q+2).
- Privacy non-compliance: Legal-reviewed consent language; regional data residency checks.

---

## Reporting Cadence and Artifacts
- Daily (Event Week): Registrations, attendance, meetings, hot leads; SLA compliance.
- Weekly (T-4 to T+4): KPI scorecard with RAG status, variance vs. target, actions.
- Monthly (to Q+2): Influenced revenue updates; ROMI; win stories.
- Final Readout (Q+2): Comprehensive performance pack, learnings, and next-event recommendations.

Artifacts:
- Executive Scorecard (one-pager)
- Pipeline & Revenue Dashboard (Tableau/Looker)
- Follow-up SLA Tracker (CRM report)
- Sponsor Delivery Report

---

## Example Timeline (16 Weeks Pre → Q+2)
- T-16: Kick-off; Purpose workshop; draft KPIs
- T-14: Approve Purpose & KPI Matrix; budget lock
- T-12: Measurement plan; campaign hierarchy; UTM guide; dashboard specs
- T-10: Sales enablement; account lists assigned; sponsor packages finalized
- T-8: Registration live; content 60% locked; BI dashboard prototype
- T-6: Meeting scheduler integrated; partner co-marketing launches
- T-4: Full data QA dry run; survey instruments finalized
- T-2: Final content & speaker confirmations; run-of-show complete
- Event Week: Daily war room reporting
- T+1: SLA enforcement; hot lead blitz; preliminary report
- T+2: First pipeline readout; sponsor delivery summary
- T+4: Performance update; learnings and optimizations
- Monthly to Q+2: Revenue influence updates; final ROMI

---

## References and Templates
- Event Purpose Statement Template
  - Download: /templates/event-purpose-statement.docx
  - Fields: Business outcomes, Audience, Value prop, Strategic alignment, Timeframe, Primary KPIs, Guardrails, Go/No-Go
- KPI Matrix Template (CSV)
  - Columns: KPI, Definition, Target, Segment, Source, Owner, Cadence, Notes
  - Download: /templates/event-kpi-matrix.csv
- UTM & Campaign Hierarchy Guide
  - Download: /templates/utm-campaign-hierarchy.pdf
  - Includes naming conventions, required parameters, QR code standards
- Data Dictionary
  - Download: /templates/data-dictionary-event-metrics.xlsx
  - Defines MQL/SQL, sourced vs. influenced, attribution model, ICP tiers
- Survey Question Bank
  - Download: /templates/event-surveys.docx
  - Standard NPS, CSAT, session ratings, sponsor survey items
- Follow-up SLA Playbook
  - Download: /templates/follow-up-sla.pdf
  - Roles, timelines, cadences, talk tracks, objection handling
- Dashboard Spec
  - Download: /templates/dashboard-spec.md
  - KPIs, segments, filters, data sources, refresh cadence

---

## Quick Start Checklist
- Purpose approved and aligned to corporate OKRs
- KPI Matrix finalized; targets baselined and documented
- Tracking: Campaign hierarchy live; UTMs/QRs issued; integrations tested
- Sales enablement: Account lists, cadences, meeting goals published
- Surveys ready; privacy and consent reviewed
- Dashboards live; RACI communicated
- Post-event follow-up SLA enforced from Day 1

This framework enables any cross-functional team to plan, execute, and prove the business impact of events with clarity and rigor. Adjust targets, timelines, and tools to your organization’s maturity and market dynamics.