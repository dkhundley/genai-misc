# Post-Event Impact Measurement Plan
Document type: Measurement plan, dashboard specification, and survey linkage map  
Topic: Event Strategy & Stakeholder Alignment

## Overview
This plan defines how we measure, attribute, and report the business impact of events. It specifies the metrics we track, the data sources and flows, attribution rules, reporting cadence, dashboard specifications, and how attendee surveys link back to registrations and CRM records. It is designed so that a cross-functional team (Event, Marketing Ops, Sales, Data/BI) can implement and operate the measurement end-to-end.

Scope:
- Applicable to all events: flagship conferences, field events, trade shows, webinars.
- Covers net-new acquisition and existing-account influence.
- Aligns with our campaign hierarchy and go-to-market segmentation (ICP tiers, regions, industries).

Example event referenced throughout:
- Name: Q4 Product Summit (Q4PS)
- Date/Location: Oct 14, 2025, San Francisco
- Audience: 500–700 practitioners and decision-makers (B2B SaaS)
- Objective: Pipeline acceleration for enterprise tier and new logo acquisition for mid-market

---

## Objectives and Key Questions
Primary objectives:
- Quantify pipeline and revenue attributable to the event.
- Measure account coverage, buying committee penetration, and engagement quality.
- Assess satisfaction, intent, and message resonance via surveys.
- Calculate efficiency and ROI to guide future investment and planning.

Key questions:
1. What net-new pipeline and revenue did the event source? What did it influence?
2. Which accounts advanced stages or expanded their buying committee engagement?
3. How did channels, sessions, and content perform?
4. Did we meet SLAs for follow-up? How did follow-up correlate with conversion?
5. What is the ROI and payback period?
6. What did attendees think (NPS/CSAT, intent to buy, content relevance)?
7. What lift did we see versus similar accounts that did not attend?

---

## Metrics and Definitions (with example targets)
Funnel and Revenue:
- Registrations: Count of unique registrants. Target: 800 for Q4PS.
- Attendees: Count of unique check-ins. Target attendance rate ≥70% (e.g., 560).
- Net-new Leads: Unique leads not previously in CRM. Target: ≥200.
- MQLs: Leads meeting score/fit criteria within 30 days post-event. Target: 150.
- SQLs/SALs: Sales-accepted/qualified leads within 45 days. Target: 50 SALs.
- Opportunities Created: New opps with event attribution within 60 days. Target: 30 opps.
- Pipeline Value: Sum of opp amounts created within window. Target: $3.0M.
- Closed-Won Revenue: Within 180 days. Target: $1.0M.
- Payback Period: Days to breakeven from attributable revenue. Target: ≤180 days.
- ROI: (Revenue attributable − Event Cost) / Event Cost. Target: ≥100%.

Influence and Coverage:
- Influenced Pipeline/Revenue: Opps where at least one buying group member engaged with event (within lookback). Report value and count.
- Account Penetration: % target accounts with ≥2 roles engaged. Target: ≥35% of Tier 1 accounts.
- Buying Committee Coverage: # roles engaged per account vs. target persona map.

Engagement and Operations:
- Session Attendance: Avg sessions per attendee; top sessions by unique attendees.
- Dwell Time: Average time in venue/booth; average session duration per attendee.
- Booth Scans/Meetings: Count and rate per attendee.
- Speed-to-First-Touch: Median hours from event to SDR outreach. Target: ≤24h.
- Sequence Completion: % attendees enrolled and completed follow-up sequence.

Efficiency:
- Cost per Registration/Attendee/MQL/Opp/$Pipeline/$Revenue.
- Channel Efficiency: Performance by source (email, paid social, partners, organic).

Satisfaction and Intent:
- NPS (event-level). Target: ≥40.
- CSAT (content, venue, logistics). Target: ≥4.2/5.
- Brand Lift & Intent: Aided awareness, purchase intent delta vs. baseline or control.

Quality:
- ICP Fit Rate: % attendees in ICP tiers (T1/T2).
- Seniority Mix: % decision-makers vs. practitioners.

Example Q4PS outcomes (illustrative):
- Registrations: 800; Attendees: 560 (70%)
- Net-new Leads: 220; MQLs: 150; Opps: 32; Pipeline: $3.2M
- Closed-Won (180d): $1.1M; Event Cost: $450k; ROI: 144%; NPS: +41
- Speed-to-First-Touch: 18 hours median

---

## Attribution Approach
Primary models:
1. Sourced (Primary Attribution)
   - Default for new-logo acquisition: W-shaped multi-touch.
   - Credit allocation: 30% First Touch (FT), 30% Lead Creation Touch (LC), 40% Opportunity Creation Touch (OC).
   - Event receives credit if it is FT, LC, or OC within the model windows:
     - FT window: 90 days before lead creation.
     - LC window: Day of lead creation (event registration or scan considered LC if it creates the lead).
     - OC window: 30 days before opportunity creation.
   - If event is not FT/LC/OC but is within 14 days pre/post LC, allocate residual touch credit pro-rata with time decay (half-life 7 days).

2. Influence (Secondary Attribution)
   - For existing accounts or in-flight opportunities: Event is credited as “influencing” if any contact on the buying team engaged within 30 days prior to stage advancement or opp creation.
   - Influence impact is reported separately as influenced pipeline/revenue and stage velocity changes.

3. Incremental Lift (Control-Based)
   - Construct a matched control group of non-attending accounts by ICP tier, region, firmographic size, and historical engagement.
   - Calculate lift in opp creation rate and pipeline value within 60/90/180 days.

Attribution rules and edge cases:
- Deduplication: Use email + eventID; secondary match on CRM contactId; flag walk-ins.
- Offline scans: Matchback by email; if absent, match by company + name (fuzzy) with confidence threshold ≥0.85; unmatchable scans are stored as prospects pending enrichment.
- Multiple events: Most recent engagement within attribution window applies for influence; sourced credit follows the W-shaped rules per opportunity.
- Partners: If partner-sourced registrant, split credit 50/50 for sourced; 100% influence to both if engaged.

Attribution windows:
- Immediate: 0–7 days for engagement and Ops SLAs.
- Sourced pipeline: 0–60 days post-event.
- Revenue: 0–180 days post-event.
- Influence: 30-day lookback prior to opp creation or stage change.

---

## Data Sources and Flow
Systems:
- Event Platform: Cvent (registrations, attendance, sessions, scans)
- CRM: Salesforce (Leads, Contacts, Accounts, Opportunities, Campaigns)
- MAP: Marketo (emails, UTMs, programs, scoring)
- Web Analytics: GA4 (UTM tracking)
- Ad Platforms: LinkedIn, Google Ads (campaign cost and click data)
- Data Warehouse: Snowflake (single source for BI)
- Survey Tool: Qualtrics (NPS, CSAT, intent)
- Enrichment: Clearbit/ZoomInfo (firmographics)
- BI/Visualization: Looker or Power BI

Data flow (daily or near-real-time where available):
1. Event Platform -> Marketo (program membership, custom fields) -> Salesforce Campaign (via native sync)
2. Event Platform -> Snowflake (raw exports via API)
3. Salesforce + Marketo + GA4 + Ad Platforms -> Snowflake (ELT pipelines)
4. Qualtrics -> Snowflake (survey responses with identifiers)
5. Snowflake -> BI dashboards (Looker/Power BI models)

Join keys:
- RegistrationId (event platform), mapped to SFDC Campaign Member Id where possible
- Email (lowercased; hashed copy for privacy-safe joins)
- SFDC Lead/Contact Id
- AccountId (for account-level rollups)
- OpportunityId (for pipeline/revenue)
- Survey ResponseId linked via ?cid, ?rid, ?eid URL parameters

Data freshness:
- Ops readout: T+1 day with preliminary QA
- Executive dashboards: Daily scheduled refresh 02:00 local time
- Final 30/60/90-day readouts: On respective days with data freeze

---

## Key Steps (End-to-End)
1. Pre-Event Setup (T-8 to T-1 weeks)
   - Define objectives, KPIs, and targets; confirm attribution windows.
   - Create CRM Campaign hierarchy:
     - Parent: FY25 Events
     - Child: 2025 Q4 Product Summit (Q4PS)
     - Tactics (children): Email Invites, Paid Social, Partners, Organic, Onsite, Follow-up
   - Configure Marketo Program with channel = Event; sync to Salesforce Campaign.
   - Set UTM schema (see template) and test in GA4/Marketo.
   - Create BI dataset stubs and calculated fields in Snowflake.
   - Build SDR follow-up sequences; set SLAs (first touch ≤24h).
   - Add survey links with identifiers (?cid, ?rid, ?eid) and QR codes for onsite.

2. During Event
   - Capture check-ins, session attendance, dwell time, and booth scans.
   - Log onsite meetings in Salesforce via event codes (e.g., E-Q4PS-MTG).
   - Monitor data sync health; fix duplicates and failed syncs same-day.

3. Post-Event (T+1 to T+14 days)
   - Run enrichment on new leads; dedupe and convert where needed.
   - Launch post-event survey at T+24h; reminder at T+7d.
   - Auto-enroll attendees in follow-up sequences; monitor speed-to-first-touch.
   - QA checks (attendance validation, UTM integrity, campaign member statuses).
   - First readout at T+7d with preliminary engagement and pipeline indicators.

4. Extended Measurement (T+30/60/90/180 days)
   - Attribute sourced and influenced pipeline and revenue.
   - Update lift analysis with control cohort.
   - Produce 30/60/90-day readouts and 180-day revenue wrap-up.

5. Closeout and Learnings
   - Document what worked/what didn’t (content, channels, ops).
   - Feed insights into next event plan; update benchmarks.

---

## Dashboard Specification
Audience and access:
- Executives: Summary KPIs, ROI, pipeline/revenue
- Marketing & Event Teams: Channel effectiveness, engagement, content
- Sales & SDR Leadership: Follow-up SLAs, meeting outcomes, account coverage
- Ops & Analytics: Data quality, attribution integrity

Global filters:
- Event Name (multi-select)
- Date Range (event date + windows)
- Region/Segment/Industry
- ICP Tier (T1/T2/T3)
- New vs Existing Account
- Role/Seniority
- Channel/Source/UTM Campaign
- Opportunity Stage

Pages and core visuals:
1. Executive Summary
   - KPIs: Registrations, Attendees, MQLs, Opps, Pipeline, Revenue, ROI
   - Trendlines: Daily registrations and attendance
   - Funnel chart: Reg -> Attendee -> MQL -> SAL -> Opp -> CW
   - Payback countdown: days to breakeven

2. Funnel & Pipeline
   - Conversion rates between stages with benchmarks
   - Cohort table: New vs Existing accounts
   - Opp table: Sourced vs Influenced, amounts, owners, stage aging

3. Account Coverage & Acceleration
   - Heatmap: Roles engaged per target account
   - Stage velocity: Median days between stages for attendees vs control
   - Account lists: Tier 1 with gaps (missing C-Level/Finance, etc.)

4. Engagement & Content
   - Sessions ranked by unique attendees and satisfaction scores
   - Dwell time distributions; booth scan counts per hour
   - Channel performance (cost, CTR, conversion to registration)

5. Survey Insights
   - NPS and CSAT with comments word cloud
   - Intent-to-purchase lift vs baseline
   - Satisfaction by persona/industry/session

6. Incrementality & Lift
   - Matched control vs attendee: Opp creation rate, pipeline per account
   - Statistical significance indicators (where applicable)

7. Ops QA & Attribution
   - Data health: duplicate rate, missing fields, sync lag
   - Attribution breakdown: % FT/LC/OC credit, time-decay distribution

Calculated fields (examples):
- Attendance Rate = attendees / registrations
- MQL Rate = MQLs / attendees
- Cost per Opp = total_event_cost / opps_created
- ROI = (attributable_revenue − total_event_cost) / total_event_cost
- Influence Flag = 1 if contact engaged within 30 days before opp creation
- Speed-to-First-Touch (hours) = first_outreach_ts − event_end_ts

Alerts:
- SLA breach: >25% attendees without first SDR touch by T+24h
- Data sync failure: No new campaign members in 6 hours
- Negative NPS trend: drop >10 points vs benchmark

Update cadence:
- Daily refresh at 02:00; Ops QA panel refresh hourly during T+3 days.

---

## Survey Linkage Map
Purpose:
- Link attendee survey responses to registrations and CRM records to analyze satisfaction, intent, and content feedback by persona, account, and outcome.

Identifiers and URL parameters:
- cid = SFDC Contact Id (or Lead Id if no Contact yet)
- rid = Event Platform Registration Id
- eid = Internal Event Id (e.g., Q4PS2025)
- src = channel (e.g., post_email, onsite_qr)

Example survey link:
https://survey.company.com/q4ps?nps=1&cid={{Contact.Id}}&rid={{Registration.Id}}&eid=Q4PS2025&src=post_email

Onsite QR flow:
- Display a unique QR per attendee badge that encodes a one-time token mapped to rid and cid.
- For anonymous scans, prompt email entry with explicit consent; store hashed email.

Survey cadence:
- Send T+24h; reminder T+7d; optional T+30d for longitudinal intent.

Core questions (5–7 minutes total):
- NPS (0–10): “How likely are you to recommend this event?”
- CSAT (1–5): “Overall satisfaction with event logistics and content.”
- Content Relevance (1–5) per attended session
- Intent to Purchase (Likert): “My likelihood to evaluate/expand increased.”
- Open-ended: “What was most valuable?” “What could be improved?”
- Persona metadata (auto-enrich from CRM where possible): role, seniority, industry

Data mapping:
- Survey Response -> Survey Table (Qualtrics) with fields: response_id, cid, rid, eid, timestamps, scores, text, consent_flag
- Join Survey Table to:
  - CRM Contacts on cid
  - Event Registrations on rid
  - Accounts via Contacts.AccountId
  - Sessions via session_id if embedded in question piping

Privacy and consent:
- Show privacy notice and purpose of data use; capture explicit consent checkbox.
- Store hashed email for anonymous responses; honor opt-outs in MAP.
- Retention: 24 months for raw responses; anonymize open-text after 12 months for non-customers.

Reporting:
- Survey results appear on Survey Insights dashboard filtered by eid.
- NPS calculation excludes staff and partners by default (flag via registration type).

---

## Reporting Cadence and Deliverables
- T+24 Hours: Ops Brief (1–2 pages)
  - Attendance, preliminary MQLs, SLA adherence, data health, top sessions
- T+7 Days: Early Impact Readout (10–12 slides)
  - Channel performance, engagement, early pipeline, survey toplines
- T+30 Days: Impact Update
  - Sourced/influenced pipeline, conversion rates, content insights, account coverage
- T+60 Days: Pipeline Deep Dive
  - Opp quality, stage velocity, SDR sequence effectiveness, lift vs control
- T+90 Days: Executive Review
  - ROI forecast, recommendations, budget implications
- T+180 Days: Revenue Wrap-Up
  - Closed-won, final ROI, playbook updates, benchmarks

---

## Responsibilities
RACI summary by function:
- Event Marketing (Accountable)
  - Define objectives/KPIs, content plan, session taxonomy, onsite data capture processes
  - Own T+24/T+7/T+30 readouts and executive alignment
- Marketing Operations (Responsible)
  - Campaign hierarchy, Marketo programs, UTM governance, dedupe/enrichment
  - Ensure MAP-CRM sync, lead scoring, and attribution rules configured
- Sales Operations (Responsible)
  - Follow-up sequences, SLA tracking, meeting logging codes, opportunity hygiene
- Data/Analytics (Responsible)
  - Build data pipelines to Snowflake, model joins, implement attribution logic
  - Develop/maintain dashboards, QA checks, and lift analysis
- SDR/BDR Managers (Consulted)
  - Enforce SLAs, coach teams, provide feedback on lead quality
- Finance (Consulted)
  - Validate cost inputs and ROI methodology
- Privacy/Legal (Consulted)
  - Consent language, data retention, DPA compliance
- Executive Sponsor (Informed)
  - Receives milestone readouts; approves strategic recommendations

Named roles (example for Q4PS):
- Event Lead: A. Kim
- MOPs Lead: J. Patel
- Sales Ops Lead: R. Nguyen
- Analytics Lead: T. Howard
- SDR Manager: L. Morales
- BI Developer: S. Reed
- Privacy Officer: D. Santos

---

## Dependencies
- System integrations active: Cvent–Marketo–Salesforce; ELT to Snowflake
- Campaign hierarchy established in Salesforce; program statuses configured
- UTM taxonomy enforced in all media and email links
- Lead scoring and MQL definition locked 4 weeks pre-event
- SDR sequences approved; SLA = first touch ≤24 hours
- Data dictionary for fields (see References) published company-wide
- Cookie consent and email opt-in flows compliant in target regions
- Partner data (if applicable) available in agreed format

---

## Data Quality and QA Checklist
- Registration-CRM sync success rate ≥98%
- Duplicate rate ≤2% after enrichment/dedupe
- Mandatory fields completeness: email, company, job title, country ≥95%
- Campaign member statuses: Invited, Registered, Attended, No Show consistent
- UTM presence on ≥95% of registration conversions
- Attribution sanity: % credit distribution sums to 100% per opportunity
- Survey response rate target: ≥20% of attendees; NPS respondent mix reflects persona distribution

---

## Cost and ROI Inputs
- Event Cost components:
  - Venue/Production, Sponsorships, Creative, Travel, Paid Media, Tech stack, Staff time (optional burden rate)
- Include media costs tied to UTM campaigns driving registrations
- Exclude sunk costs unrelated to event influence
- Finance sign-off at T+30 and T+180

---

## References and Templates
1. UTM Schema
   - utm_source: email | linkedin | google | partner | organic
   - utm_medium: cpc | cpm | social | email | referral
   - utm_campaign: fy25_q4ps_invite_mm | fy25_q4ps_ret_targeting
   - utm_content: variantA_headline1 | speakername
   - utm_term: keyword (for search)

2. Salesforce Campaign Hierarchy (example)
   - FY25 Events (Parent)
     - 2025 Q4 Product Summit (Child)
       - Q4PS | Email Invites
       - Q4PS | Paid Social
       - Q4PS | Partners
       - Q4PS | Onsite
       - Q4PS | Follow-up

3. Field Dictionary (selected)
   - sfdc.campaign_member.status: Invited, Registered, Attended, No Show
   - event.registration_id (string)
   - contact.id / lead.id (string)
   - opportunity.primary_campaign_id (string)
   - survey.response_id (string)
   - engagement.session_id, dwell_minutes (numeric)

4. Example SQL Snippets (pseudo)
   - Attendance Rate:
     select event_id, count(distinct case when status='Attended' then registration_id end)::float / count(distinct registration_id) as attendance_rate
   - Sourced Pipeline (60d):
     select sum(o.amount) from opportunity o
     join attribution a on a.opportunity_id = o.id
     where a.touchpoint_type='event' and a.event_id='Q4PS2025' and a.role in ('FT','LC','OC') and o.created_date <= event_end + interval '60 days'
   - Influenced Pipeline:
     select sum(o.amount) from opportunity o
     join contact_activity ca on ca.contact_id = o.contact_id and ca.event_id='Q4PS2025' and ca.activity_date between o.created_date - interval '30 days' and o.created_date

5. Survey Question Bank (abbreviated)
   - NPS, CSAT, Content Relevance, Intent to Purchase, Open-ended

6. Ops Readout Template (slides)
   - Slide 1: KPIs summary
   - Slide 2: Funnel
   - Slide 3: Channel performance
   - Slide 4: Top sessions
   - Slide 5: SLA compliance
   - Slide 6: Risks/Actions

---

## Example Timeline (Q4PS)
- T-8 weeks: Finalize KPIs, hierarchy, UTMs; build dashboards; confirm SLAs
- T-6 weeks: Launch registrations; test data flows
- T-1 week: Dry run; lock scoring; publish runbook
- Event day: Monitor capture; hourly QA
- T+1 day: Ops Brief; survey launch
- T+7 days: Early Impact Readout
- T+30/60/90/180 days: Scheduled readouts and closeout

---

## Risks and Mitigations
- Broken UTMs or redirects: Use automated link validator pre-send; GA4 real-time checks
- Delayed sync: Implement retry and lag alerts; manual CSV fallback for critical readouts
- Low survey response: Incentivize with raffles; shorten survey; embed in Thank You emails
- Attribution disputes: Publish definitions; provide both sourced and influenced views; maintain audit trail

---

## How to Get Started (Action Steps This Week)
- Event Lead: Confirm objectives, KPIs, and targets with stakeholders; share this plan.
- MOPs: Create Salesforce Campaign hierarchy; build Marketo Program and statuses.
- Analytics: Provision Snowflake tables and BI model; implement attribution logic.
- Sales Ops: Publish SDR sequence; confirm SLA monitoring and dashboards.
- Survey Owner: Configure Qualtrics with cid/rid/eid parameters and privacy text.
- All: Schedule T+7, T+30, T+60, T+90, T+180 readouts on stakeholder calendars.

With this plan, any team member can set up, execute, and report on event impact consistently, enabling strategic alignment and continuous improvement across the event portfolio.