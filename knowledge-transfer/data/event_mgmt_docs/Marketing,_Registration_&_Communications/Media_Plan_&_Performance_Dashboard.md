# Media Plan & Performance Dashboard

Document Type: Plan document and dashboard specification  
Workstream: Marketing, Registration & Communications  
Purpose: Allocate media budget, placements, targets, and measurement framework with real-time tracking to drive registrations and revenue for the event.

---

## Overview

This document provides a complete media plan and a performance dashboard specification for an event marketing campaign. It is designed so a team member can plan, launch, and monitor paid media that drives event registrations with clear KPIs, data collection, and optimization rules.

Example event context:
- Event: Global Product Summit 2026
- Event dates: March 24–26, 2026 (San Francisco + Virtual)
- Registration platform: Swoogo
- CRM/Marketing automation: HubSpot, synced to Salesforce
- Analytics stack: GA4 + server-side GTM, BigQuery warehouse, Looker Studio dashboard

Primary goals:
- 7,500 total registrations (5,000 paid in-person; 2,500 free virtual)
- Registration revenue target: $2.8M
- Blended CPA target (paid media): $175
- ROAS target: 4.5x
- Secondary: 40% registrations from target geos (US, UK, DACH), 25% from net-new accounts

Campaign timeline (example):
- Early bird: Oct 1–Nov 30, 2025
- Standard: Dec 1, 2025–Feb 15, 2026
- Last chance: Feb 16–Mar 23, 2026
- Onsite: Mar 24–26, 2026

---

## Key Details or Steps

### Part A — Media Plan

1) Audience Strategy
- Primary segments:
  - Past attendees and CRM leads (retargeting and suppression for converters)
  - Lookalike audiences (1–3%) seeded on past converters (by region)
  - Job titles/roles: Product Managers, Heads of Product, UX/Design Leads, Growth, Engineering Managers, Data/Product Analytics
  - Company size: 200–10,000 employees; industries: Software, FinTech, HealthTech, Retail, Manufacturing
- Geo focus: US (70% budget), UK (15%), DACH (10%), Rest of World (5%)
- Exclusions: Current year registrants; competitors; students (unless student ticket promo period)

2) Channel Mix & Objectives
- Search (Google/Bing): Capture high-intent queries ("product conference", "innovation summit"); CPA ≤ $160
- Paid Social:
  - LinkedIn: Precise B2B targeting; CPA ≤ $220
  - Meta (Facebook/Instagram): Scale + retargeting; CPA ≤ $150
  - YouTube: Awareness + remarketing assist; CPV ≤ $0.05
- Programmatic Display/DOOH (DV360): Awareness + retargeting lift; view-through assist rate ≥ 12%
- Partnerships/Affiliates: Industry newsletters and associations; CPA ≤ $180
- Email Sponsorships: Direct response in relevant B2B lists; CPA ≤ $165

3) Budget & Flighting (example)

Total paid media budget: $250,000 (Oct 1, 2025–Mar 23, 2026)

- By phase:
  - Early Bird (Oct–Nov): $85,000 (34%)
  - Standard (Dec–Feb 15): $110,000 (44%)
  - Last Chance (Feb 16–Mar 23): $55,000 (22%)

- By channel (blended across phases):
  - Google Search: $62,500 (25%) — CPC target: $3.50; Conv. rate target: 2.5%
  - Bing Search: $12,500 (5%) — CPC: $2.80; Conv. rate: 2.3%
  - LinkedIn: $75,000 (30%) — CPC: $7.00; CTR: 0.65%; Conv. rate: 1.2%
  - Meta: $50,000 (20%) — CPC: $1.50; CTR: 1.1%; Conv. rate: 1.5%
  - YouTube: $12,500 (5%) — CPV: $0.04; View rate ≥ 25%; Assist rate monitored
  - DV360 Display/DOOH: $25,000 (10%) — CPM: $5.50; Viewability ≥ 60%
  - Partnerships/Affiliates: $12,500 (5%) — Fixed + CPA deals

- Pacing rules:
  - Spend ±10% vs. plan per phase unless forecast indicates risk to registration goal
  - Shift up to 15% of channel budget intra-phase to top-performing channels at weekly optimizations

4) Creative & Messaging
- Pillars:
  - Learning: "200+ sessions led by product leaders"
  - Impact: "Increase product velocity and customer value"
  - Community: "Network with 5,000+ peers"
  - Offer: "Save $300 during Early Bird"
- CTAs:
  - In-person: "Register Now" / "Save $300 Today"
  - Virtual: "Claim Free Virtual Pass"
- Formats/specs:
  - LinkedIn: Single image (1200x627), Video (1:1, 1080x1080), Document ads
  - Meta: Carousel (1080x1080), Reel (9:16), Static (1080x1350)
  - Display: 300x250, 300x600, 728x90, 160x600, 970x250; HTML5 and static
  - YouTube: 15s bumper, 30s skippable
- Creative testing:
  - A/B test headlines (benefit vs. urgency), imagery (speakers vs. crowd), offer framings
  - Minimum 5,000 impressions per creative before decision; promote winners with ≥15% better CTR or ≥10% better CPA

5) Landing Pages & Offers
- Primary LPs:
  - /register (full-flow)
  - /pricing (ticket tiers)
  - /virtual (free pass)
  - /why-attend (benefits, agenda highlights)
- Promotion cadence:
  - Early Bird: emphasize discount, social proof (past attendee logos)
  - Standard: emphasize agenda reveal, speaker announcements
  - Last Chance: scarcity (ticket thresholds, hotel cutoff)
- CRO best practices:
  - Above-the-fold CTA, trust badges, short form for first step, progress bar
  - Use exit-intent modals for 10% off newsletter opt-in (email nurture to convert)

6) Tracking & Measurement Framework
- Conversion events:
  - PageView, SessionStart
  - Reg_Start (click “Begin Registration”)
  - Reg_Complete (payment or free registration success)
  - Add_to_Calendar
  - Lead_Capture (newsletter or waitlist)
- Data capture and enrichment:
  - UTMs on all paid and owned links (see UTM schema below)
  - Client-side and server-side events via GTM (web) and GTM Server
  - Offline conversions: daily/near-real-time sync from Swoogo/HubSpot to ad platforms (GCLID/FBCLID/MSCLKID capture)
- Attribution:
  - Default: 7-day click / 1-day view platform attribution; report also in GA4 (data-driven) and last non-direct click for triangulation
  - MMM lite: monthly spend vs. outcomes regression with holdouts (where feasible)
- Holdout/control:
  - 10% geo or audience holdout for Display/YouTube to estimate incremental lift during Early Bird phase
- Brand safety and fraud:
  - DV360 pre-bid brand safety filters; exclude MFA (Made For Advertising) domains; enable ads.txt checks

7) UTM Schema (example)
- utm_source: google | linkedin | meta | dv360 | newsletterX | partnerY
- utm_medium: cpc | cpm | email | affiliate | social | video
- utm_campaign: gps26_earlybird | gps26_standard | gps26_lastchance
- utm_content: creativeA_headline1 | video15s_speakers | carousel_offer
- utm_term: for search keywords (e.g., product+conference)
Example URL:
https://www.gpsummit.com/register?utm_source=linkedin&utm_medium=social&utm_campaign=gps26_earlybird&utm_content=docad_benefit&utm_term=

8) Optimization Cadence & Decision Rules
- Daily:
  - Pause creatives with CTR < 0.3% (LinkedIn) / < 0.6% (Meta) after 5,000 impressions
  - Increase bids/budgets on ad sets with CPA ≤ 85% of target and ≥ 10 conversions in last 7 days
  - Shift spend to geo-ad sets with CVR ≥ 120% of account average
- Weekly:
  - Reallocate up to 15% budget across channels based on blended CPA and assisted conversions
  - Refresh creatives: rotate in 2 new variants per channel; retire bottom quartile
  - CRO changes: test 1 LP variant per week with minimum 95% significance or 1,000 sessions
- Phase gates:
  - If phase forecast < 90% of registration target at midpoint, deploy contingency:
    - Increase search budgets +20%
    - Add mid-funnel webinar partnership
    - Launch limited-time bundle (2-for-1) for teams, capped at 200 redemptions

9) Example KPIs by Phase
- Early Bird:
  - Registrations: 3,000 (CPA target $150)
  - Revenue: $1.2M
  - CTR targets: LinkedIn 0.65%, Meta 1.1%, Display 0.25%
- Standard:
  - Registrations: 3,000 (CPA $180)
  - Revenue: $1.1M
- Last Chance:
  - Registrations: 1,500 (CPA $200)
  - Revenue: $0.5M

10) Risk & Mitigation
- Risk: Rising CPCs in Jan–Feb; Mitigation: build strong retargeting pools earlier; secure partner inventory in Q4
- Risk: Tracking loss from browser privacy; Mitigation: server-side tagging, consent mode, modeled conversions
- Risk: Creative fatigue; Mitigation: pre-build 30+ assets per channel; weekly rotation
- Risk: Registration friction; Mitigation: monitor funnel drop-off; simplify form fields; add SSO options

---

### Part B — Performance Dashboard Specification

1) Objectives
- Provide real-time visibility into spend, traffic, funnel performance, registrations, revenue, and ROI by channel, audience, creative, and geo.
- Support day-to-day optimization and executive reporting.

2) Users & Views
- Executive: Overview metrics, pacing vs. plan, forecast to goal
- Media Managers: Channel, creative, audience drill-downs; optimization alerts
- Registration Ops: Funnel breakdown by ticket type, discount code usage, cart abandonment
- Finance: Budget vs. actuals; CAC/ROAS by phase

3) Data Sources
- Ad Platforms: Google Ads, Microsoft Ads, LinkedIn, Meta, DV360, YouTube
- Web Analytics: GA4 (via BigQuery export)
- Registration Platform: Swoogo (registrations, revenue, ticket types, discount codes)
- CRM/MA: HubSpot + Salesforce (lead quality, company, pipeline influence)
- DOOH/Partners: Uploaded CSVs (impressions, spend, tracking parameters)
- Warehouse: BigQuery as single source of truth

4) Data Model (core tables/fields)
- dim_date (date_key, date, week, phase)
- dim_channel (channel_id, channel_name, platform, is_paid)
- dim_campaign (campaign_id, campaign_name, phase, geo, audience, utm_campaign)
- dim_creative (creative_id, format, message_pillar, size, creative_name)
- fact_spend (date_key, channel_id, campaign_id, spend, impressions, clicks, video_views)
- fact_web (date_key, campaign_id, sessions, bounces, events)
- fact_conversions (date_key, campaign_id, reg_start, reg_complete, add_to_calendar, ticket_type, revenue, gclid, fbclid, msclkid)
- fact_crm (date_key, campaign_id, mqls, sqls, opps, pipeline_value)
- mappings for UTMs to campaign/channel, and offline ID joins (gclid, fbclid, msclkid)

5) Data Processing & Refresh
- Ingestion:
  - Automated connectors (Supermetrics/Fivetran/Stitch) hourly for ad platforms
  - GA4 BigQuery export streaming; web events processed via SQL
  - Swoogo → HubSpot → BigQuery sync every 15 minutes (API/Webhook)
  - Salesforce pipeline sync hourly
- Transformation:
  - Standardize currency to USD; deduplicate by transaction_id
  - Join offline conversions to clicks via CLIDs within 7-day window
  - Apply consent mode/modeling flags (is_modeled)
- Refresh cadence:
  - Dashboard near-real-time (within 1–2 hours); daily snapshot at 02:00 local time for archival

6) Dashboard Structure (Looker Studio or equivalent)

- Global filters: Date range, Phase, Geo, Channel, Audience, Ticket Type, Device, New vs. returning
- Page 1: Executive Summary
  - KPIs: Spend, Registrations, Revenue, Blended CPA, ROAS, Forecast to Goal
  - Pacing vs. Plan: gauge + sparkline
  - Phase performance tiles
- Page 2: Funnel Performance
  - Sessions → Reg_Start → Reg_Complete by channel and by LP
  - Drop-off heatmap; CVR by step
- Page 3: Channel & Campaign
  - Table: Spend, Impr, Clicks, CPC, CTR, CVR, CPA, ROAS by channel/campaign
  - Trend lines with annotations (creative swaps, offer changes)
- Page 4: Creative Insights
  - Performance by creative_id (CTR, CPA, ROAS, frequency)
  - Fatigue indicator: performance vs. impressions over time
- Page 5: Audience & Geo
  - Map view (registrations, CPA by region)
  - Audience segments: lookalikes, job title clusters, retargeting windows
- Page 6: Pacing & Forecast
  - Daily spend vs. plan, burn rate; registration forecast with confidence intervals
  - Optimization recommendations sourced from rules engine
- Page 7: Registration Quality & Revenue
  - Ticket type mix, average order value, discount code usage
  - CRM quality: MQL/SQL rate, pipeline influenced (if applicable)
- Page 8: Experiments
  - A/B test registry with variants, hypothesis, status, lift, significance
- Page 9: Technical Health
  - Pixel firing rates, event integrity, ID capture rates (GCLID/FBCLID)
  - Data freshness indicators; connector status

7) Core Metrics & Definitions
- CPA: Spend / Reg_Complete
- ROAS: Revenue / Spend
- CVR: Reg_Complete / Clicks (channel) or / Sessions (site)
- Assisted Conversions: From GA4 multi-channel funnels; includes YouTube/Display assist rate
- Frequency (Paid Social): Impressions / Reach
- Incremental Lift: (Test group conversions − Control) / Control

8) Alerts & Automation
- Slack/Email alerts (via Cloud Functions/Apps Script):
  - CPA > $200 for 6+ hours and 10+ conversions: notify channel owner
  - Spend pacing variance > ±15% vs. plan for 2 consecutive days
  - Pixel error rate > 5% or missing consent tags
  - Zero conversions recorded for a channel in last 12 hours
- Automated budget reallocation suggestions:
  - Identify top quartile campaigns by CPA and CVR; propose +10% daily cap increase (requires human approval)

9) Privacy & Compliance
- Consent management (CMP) implemented; GA4 + Ads Consent Mode V2
- Server-side tagging with IP anonymization; data retention policy (26 months)
- Honor DNT and regional data residency for EU audiences
- Update privacy notice to reflect tracking and marketing partners

10) Example Visual Targets on Dashboard
- KPI targets as reference bands: CPA $175, ROAS 4.5x
- CTR target lines: LinkedIn 0.65%, Meta 1.1%, Display 0.25%
- Viewability target line: 60% for Display

---

## Responsibilities

- Marketing Lead (Owner)
  - Approves strategy, budget, messaging; chairs weekly performance review
- Performance Media Manager
  - Builds campaigns, manages bids, pacing, optimizations, and channel reallocations
- Creative Lead
  - Delivers asset roadmap; oversees A/B testing and refresh cadence
- Web/CRO Lead
  - Owns landing pages, form UX, and experimentation
- Analytics Engineer
  - Implements tracking, data pipelines, QA, and dashboard builds
- Registration Operations
  - Manages Swoogo setup, ticketing, discount codes, and payment flows
- Partnerships Manager
  - Coordinates newsletter/affiliate buys and tracking
- Finance Partner
  - Tracks spend vs. plan; validates invoices and accruals
- Legal/Privacy
  - Approves CMP, data handling, and partner contracts for compliance

Meeting cadence:
- Daily 15-min standup (Mon–Thu): blockers, alerts, hot fixes
- Weekly optimization (60 min): performance review, reallocations, creative next steps
- Phase kickoff/retro (90 min): goals, learnings, changes for next phase

---

## Dependencies

- Creative assets ready 10 business days before phase start (all required sizes/formats)
- Landing pages finalized and load-tested 7 days before launch
- Tracking in place (GTM web + server, GA4, Swoogo webhooks) 10 days before launch; QA 5 days before
- Data connectors authenticated and scheduled (ad platforms, HubSpot, Salesforce, Swoogo) 7 days before
- Budget approvals and IOs signed for partners 2 weeks before insertion dates
- UTM naming conventions documented and enforced via link builder
- CRM fields mapping finalized (ticket type, company size, job title, source fields)

---

## References or Templates

1) Media Plan Template (example)

Channel | Objective | Targeting | Budget | KPI Targets | Creative Formats | Notes
---|---|---|---:|---|---|---
Google Search | Capture intent | Exact/phrase match “product conference”, “product management summit” | $62,500 | CPA ≤ $160, CVR ≥ 2.5% | RSA, Sitelinks | Negatives: jobs, free, internship
LinkedIn | B2B precision | Titles: PM/Head of Product; 200–10k employees | $75,000 | CPA ≤ $220, CTR ≥ 0.65% | Single image, Video, Document | Test document ads: agenda preview
Meta | Scale + retargeting | Lookalikes (1–3%), site retargeting 7/30d | $50,000 | CPA ≤ $150, CTR ≥ 1.1% | Carousel, Reel, Static | Frequency cap 2/day
DV360 | Awareness/retarget | Contextual + PMP + remarketing | $25,000 | Viewability ≥ 60%, Assist rate ≥ 12% | Display, DOOH | Exclude MFA sites
YouTube | Awareness | In-market tech/professional; retargeting | $12,500 | CPV ≤ $0.05, View rate ≥ 25% | 15s bumper, 30s skippable | Use speaker teasers
Bing | Incremental intent | Same as Google | $12,500 | CPA ≤ $170 | RSA | Lower CPCs likely
Partners | Direct response | Industry newsletters/associations | $12,500 | CPA ≤ $180 | Native/email | Fixed + CPA hybrid

2) UTM & Naming Conventions
- Campaign name: gps26_{phase}_{channel}_{geo}_{audience}
  - Example: gps26_earlybird_linkedin_us_titles_pm
- Asset name: {pillar}_{format}_{size}_{version}
  - Example: impact_carousel_1080x1080_v3

3) Pixel & QA Checklist
- GA4 events: page_view, session_start, Reg_Start, Reg_Complete (with ticket_type, revenue)
- Ad pixels: Google Ads, Meta, LinkedIn with consent gating
- Server-side GTM:
  - CLID capture for gclid/fbclid/msclkid
  - IP anonymization
- Test cases:
  - Complete paid registration with test card → verify in GA4, Swoogo, HubSpot, Ads platforms
  - Consent states: accept/deny → verify event behavior
  - UTM propagation from ad click through to transaction

4) Sample SQL Snippets (BigQuery)
- Join offline conversions to campaigns:
  SELECT
    c.date_key,
    m.campaign_id,
    COUNTIF(c.event='Reg_Complete') AS registrations,
    SUM(c.revenue) AS revenue
  FROM fact_conversions c
  JOIN dim_campaign m
    ON c.utm_campaign = m.utm_campaign
  WHERE c.date_key BETWEEN '2025-10-01' AND '2026-03-23'
  GROUP BY 1,2;

- Compute CPA and ROAS:
  SELECT
    d.date,
    ch.channel_name,
    SUM(s.spend) AS spend,
    SUM(conv.registrations) AS registrations,
    SAFE_DIVIDE(SUM(s.spend), NULLIF(SUM(conv.registrations),0)) AS cpa,
    SAFE_DIVIDE(SUM(conv.revenue), NULLIF(SUM(s.spend),0)) AS roas
  FROM fact_spend s
  JOIN dim_date d ON d.date_key = s.date_key
  JOIN dim_channel ch ON ch.channel_id = s.channel_id
  JOIN (
    SELECT date_key, campaign_id,
           COUNTIF(event='Reg_Complete') AS registrations,
           SUM(CASE WHEN event='Reg_Complete' THEN revenue ELSE 0 END) AS revenue
    FROM fact_conversions
    GROUP BY 1,2
  ) conv ON conv.date_key = s.date_key AND conv.campaign_id = s.campaign_id
  GROUP BY 1,2
  ORDER BY d.date;

5) Example Weekly Performance Review Agenda
- Topline: spend, registrations, revenue vs. plan
- Forecast to goal and gaps by phase
- Channel deep-dive: CPA/ROAS, assists, creative fatigue
- Audience and geo insights
- CRO results and next tests
- Decisions: budget reallocations, creative refreshes, new offers
- Risks/blockers and owners

---

## How to Get Started (Step-by-Step)

1. Confirm goals, budget, phases, and ticketing structure with stakeholders.
2. Finalize UTM schema and naming conventions; set up link builder for the team.
3. Build or update landing pages; implement CRO best practices; run performance tests.
4. Implement tracking: GTM web + server, GA4, ad pixels, Swoogo webhooks; complete QA.
5. Connect data sources to warehouse; build dashboard according to spec; validate metrics.
6. Produce initial creative set per channel; load to ad platforms with test campaigns.
7. Launch Early Bird with conservative bids; monitor first 72 hours closely; fix any data issues.
8. Run daily optimizations and weekly reviews; document learnings; adjust budgets/creatives.
9. At phase transitions, publish a brief recap and updated plan; adjust forecasts.
10. Post-event, deliver final report: performance vs. goals, incrementality, learnings, and recommendations for next cycle.

---

This document serves as the single source of truth for planning and operating paid media and the performance dashboard to drive event registrations and revenue.