# Mobile App Content Map & Push Strategy
Attendee Experience & Onsite Services

Document version: 1.0  
Prepared by: Event Experience & Communications  
Last updated: 2025-08-23

## Overview
This document catalogs the event mobile app’s content architecture and ownership and defines the push notification strategy tied to key onsite moments. It is designed so any team member can understand what content lives where, who maintains it, how often it updates, and when/how we message attendees.

Assumptions for planning examples:
- Event: Connect 2025 Conference
- Dates: Tue–Thu, Sep 16–18, 2025
- Location: Moscone Center, San Francisco, CA (Local time: PDT, UTC-7)
- Attendance: ~6,000
- App Platform: iOS/Android + responsive web app
- Content CMS: AppCMS v3.2; Schedule feed from Sessionize; Registration feed from RegSys; Maps from MappedIn

Sections:
- Content Sitemap (modules, owners, update cadence, deep links)
- Governance & operations (workflows, SLAs)
- Push notification strategy (targeting, frequency, approvals)
- Messaging calendar (pre-event through onsite/post)
- Responsibilities, Dependencies, KPIs, References/Templates

---

## Content Sitemap (Modules, Ownership, Update Cadence)
Notes on fields:
- Owner = accountable content steward
- Data source = system of record (SOR)
- Update cadence = when content must be reviewed/refreshed
- SLA = publication time after change request
- Deep link = app URI pattern for routing

1) Agenda & Sessions
- Description: Full schedule with tracks, filters, session details, capacity, and add-to-personal tools.
- Owner: Program Manager (PM), App Admin publishes.
- Data source: Sessionize API (hourly sync), manual overrides in AppCMS.
- Update cadence: Daily pre-event (T-14 to T-1); Hourly onsite.
- SLA: Critical change (room/time): 10 min; Speaker update: 4 hours.
- Deep link: app://agenda; app://session/{sessionId}; app://track/{trackId}

2) Speakers
- Description: Profiles with bios, headshots, sessions, social links.
- Owner: Speaker Ops.
- Data source: Sessionize; photo assets DAM.
- Update cadence: Twice weekly pre-event; daily onsite for swaps.
- SLA: 24 hours; onsite swaps 2 hours.
- Deep link: app://speaker/{speakerId}

3) My Schedule & Favorites
- Description: Personalized list of saved sessions and RSVPs.
- Owner: App Admin; Program for RSVP rules.
- Data source: AppCMS user profile; Sessionize RSVP flags.
- Update cadence: Real-time as users interact.
- SLA: N/A
- Deep link: app://my/schedule

4) Venue Maps & Wayfinding
- Description: Interactive building maps, halls, session rooms, expo floor, key services.
- Owner: Venue Ops.
- Data source: MappedIn; custom POIs from Ops.
- Update cadence: Weekly pre-event; same-day for closures.
- SLA: Critical (safety/closure): 10 min; Non-critical: same business day.
- Deep link: app://map; app://poi/{poiId}

5) Transportation & Shuttles
- Description: Airport transfer info, shuttle routes, ride-share zones, public transit, parking.
- Owner: Transportation Lead.
- Data source: Shuttle vendor feed; static content from Ops.
- Update cadence: Twice weekly pre-event; 30 min interval onsite during shuttle service windows.
- SLA: Routing delays/alerts: 10 min; Schedule updates: 1 hour.
- Deep link: app://transport; app://shuttle/{routeId}

6) Check-in & Badging
- Description: Badge pickup hours, locations, ID requirements, QR code.
- Owner: Registration Lead.
- Data source: RegSys API for QR; static content for hours.
- Update cadence: Weekly pre-event; real-time QR.
- SLA: 4 hours non-critical; 30 min line management notices.
- Deep link: app://badge; app://qr

7) Expo & Exhibitors
- Description: Exhibitor listings, categories, booth locations, sponsor activations.
- Owner: Expo Manager.
- Data source: Exhibitor portal export; floorplan from Venue Ops.
- Update cadence: Weekly pre-event; daily onsite for last-minute changes.
- SLA: 24 hours pre; 2 hours onsite.
- Deep link: app://expo; app://exhibitor/{exhibitorId}; app://booth/{boothId}

8) Live Q&A & Polling
- Description: Session-specific engagement tools.
- Owner: Program Manager; Tech Producer per room.
- Data source: Slido/Glisser integration.
- Update cadence: As sessions start/end.
- SLA: Enable/disable per session: 5 min.
- Deep link: app://session/{sessionId}/qa

9) Alerts & Updates (In-App Inbox)
- Description: Persistent message center for non-urgent updates.
- Owner: Comms Lead, App Admin publishes.
- Data source: Manual.
- Update cadence: As needed.
- SLA: 1 hour standard; 10 min urgent.
- Deep link: app://inbox/{messageId}

10) Food & Beverage
- Description: Meal times/locations, dietary options, water stations.
- Owner: Catering Ops.
- Data source: Ops docs.
- Update cadence: Weekly pre-event; daily onsite.
- SLA: 4 hours; 30 min if location shifts.
- Deep link: app://dining; app://poi/{poiId}

11) Accessibility & Inclusion Services
- Description: ADA access routes, ASL/Captioning schedule, nursing room, prayer/quiet rooms.
- Owner: Accessibility Lead.
- Data source: Ops; vendor schedules.
- Update cadence: Weekly pre-event; daily onsite.
- SLA: Critical relocation: 15 min; general: same day.
- Deep link: app://accessibility

12) Health, Safety & Security
- Description: Code of conduct, emergency procedures, first aid, security contacts.
- Owner: Safety & Security Lead; Legal for COC.
- Data source: Ops; Legal.
- Update cadence: At milestones (T-30, T-14, T-7); immediate for incidents.
- SLA: Critical incident: 5–10 min; updates 30 min.
- Deep link: app://safety; app://coc

13) Help Desk & Lost/Found
- Description: Help chat/phone, onsite desks, ticketing form, lost item log.
- Owner: Attendee Services Lead.
- Data source: Zendesk integration; Ops list.
- Update cadence: Daily pre; hourly onsite.
- SLA: New desk location: 15 min; contact corrections: 1 hour.
- Deep link: app://help; app://lostfound

14) Surveys (Daily & Session)
- Description: CES/CSAT daily pulse, post-session surveys.
- Owner: Insights/Research.
- Data source: Qualtrics; Sessionize mapping.
- Update cadence: Per session end; daily at 4:30 PM.
- SLA: Preloaded; updates 2 hours.
- Deep link: app://survey/{surveyId}

15) Networking & Messaging
- Description: Opt-in attendee list, matchmaking, 1:1 messages, meeting slots.
- Owner: Community Manager.
- Data source: App platform; RegSys segments.
- Update cadence: Ongoing; daily moderation.
- SLA: Abuse report escalation: 15 min.
- Deep link: app://networking; app://attendee/{attendeeId}

16) Social & Media
- Description: Social feed, official hashtag, photo gallery, livestream links.
- Owner: Social Lead.
- Data source: Curated UGC; media DAM.
- Update cadence: Daily pre; hourly onsite.
- SLA: 1 hour.
- Deep link: app://social; app://media

17) Wi‑Fi & Tech Support
- Description: SSID/password, troubleshooting, device tips.
- Owner: IT Lead.
- Data source: Venue IT.
- Update cadence: At go-live; as needed onsite.
- SLA: 30 min.
- Deep link: app://wifi

18) Sustainability
- Description: Waste sorting map, refill stations, green tips, carbon offset info.
- Owner: Sustainability Lead.
- Data source: Ops.
- Update cadence: T-14, T-7, onsite daily.
- SLA: 4 hours.
- Deep link: app://sustainability

19) Legal & Policies
- Description: Terms, privacy, photo/recording policy.
- Owner: Legal.
- Data source: Legal docs.
- Update cadence: T-30 and final T-7; urgent as required.
- SLA: 24 hours.
- Deep link: app://legal

20) Sponsor Promotions
- Description: Banner placements, sponsored content tiles, lead scans.
- Owner: Sponsorships.
- Data source: Sponsor portal assets.
- Update cadence: T-14, T-7; daily onsite for rotations.
- SLA: 24 hours pre; 2 hours onsite.
- Deep link: app://sponsor/{sponsorId}

Menu IA (top-level navigation):
- Home (dynamic tiles), Agenda, Speakers, Maps, Expo, Networking, Messages, Help, Safety, More (Dining, Transport, Accessibility, Surveys, Wi‑Fi, Sustainability, Legal)

---

## Governance & Operations

Content workflow
- Intake: Requester submits Content Change Form (see template) via Slack #app-content or ticketing queue.
- Review: Owner validates accuracy; Legal/Brand review if policy or sponsor-related.
- Publish: App Admin applies changes in AppCMS, tests on staging, then publishes to prod.
- Verification: QA confirms change in live app and logs in Change Log.

Change SLAs (time to publish after approval)
- Critical safety/evacuation: 5–10 min (push + app update)
- Major agenda/location changes: 30 min
- Operational notices (shuttle, F&B): 30–60 min
- Content hygiene (typos, bios): 4–24 hours

Blackout windows
- Daily 08:45–09:30, 12:00–12:30, 16:45–17:30: limit non-critical publish to avoid user disruption.
- Exempt: critical safety and room/location changes.

Naming conventions
- Sessions: [Track] Title (Level) | Room | Day HH:MM
- POIs: Building – Level – Room – Name (e.g., Moscone West – L2 – 2009 – Quiet Room)
- Messages: D{1-3}-[Module]-ShortTitle (e.g., D1-Transport-AM Shuttles)

Testing/UAT checklist
- Deep link routes correctly from push and from Home tiles.
- Map POI opens correct floor/zoom.
- Session survey auto-launches 5 min before end.
- Accessibility labels on icons/images.
- Offline cache: maps and agenda available without network.

Accessibility standards
- Color contrast AA minimum; text resizable.
- Alt text for images; transcripts for videos.
- Wayfinding includes accessible routes and elevators.

Data hygiene & privacy
- Do not include PII in push messages.
- Honor user notification preferences and opt-outs.
- Archive messages older than 30 days.

---

## Push Notification Strategy

Goals
- Reduce friction in onsite navigation and services.
- Drive attendance to key program moments.
- Prompt feedback collection with high response rates.
- Provide timely safety/operational advisories without spam.

Principles
- Utility first; no more than 3 non-critical pushes per attendee per day.
- Segment whenever possible for relevance.
- Respect quiet hours: 9:00 PM–7:00 AM PDT (exceptions: safety).
- Always include a deep link and clear CTA.
- Pair push with in-app inbox post for persistence when appropriate.

Segmentation
- Role: Attendee, Speaker, Exhibitor, VIP, Staff.
- Location: Onsite geofence vs. offsite (airport/hotels).
- Registration flags: First-time attendee, Session RSVPs, Accessibility requests.
- Interests/Tracks: Based on saved items.
- Venue zone/room: For capacity/line management (if BLE/beacons enabled).

Frequency caps
- All-attendee informational: Max 1 morning + 1 midday + 1 late-day.
- Segment-specific: Max 2 additional.
- Critical alerts: Not capped.

Approval workflow
- Draft: Comms Lead
- Review: Module Owner + Legal (if policy/safety)
- Approve/Publish: Comms Lead or Duty Manager (onsite)
- Emergency: Safety Lead can publish immediately using predefined templates.

Message metadata (required fields)
- Title (max 48 chars), Body (max 140 chars), CTA label, Deep link, Segment, Priority (Critical/High/Standard), Schedule time (local), TTL (time-to-live), Owner, Approver.

Quiet hours & scheduling
- Default send windows: 07:30–18:30 PDT.
- Schedule critical ops around natural transitions (arrivals, meals, session blocks).
- Use local time; app converts based on device timezone for pre-event messages.

Throttling
- Minimum 15 min between all-attendee pushes.
- Batch seat-availability nudges to RSVP’d segments at T-30/T-10 minutes.

---

## Messaging Calendar (Example)

Pre-event timeline
- T-14 days (Tue, Sep 2, 10:00)
  - Segment: All registrants
  - Title: Build your plan
  - Body: Create your schedule to get smart recommendations onsite.
  - CTA: Open Agenda
  - Deep link: app://agenda
  - Owner: Program; Approver: Comms

- T-7 days (Tue, Sep 9, 09:30)
  - Segment: All registrants
  - Title: Know before you go
  - Body: Badging, Wi‑Fi, and maps—check arrival details.
  - CTA: Get Details
  - Link: app://arrival (Home tile linking to Check-in, Transport, Maps)
  - Owner: Ops; Approver: Comms

- T-2 days (Sun, Sep 14, 15:00)
  - Segment: Speakers
  - Title: Speaker check-in
  - Body: Review A/V and room arrival times for your session(s).
  - CTA: View Speaker Kit
  - Link: app://speakerkit
  - Owner: Speaker Ops

- T-1 day (Mon, Sep 15, 17:00)
  - Segment: All registrants within city geofence
  - Title: Badge pickup now open
  - Body: Avoid morning lines—pick up tonight until 20:00 at Moscone West.
  - CTA: View Map
  - Link: app://poi/badge-desk-west
  - Owner: Registration

Onsite Day 0 (Early arrivals, Mon)
- 07:30: Exhibitors
  - Title: Move-in reminder
  - Body: Dock access and safety briefing at 08:00. PPE required.
  - CTA: View Move-In
  - Link: app://expo/movein

Onsite Day 1 (Tue, Sep 16)
- 07:30: All attendees
  - Title: Welcome! Start here
  - Body: Breakfast 07:30–09:00 L1 Galleria. Keynote at 09:00 Hall F.
  - CTA: Open Today
  - Link: app://home/today

- 08:20: Not checked-in yet (Reg status)
  - Title: Fast badge pickup
  - Body: Shortest line at Moscone South Hall. Scan your QR at station 12.
  - CTA: Show My QR
  - Link: app://qr

- 10:15: Session RSVPs for “AI in Production” (capacity alert)
  - Title: Your session moving to Hall D
  - Body: “AI in Production” moved to Hall D. Starts 10:30.
  - CTA: Open Session
  - Link: app://session/8475
  - Priority: High

- 12:00: All attendees
  - Title: Lunch & dietary options
  - Body: Vegan/Gluten-free in West L2. Filter by icon on map.
  - CTA: Find Stations
  - Link: app://dining

- 15:45: Accessibility request holders
  - Title: Captioned sessions now
  - Body: Next captioned talks at 16:00 in rooms 2001 and 2003.
  - CTA: See Schedule
  - Link: app://accessibility

- 17:15: All attendees
  - Title: Daily survey—2 mins
  - Body: Tell us about Day 1. Help us improve Days 2–3.
  - CTA: Take Survey
  - Link: app://survey/day1

Onsite Day 2 (Wed, Sep 17)
- 07:45: All attendees
  - Title: Today at a glance
  - Body: Top picks and map shortcuts for Day 2.
  - CTA: Open Today
  - Link: app://home/today

- 09:50: Attendees without sessions 10:00–11:00
  - Title: Seats available near you
  - Body: Nearby sessions with open seats starting at 10:00.
  - CTA: Browse Now
  - Link: app://agenda?filter=nearby_open

- 12:05: Expo promotion
  - Segment: Not yet scanned into Expo
  - Title: Explore the Expo
  - Body: Meet 200+ exhibitors and claim your swag at Booth S-120.
  - CTA: Open Expo Map
  - Link: app://expo

- 16:30: All attendees
  - Title: Evening shuttles
  - Body: Departures every 10 min 16:45–19:00 from Howard St.
  - CTA: See Routes
  - Link: app://shuttle/routes

- 17:10: Session survey automation
  - Segment: Attended “Security by Design”
  - Title: Rate your session
  - Body: Quick 3 questions about “Security by Design.”
  - CTA: Give Feedback
  - Link: app://survey/9123

Onsite Day 3 (Thu, Sep 18)
- 08:00: All attendees
  - Title: Final day highlights
  - Body: Don’t miss the closing keynote and community lunch.
  - CTA: View Highlights
  - Link: app://home/today

- 11:30: Sustainability
  - Title: Help us go green
  - Body: Sort waste correctly—find stations near you.
  - CTA: View Map
  - Link: app://sustainability

- 14:45: All attendees
  - Title: Badge print closes at 16:00
  - Body: Need reprint? Visit West L1 by 16:00 today.
  - CTA: Find Desk
  - Link: app://poi/badge-desk-west

- 16:30: All attendees
  - Title: Thank you + on-demand
  - Body: Sessions on-demand next week. Watch for an email.
  - CTA: See What’s Next
  - Link: app://media

Contingency/Emergency (template—send immediately)
- Title: Safety alert
- Body: Please evacuate Moscone West via nearest exit. Follow staff guidance.
- CTA: View Safety Map
- Link: app://safety/evac-west
- Priority: Critical (override quiet hours, high sound/vibrate)

Post-event (Fri, Sep 19, 10:00)
- Segment: All attendees
- Title: We value your feedback
- Body: Complete the 5‑min survey by Sep 26 to help us improve.
- CTA: Take Survey
- Link: app://survey/post

Note: For each scheduled message, also create an in-app inbox post if the information should remain accessible later (e.g., surveys, transport schedules).

---

## Responsibilities

Roles and owners
- App Admin (Digital Experience): CMS configuration, publishing, routing/links, QA.
- Comms Lead (Marketing): Push calendar, copywriting, approvals, frequency management.
- Program Manager (Content): Agenda/speaker accuracy, session capacities, live changes.
- Venue Ops (Operations): Maps, POIs, F&B, room changes.
- Transportation Lead: Shuttle schedules, alerts.
- Registration Lead: Badge info, QR integration, onsite lines communication.
- Accessibility Lead: Services info, wayfinding, accommodations.
- Safety & Security Lead: Emergency content, notifications, policy enforcement.
- Social Lead: Social feed moderation, livestream links.
- Sponsorships: Sponsor assets, expo promotions.
- Insights/Research: Surveys, analytics, reporting.
- IT Lead: Wi‑Fi info, SSO/SSO, integrations uptime.

On-call escalation (onsite)
- Primary: App Admin (08:00–18:30)
- Secondary: Comms Lead
- Emergency: Safety Lead (24/7)
- Pager/Slack: #war-room-app with rotation schedule pinned

---

## Dependencies

Systems
- AppCMS v3.2 (content), Sessionize (agenda), RegSys (QR/status), MappedIn (maps), Qualtrics (surveys), Slido (Q&A), Zendesk (help), Firebase/APNs (push), DAM (assets).

Data integrations
- Agenda: Sessionize → AppCMS (hourly)
- Registration: RegSys → AppCMS (nightly + on-demand sync)
- Maps: MappedIn static pack + POI JSON
- Surveys: Qualtrics links with sessionId params
- Q&A: Slido event codes per session

Credentials & access
- Service accounts for each integration; keys stored in Secrets Vault; least-privilege roles.

External vendors
- Shuttle provider, Venue IT, Security firm, Captioning/ASL vendor.

Risk & mitigations
- Push service outage: Use in-app banners + venue signage; PA announcements for critical.
- Agenda sync failure: Manual CSV upload fallback; freeze edits until resolved.
- Network congestion: Pre-cache maps/agenda; distribute printed quick maps.
- High opt-outs: Shift to in-app inbox banners; reinforce Home tile.

---

## KPIs & Reporting

Engagement metrics
- Push: Delivery rate (>95%), open rate target (25–35%), deep link tap-through (>15%), opt-out rate (<5%).
- Content: Time on key modules, map opens per user, schedule additions per push.
- Surveys: Response rate (daily >20%, session >30%), average score.
- Ops: Help desk volume and resolution time; shuttle wait times.

Reporting cadence
- Daily onsite dashboard at 12:30 and 17:30 to War Room.
- End-of-event summary within 5 business days with top messages and learnings.

Attribution tagging
- UTM-style tags on deep links (e.g., app://agenda?src=push_d1_morning) to associate pushes with behaviors (adds, scans, survey completions).

---

## References & Templates

A) Push Message Template
- Internal name: D{#}-{Module}-{ShortTitle}
- Title (<=48 chars): …
- Body (<=140 chars): …
- CTA label: …
- Deep link (app://…): …
- Segment: All / Role / RSVP / Geofence …
- Priority: Critical / High / Standard
- Schedule (Local): YYYY-MM-DD HH:MM PDT
- TTL: e.g., 60 minutes
- Owner: …
- Approver: …
- Notes: Accessibility considerations, translation needs

B) Content Change Request Template
- Requester:
- Module:
- Change type: New / Update / Remove
- Description:
- Priority: Critical / Major / Minor
- Desired publish time:
- Screenshots/assets (links):
- Approvals needed:
- Submitted via: Ticket # / Slack link

C) Change Log Fields
- Date/time (local)
- Module
- Summary of change
- Requested by
- Published by
- Verification (✓ by QA)
- Notes/impact

D) UAT Checklist (pre-go-live)
- Navigation: All menu items route correctly
- Deep links: From push/inbox to correct views
- Map layers: Toggle rooms/POIs, zoom, floor switch
- Agenda filters: Track/Level/Capacity functional
- Surveys: Launch automatically at session end
- Accessibility: VoiceOver/ TalkBack labels verified
- Performance: Content loads under 2 seconds on venue Wi‑Fi
- Offline: Agenda and maps cached

E) Style & Tone Guidelines (push/in-app)
- Be specific, time-bound, and action-oriented.
- Use sentence case; avoid exclamation overload.
- Include location context (building/level/room).
- Avoid acronyms or define them once.
- Never include personal data or sensitive info.

F) Deep Link Patterns
- Agenda: app://agenda
- Session detail: app://session/{id}
- Today view: app://home/today
- Map POI: app://poi/{id}
- Shuttle route: app://shuttle/{routeId}
- Survey: app://survey/{id}
- Inbox message: app://inbox/{id}

---

Execution steps summary
1) Confirm module owners and grant AppCMS permissions.
2) Load all baseline content (T-30) and validate deep links.
3) Stand up integrations and verify syncs (agenda, reg, maps).
4) Populate Home tiles for Day 0–3 “Today” views.
5) Finalize push calendar and segments (T-7), pre-schedule non-critical.
6) Run UAT (T-5) and fix defects; cache offline packs.
7) Onsite: Operate content desk, publish changes per SLA, send pushes per calendar, monitor KPIs.
8) Post: Send thank-you/survey, archive content, publish report with learnings.