# Email Nurture Calendar & Copy Bank
Marketing, Registration & Communications

Document Title: Email Nurture Calendar & Copy Bank  
Document Description: Schedules send cadence by segment and provides approved subject lines, CTAs, and body copy. Format: calendar spreadsheet and copy repository.

---

## Overview
This document provides a turnkey email nurture plan and copy repository for promoting and managing registrations for a flagship event. It includes:

- A segment-based send calendar from pre-launch to post-event, with timing, frequency caps, and exclusion rules.
- A copy bank of approved subject lines, preheaders, CTAs, and body copy mapped to lifecycle stages and audience segments.
- Operational guidance (naming conventions, UTM/parameters, QA checklist).
- Roles, dependencies, and references to templates.

Assumptions for the example timeline:
- Event: Future of Ops Summit (FOS) 2025
- Dates: November 12–14, 2025 (Wed–Fri)
- Primary audience: North America (EN-US); secondary: EMEA/APAC
- Early-bird deadline: September 15, 2025
- Standard registration closes: November 10, 2025

You can adapt names/dates for other events; the structure remains consistent.

---

## How to Use This Document
1. Confirm event dates, deadlines, prices, and segments with the Event PM and Marketing Ops.
2. Clone the calendar and copy bank into your event folder; update placeholders (e.g., [EVENT_NAME], [DATE], [PRICE]).
3. Map segments to your CRM/ESP lists and suppression logic.
4. Build email assets using the naming conventions herein.
5. Route for content and legal approvals per the responsibilities section.
6. Schedule sends according to the calendar and frequency caps.
7. Monitor performance and optimize using A/B tests and the measurement plan.

---

## Segments and Definitions
- Prospects – Cold: Contacts in target ICP who have never clicked or registered for any event in the past 12 months.
- Prospects – Warm: Leads with email clicks/website visits in the last 90 days but no registration.
- Inquiries: Contacts who filled an “Interested” form or downloaded the agenda but did not start registration.
- Partial Registrants: Started registration but abandoned (no payment/completion).
- Registered – General: Paid or confirmed free passes; not VIP.
- Registered – VIP/Invite: Executive pass holders or invited accounts.
- Speakers: Confirmed speakers.
- Sponsors/Exhibitors: Confirmed sponsors/exhibitors.
- Waitlist: Registered interest for sold-out sessions or capacity-limited features.
- Attendees – Attended: Checked in to at least one session.
- Attendees – No-Show: Registered but did not attend.
- Lapsed Past Attendees: Attended a prior year’s event but not yet engaged for this year.
- Unsubscribed/Suppressed: Excluded per policy; do not contact.

Segment criteria must be configured in CRM/ESP audience queries and validated by Marketing Ops before campaign launch.

---

## Send Cadence and Frequency Caps
- Default quiet hours: 8 pm–7 am recipient local time. Do not exceed 1 email/day per contact across all campaigns.
- Frequency caps per segment (weekly):
  - Prospects (Cold/Warm): Max 2/week (non-consecutive days).
  - Inquiries & Partial Registrants: Max 3/week during critical windows (cart recovery/deadlines), otherwise 2/week.
  - Registered (General/VIP): Max 2/week; increase to 3/week during “Know Before You Go” week.
  - Speakers, Sponsors: Max 2/week operational; 1/week during steady state.
  - Post-event: Max 2/week for 3 weeks, then 1/week.
- Priority: Transactional/operational > Deadline/price increase > Content value (agenda/speakers) > General awareness.
- Resend policy: No “non-opener” resends due to Apple MPP. Allow “non-clicker” follow-up 48–72 hours later with changed subject line and stronger CTA (limit 1 resend per message).

---

## Calendar: Example Schedule (Key Milestones and Send Themes)
Event: Future of Ops Summit 2025 (Nov 12–14)

T-16 to T-13 weeks (Jul 21–Aug 17)
- Theme: Save the Date + Super Early Awareness
- Prospects (Warm/Cold):
  - Email E01: Save the Date announcement; CTA: Get Event Updates.
- Lapsed Past Attendees:
  - E02: “We’re back” with highlights; CTA: Hold Your Spot.
- Speakers/Sponsors (internal):
  - E03: Confirmation + next steps (operational).

T-12 to T-9 weeks (Aug 18–Sep 14)
- Theme: Early-Bird Opens, Agenda Preview
- Prospects (Warm), Inquiries:
  - E04: Early-bird open with 20% off ends Sep 15; CTA: Register Early.
  - E05: Agenda first look; CTA: Explore Tracks.
- Partial Registrants:
  - E06: Cart recovery with incentive reminder; CTA: Complete Registration.
- Lapsed Past Attendees:
  - E07: Loyalty note + discount code; CTA: Come Back.
- VIP/Invite:
  - E08: Invite-only passes; CTA: Claim VIP Pass.

T-8 to T-5 weeks (Sep 15–Oct 12)
- Theme: Price Increase, Speaker Headliners
- Prospects (Cold/Warm), Inquiries:
  - E09: Last day for Early-Bird (Sep 15); CTA: Register Now.
  - E10: Headliner announcement; CTA: See Speakers.
- Registered:
  - E11: Hotel/travel info; CTA: Book Your Room.
- Sponsors:
  - E12: Exhibitor portal setup; CTA: Access Portal.

T-4 to T-2 weeks (Oct 13–Nov 3)
- Theme: Urgency, Agenda Builder, Teams
- Prospects, Inquiries:
  - E13: 3 weeks to go + session highlights; CTA: Secure Your Seat.
- Partial Registrants:
  - E14: Cart recovery with expiring incentive; CTA: Finish Registration.
- Registered (General/VIP):
  - E15: Agenda builder + app download; CTA: Build Your Schedule.
  - E16: Know-before-you-go Part 1 (logistics); CTA: View Details.
- Speakers/Sponsors:
  - E17: Deliverables and deadlines reminder.

Event Week (Nov 4–10 pre, Nov 12–14 live)
- Registered:
  - E18: Know-before-you-go Part 2 (badges/check-in); CTA: Check-In Details.
- All (geo-targeted within 50 miles, if applicable):
  - E19: Final call for on-site registration; CTA: Walk-in Info.
- During event:
  - E20–E22: Daily highlights and next-day preview (operational).

Post-Event (Nov 17–Dec 8)
- Attendees – Attended:
  - P01: Thank you + survey; CTA: Share Feedback.
  - P02: On-demand library; CTA: Watch Sessions.
- Attendees – No-Show:
  - P03: Sorry we missed you + on-demand; CTA: Get Access.
- Prospects/Lapsed:
  - P04: Best-of content sampler; CTA: Watch Highlights.
- Sponsors:
  - P05: Lead retrieval and wrap-up; CTA: Download Leads.

Notes:
- Use send windows Tue–Thu 9:00–11:30 am local; test alternatives per segment.
- Buffer content deadlines: copy/final assets due 5 business days before send.

---

## Copy Bank (Approved, Ready-to-Use)
Tokens: Use merge fields per ESP syntax. Examples:
- [FIRST_NAME], [COMPANY], [JOB_TITLE], [EVENT_NAME], [EVENT_DATES], [EVENT_CITY], [EARLY_BIRD_PRICE], [STANDARD_PRICE], [DISCOUNT_CODE], [HOTEL_CUTOFF_DATE], [AGENDA_URL], [REGISTER_URL]

UTM standard: utm_source=email&utm_medium=nurture&utm_campaign=fos2025_[segment]_[emailID]  
Example link: https://fosummit.com/register?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_E04

E01 – Save the Date (Prospects – Cold/Warm)
- Subject: Save the date: Future of Ops Summit returns Nov 12–14
- Preheader: 3 days. 1000+ peers. Ideas you’ll use Monday.
- Body:
  Hi [FIRST_NAME],  
  The Future of Ops Summit is back in [EVENT_CITY] on [EVENT_DATES]. Join 1000+ leaders for hands-on sessions on AI in operations, change management, and resilient processes.  
  Be first to know when registration opens and snag early pricing.
- Primary CTA: Get Event Updates
- CTA URL: https://fosummit.com/updates?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_E01

E02 – We’re Back + Highlights (Lapsed Past Attendees)
- Subject: You made last year great—here’s what’s new for 2025
- Preheader: New tracks, live labs, and bigger peer exchanges.
- Body:
  Welcome back, [FIRST_NAME]!  
  Because you joined us before, you’re first to see 2025 upgrades:  
  - 4 tracks including AI-in-the-Flow  
  - Live process labs and certification prep  
  - More executive roundtables  
  Lock in early access before prices rise.
- CTA: Hold Your Spot
- URL: https://fosummit.com/register?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_lapsed_E02

E04 – Early-Bird Opens (Prospects – Warm/Inquiries)
- Subject: Early-bird is open: Save 20% through Sep 15
- Preheader: Your best price for Future of Ops Summit 2025.
- Body:
  It’s official—registration is open. Early-bird pricing saves you 20% through Sep 15.  
  Expect 40+ sessions, headliners from [COMPANY], and practical frameworks you can take back to your team.  
  Bring a colleague and amplify the impact.
- CTA: Register Early
- URL: https://fosummit.com/register?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_warm_E04

E05 – Agenda First Look (Prospects/Inquiries)
- Subject: First look: 40+ sessions to future-proof ops
- Preheader: Agenda preview inside—build your must-see list.
- Body:
  The agenda is live. Explore new tracks like AI-in-the-Flow, Scaling Change, and Customer-Centric Ops.  
  See the sessions trending with leaders like you and plan your path to measurable wins.
- CTA: Explore Tracks
- URL: [AGENDA_URL]?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_inquiry_E05

E06 – Cart Recovery (Partial Registrants)
- Subject: You’re nearly there—complete your FOS 2025 registration
- Preheader: Finish in 2 minutes. Your early-bird savings await.
- Body:
  Hi [FIRST_NAME], you started registering for [EVENT_NAME] but didn’t finish.  
  Complete your registration now to secure your seat and early-bird savings before they’re gone.
- CTA: Complete Registration
- URL: https://fosummit.com/checkout?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_partial_E06
- Variant: Include dynamic block with saved ticket type and price.

E07 – Loyalty Offer (Lapsed Past Attendees)
- Subject: Welcome back offer: extra 10% off ends Sep 15
- Preheader: Because you’ve joined us before.
- Body:
  As a thank-you for being part of our community, use code [DISCOUNT_CODE] for an extra 10% off early-bird.  
  See what’s new and reconnect with peers.
- CTA: Use Your Code
- URL: https://fosummit.com/register?code=[DISCOUNT_CODE]&utm_source=email&utm_medium=nurture&utm_campaign=fos2025_lapsed_E07

E09 – Last Day Early-Bird (All Prospects/Inquiries)
- Subject: Last day to save 20% on FOS 2025
- Preheader: Prices increase at midnight your local time.
- Body:
  Final hours to lock in early-bird pricing for [EVENT_NAME].  
  Join 1000+ ops leaders for tools, templates, and real-world case studies.  
  If you register today and plans change, transfers are free.
- CTA: Register Now
- URL: https://fosummit.com/register?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_E09

E10 – Headliner Announcement (Prospects/Inquiries)
- Subject: Just announced: Keynotes from [SPEAKER_NAME] and [SPEAKER_2]
- Preheader: Fresh ideas from leaders at [BRAND_A] and [BRAND_B].
- Body:
  We’re thrilled to welcome [SPEAKER_NAME], [TITLE] at [BRAND_A], and [SPEAKER_2] from [BRAND_B].  
  Get their playbooks for building resilient, AI-powered operations.
- CTA: See Speakers
- URL: https://fosummit.com/speakers?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_E10

E11 – Hotel & Travel (Registered)
- Subject: Book your room by [HOTEL_CUTOFF_DATE] and save
- Preheader: Preferred rates and walking-distance hotels.
- Body:
  You’re in! Next step: secure your hotel at our discounted rate by [HOTEL_CUTOFF_DATE].  
  Get maps, transport tips, and visa letters if needed.
- CTA: Book Your Room
- URL: https://fosummit.com/travel?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_registered_E11

E13 – 3 Weeks to Go (Prospects/Inquiries)
- Subject: 3 weeks out—this is your sign to secure your seat
- Preheader: Sessions are filling; join peers tackling the same challenges.
- Body:
  With three weeks to go, top sessions are nearing capacity.  
  If operational excellence is on your roadmap, [EVENT_NAME] is where to accelerate.
- CTA: Secure Your Seat
- URL: https://fosummit.com/register?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_E13

E15 – Agenda Builder + App (Registered)
- Subject: Build your FOS schedule in minutes
- Preheader: Download the app and reserve sessions.
- Body:
  Make the most of your time. Download the app to reserve sessions, message peers, and get live updates.  
  Popular sessions may waitlist—add them now.
- CTA: Build Your Schedule
- URL: https://fosummit.com/app?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_registered_E15

E16 – Know Before You Go Part 1 (Registered)
- Subject: Know before you go: badges, check-in, and logistics
- Preheader: Everything you need for a smooth first day.
- Body:
  Here’s what to expect: registration hours, badge pick-up, Wi-Fi, meals, and accessibility services.  
  Questions? Reply to this email—we’re here to help.
- CTA: View Details
- URL: https://fosummit.com/kbyg?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_registered_E16

E18 – Know Before You Go Part 2 (Registered)
- Subject: Tomorrow’s the day—final details inside
- Preheader: Weather, entrance map, and opening keynote time.
- Body:
  See you tomorrow. Quick reminders: entrance at Hall B, doors open 8 am, keynote at 9 am.  
  Badge QR is in the app for faster entry.
- CTA: Check-In Details
- URL: https://fosummit.com/checkin?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_registered_E18

P01 – Thank You + Survey (Attended)
- Subject: Thank you for joining us—tell us how we did?
- Preheader: 2-minute survey. Your feedback shapes 2026.
- Body:
  Thank you, [FIRST_NAME], for being part of FOS 2025.  
  Share what worked and what we can improve in a 2-minute survey.
- CTA: Share Feedback
- URL: https://fosummit.com/survey?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_attended_P01

P02 – On-Demand Library (Attended)
- Subject: Your on-demand access is ready
- Preheader: Watch sessions you missed, share with your team.
- Body:
  Replay keynotes and breakouts on your schedule.  
  Slides and templates are available under each session.
- CTA: Watch Sessions
- URL: https://fosummit.com/on-demand?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_attended_P02

P03 – On-Demand for No-Shows (No-Show)
- Subject: Sorry we missed you—here’s your access
- Preheader: Top sessions, available now on-demand.
- Body:
  We’re sorry you couldn’t make it. Catch up with the most-watched sessions and speakers.
- CTA: Get Access
- URL: https://fosummit.com/on-demand?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_noshow_P03

P04 – Best-of Sampler (Prospects/Lapsed)
- Subject: Most-watched sessions from FOS 2025
- Preheader: Start with these 5 talks everyone’s sharing.
- Body:
  Curious what you missed? Sample the five most-watched sessions—no pass required.
- CTA: Watch Highlights
- URL: https://fosummit.com/highlights?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_prospect_P04

P05 – Sponsor Wrap-Up (Sponsors)
- Subject: Your leads and post-event toolkit
- Preheader: Export leads, booth metrics, and follow-up tips.
- Body:
  Your leads are ready in the Exhibitor Portal, including scans, engagement, and notes.  
  Use our follow-up templates to convert interest into meetings.
- CTA: Download Leads
- URL: https://fosummit.com/exhibitors?utm_source=email&utm_medium=nurture&utm_campaign=fos2025_sponsor_P05

Note: All emails must include a branded footer, physical mailing address, and a visible unsubscribe or preference link.

---

## Operational Steps and Standards
Build process per email:
1. Intake
   - Confirm segment, goal, send date, KPI, and content owner.
   - Create or update brief (see Templates).
2. Asset creation
   - Copy from this bank; adjust tokens; route to design for images if needed.
   - Build in ESP using approved template (dark mode friendly, responsive).
3. Naming convention
   - Campaign: FOS2025_[Segment]_[EmailID]_v[Version] (e.g., FOS2025_PROSPECT_E04_v1)
   - Email asset: Same as campaign; include locale if applicable (e.g., _ENUS).
   - Audience list: SEG_[SegmentName]_FOS2025_YYYYMMDD
4. Links and tracking
   - Append UTM; test all links; use link aliases in ESP if available.
5. Personalization and dynamic content
   - Default fallbacks: [FIRST_NAME] -> “there”
   - Dynamic blocks by segment or ticket type as defined in brief.
6. QA checklist (must pass before schedule)
   - Spelling, grammar, brand voice.
   - Tokens resolve with fallbacks.
   - Links/UTMs working; plain-text version updated.
   - Mobile/responsive test (e.g., Litmus/Email on Acid).
   - Inbox rendering seed test for top clients (Gmail, Outlook, Apple Mail).
   - Accessibility: 16px+ body text, sufficient color contrast, ALT text.
   - Compliance: unsubscribe link, postal address, consent flags.
   - Suppression lists and frequency caps applied.
   - Volume sanity check vs. segment size.
7. Approvals
   - Content: Content Lead
   - Design: Brand/Design Lead
   - Legal (if promotional offer or regulated claims)
   - Final: Marketing Ops
8. Schedule and monitor
   - Stagger sends by timezone where possible.
   - Warm-up IP/domain as needed.
   - Monitor 0–24 hours for deliverability anomalies.

A/B testing guidelines:
- Test 1 variable at a time; minimum 10k audience or wait for 95% confidence (or 4-hour decision window).
- Common tests: subject line (benefit vs. urgency), CTA label (Register Now vs. Save My Seat), hero image vs. no image, long vs. short copy.
- Winner metric: click-through rate for top-of-funnel; conversion rate for cart recovery.

Preference center and opt-down:
- Offer options: FOS-only updates, All events, Newsletters, Unsubscribe all.
- Place above full unsubscribe where allowed.

---

## Responsibilities
- Event PM: Owns milestones, pricing, and deadlines; final authority on timeline changes.
- Content Lead: Owns copy adaptation and accuracy; manages copy bank updates.
- Brand/Design Lead: Ensures brand compliance; supplies assets.
- Marketing Operations (MOPS): Audience segmentation, ESP build, QA, send, deliverability, and reporting.
- Data/CRM Owner: Ensures data accuracy, consent flags, and integrations (registration platform, app).
- Legal/Compliance: Reviews promotional offers, terms, and regional compliance (CAN-SPAM, GDPR, CASL).
- Web/Digital: Landing pages, registration flow, tracking, and on-demand library pages.
- Analytics: Dashboard creation, performance analysis, and insights.
- Sponsor/Partner Manager: Communications to sponsors/exhibitors, fulfillment of deliverables.

Approval SLAs:
- Copy draft: 5 business days before send.
- Design assets: 4 business days before send.
- Final approvals: 2 business days before send.

---

## Dependencies
- ESP/CRM integration with registration platform (writeback of status: Registered, Attended, No-Show).
- Verified sender domain, SPF/DKIM/DMARC alignment; warmed sending IP/domain.
- Preference center and suppression lists functioning; consent captured by region.
- Agenda page, speakers page, registration, travel, app, and on-demand pages live and stable.
- Discount codes configured and tested; hotel block and cutoff dates confirmed.
- Mobile app store links available (iOS/Android).
- Translations and localized send times (if applicable).

Risk mitigations:
- If web pages are delayed, swap CTAs to “Get Updates” or “Download Agenda PDF.”
- If deliverability dips (bounce/spam rate threshold breached), pause prospect sends; send only transactional/registered ops while remediating.

---

## Measurement and Reporting
Primary KPIs by stage:
- Awareness (E01–E05): Delivered rate, open rate (directional), CTR, landing page engagement.
- Conversion (E04, E06, E09, E13): CTR, registration conversion rate, revenue per send.
- Operational (E11, E15–E18): Click-to-task completion (e.g., hotel bookings, app installs).
- Post-event (P01–P05): Survey completion rate, on-demand activation rate, sponsor lead retrieval rate.

Benchmarks (adjust per historical data):
- CTR: 2.5–4.5% (prospects), 4–8% (registered ops).
- Registration CVR from click: 6–12% (warm), 12–25% (cart recovery).
- Survey completion: 20–35% within 7 days.

Reporting cadence:
- Day 1 post-send: Deliverability/CTR spot check.
- Weekly: Segment performance rollup; test results.
- Post-event, 30 days: Full funnel analysis and recommendations for next cycle.

---

## Governance and Compliance
- Always include physical mailing address and unsubscribe link.
- Honor local laws: CAN-SPAM (US), GDPR (EU), CASL (CA). Only email contacts with valid consent and lawful basis.
- Maintain audit trail of approvals (brief, copy, assets, send logs).
- Store all campaign assets and versions in the designated folder with version control.

---

## References or Templates
File storage (example paths; update to your environment):
- Calendar Spreadsheet: /Marketing/Events/FOS2025/Email/Email_Nurture_Calendar_FOS2025.xlsx
  - Tabs: Overview, Milestones, Segment Sends, Asset Inventory, Test Log
- Copy Repository: /Marketing/Events/FOS2025/Email/Copy_Bank_FOS2025.docx
  - Sections mirror the copy bank above; include locale variants.
- ESP Template: FOS_Nurture_Master_ENUS (responsive, dark-mode safe)
- Email Brief Template: /Marketing/Templates/EmailBrief_v3.docx
  - Fields: Objective, Segment, Offer, Key Points, Tokens, Dynamic Content, KPIs, Approvals
- QA Checklist: /Marketing/Templates/Email_QA_Checklist.pdf
- UTM Guide: /Marketing/Analytics/UTM_Conventions.pdf
- Preference Center Requirements: /Marketing/CRM/PreferenceCenter_Specs.md

---

## Example “Segment Sends” Entry Format (for Spreadsheet)
For each row in the calendar spreadsheet, include:
- Send Date (local), Time Window
- Segment
- Email ID (e.g., E09)
- Objective (e.g., Price increase conversion)
- Subject Line
- Primary CTA
- Landing URL (with UTM)
- Audience Size (est.)
- Owner (Content/MOPS)
- Status (Draft/In Review/Approved/Scheduled/Sent)
- Notes (A/B test, exclusions, dependencies)

---

## Exclusions and Safeguards
- Suppress anyone registered from receiving prospect conversion emails within 24 hours of registering.
- Exclude VIPs from generic discount emails; they get tailored invitations.
- Geo-filter “walk-in” emails to local radius only.
- Respect frequency caps across all concurrent campaigns; MOPS enforces via global frequency setting.

---

## Change Management
- If event dates, pricing, or offers change, the Event PM must issue a change log within 24 hours. MOPS pauses impacted sends until assets are updated and reapproved.
- Version control: Increment v# on any content change post-approval; document what changed in the brief.

---

This document, combined with the calendar spreadsheet and copy repository, enables any team member to plan, build, and execute the event email program with consistency, compliance, and measurable outcomes. Adapt the examples to your event while keeping the structure and operational rigor.