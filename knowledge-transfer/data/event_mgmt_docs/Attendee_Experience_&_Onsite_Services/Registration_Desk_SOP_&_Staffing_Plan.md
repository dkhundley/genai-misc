# Registration Desk SOP & Staffing Plan
Attendee Experience & Onsite Services

Document Title: Registration Desk SOP & Staffing Plan  
Version: 1.0  
Owner: Attendee Experience Lead  
Last Updated: 23 Aug 2025

---

## Overview
This document outlines the standard operating procedures (SOP) and staffing plan for the registration desk at a mid-size conference. It is written for registration staff, volunteers, and managers to execute check-in, equipment setup, queue management, and issue resolution without additional context.

Example scenario used in this SOP:
- Event: ACME Annual Summit 2025
- Venue: City Convention Center, Hall B Lobby
- Dates: Tue–Thu, 14–16 Oct 2025
- Attendees: 1,200 total; expected peak arrival Tue 08:00–10:30 and Wed 08:00–09:30
- Registration Hours:
  - Mon (13 Oct): Build & tech setup 10:00–18:00 (no attendees)
  - Tue (14 Oct): 07:00–18:00
  - Wed (15 Oct): 07:30–17:30
  - Thu (16 Oct): 08:00–14:00

Goals and service levels:
- 80% of attendees processed within 5 minutes of joining the line
- Average throughput: 50–60 check-ins per staffed station per hour during peak
- Queue length not to exceed 30 attendees at main desk; trigger overflow measures at 20+

---

## Floor Plan & Physical Setup
Zones (left-to-right facing the desk):
1. Welcome/Greeter Zone: 2 staff with handheld scanners and signage.
2. Self-Check Kiosk Zone: 6 kiosks (touchscreen + scanner + badge printer).
3. Assisted Check-In Zone: 8 seated stations (laptop + scanner + badge printer).
4. Issue Resolution Desk: 2 desks offset to the side with seating privacy.
5. Badge Reprint & Onsite Sales: 2 stations; near cashier signage.
6. Supplies & Back-of-House: behind desk; secure storage for badges, lanyards, ribbons, merch, tech spares.
7. ADA Priority Lane: clearly signed; <3-minute target wait.
8. VIP/Speaker Desk: 1 station near a quiet corner; no queue.

Signage:
- Overhead banners at 8–10 ft height, font 200+ pt: “Check-In,” “Self-Check,” “Assisted,” “Issues,” “Onsite Registration,” “ADA Priority,” “VIP/Speakers.”
- Floor standing wayfinding (A-frames) at lobby entrance and 25 ft intervals.
- Multilingual quick guides (EN/ES) at kiosks.

Accessibility:
- 1 lowered counter at 34 in height.
- 36 in clear path in all lanes; stanchions placed to provide turning radius.
- Seating available at Issue Resolution.

Power and cable management:
- Dedicated 20A circuits per 4 stations; UPS on each printer bank.
- Gaffer tape and cable ramps on all walkways; daily inspection.

---

## Equipment & Supplies
Core equipment (label each with zone-station ID, e.g., “A-03”):
- Laptops: 12 (Windows 11/Chrome), power adapters, mouse; 2 spares.
- Barcode scanners: 12 USB; 2 spares.
- Badge printers: 12 (e.g., Zebra ZC300), 2 spares; cleaning kits.
- Self-check kiosks: 6 touchscreens with integrated scanner + printer.
- Receipt/label printers: 2 for onsite Reg receipts or ADA labels.
- Networking: 1 managed switch (24-port), pre-configured; 2 MiFi backups; 2 long-range APs; 2 x 50 ft CAT6; 20 x 10 ft CAT6.
- Power: 12 x 6-outlet strips with surge; 6 UPS units (1000VA).
- Consumables: 
  - Badge stock: 1,500 pre-printed fronts, 300 backup blanks
  - Lanyards: 1,400
  - Badge holders: 1,400
  - Ribbons: 300 “Speaker,” 150 “Sponsor,” 250 “VIP,” 200 “Exhibitor”
  - Cleaning wipes, microfiber cloths, hand sanitizer
  - Tape (gaffer), zip ties, scissors, spare pens and notepads

Network plan:
- Dedicated SSID: ACME-Reg (WPA2), bandwidth 50/50 Mbps minimum.
- Ethernet preferred for stationary stations; Wi-Fi as backup.
- DHCP reservation for printers; fallback to USB printing if LAN fails.

Software:
- Registration platform: RegPro Cloud (example)
- Payment: Square terminals (NFC/EMV), credit only; no cash.
- Comms: Slack channel #reg-ops; WhatsApp group for vendor liaisons.
- Incident log: Google Sheet “Reg-Desk Daily Log”
- Dashboard: RegPro Ops View (check-ins per hour, queue length)

---

## Standard Operating Procedures

### 1) Pre-Event (T-14 to T-1)
- Validate attendee data in RegPro; lock badge templates (T-7).
- Finalize printer drivers and test print 20 sample badges (T-7).
- Order consumables with 20% overage (T-14).
- Prepare staff training deck; schedule 30-min live run-through (T-3).
- Assign station labels and print asset tags (T-3).
- Share onsite comms plan and escalation matrix (T-2).
- Prepare signage proofs; send to print (T-10), receive and QA (T-3).

Deliverables:
- Station map v1.2
- Roster and shift assignments
- Checklists printed and laminated

### 2) Build & Setup (T-1: Mon)
- Mark floor with tape according to plan.
- Set stanchions; verify ADA lanes unobstructed.
- Deploy tables, skirting, and power; test circuits with load.
- Place equipment per station ID; cable manage.
- Network: connect switch to venue drop; verify speed; set VLAN if provided.
- Install drivers; log in to RegPro; perform test scans and prints.
- Set up MiFi and APs as fallback; label SSID/password cards.
- Inventory consumables; create “active” stock bins per station.
- Print “quick help” cards for common issues.

Sign-offs required by:
- Registration Manager (functionality)
- IT/Badge Tech Lead (network and printing)
- Venue Liaison (power, safety)
- Security (emergency egress clear)

### 3) Daily Opening Checklist (D-0 60 minutes before doors)
- Power on UPS, printers, laptops in order (UPS > printer > laptop).
- Log in to RegPro; open “ACME 2025 Onsite – Day X.”
- Test scan and print at each station (1 badge); reprint test badges marked “TEST.”
- Load lanyands/badge holders at front; refill ribbons by role.
- Open Square terminals; run $0.01 test then void.
- Wipe surfaces, confirm signage in place, music level acceptable.
- Brief team (10 minutes): updates, schedule, targets, VIP list.
- Set queue monitoring board to zero; assign queue lead.

### 4) Standard Check-In (Assisted)
- Greet and triage: “Do you have your QR code? If yes, to Self-Check; if no, Assisted.”
- Lookup options: scan QR from email/app; or search by name/company.
- Verify attendee details (name, company, pronouns optional).
- Print badge; attach ribbon(s); hand lanyard and holder.
- Confirm consent for badge scanning (GDPR notice displayed).
- Provide quick orientation (program, venue map).
- Close interaction: “Anything else I can help with?” Average 60–90 seconds.

### 5) Self-Check Kiosks
- Instructions on screen + tabletop card:
  1) Scan QR
  2) Confirm name and spelling
  3) Tap Print
- Attendant monitors 2–3 kiosks; assists with jams or name changes.
- If kiosk error > 15 seconds, redirect to Assisted.

### 6) Onsite Registration (New Purchase)
- Direct to “Onsite Registration” desk.
- Steps:
  1) Collect consent + privacy notice.
  2) Create record in RegPro; select correct ticket type and price.
  3) Process payment via Square (no cash; email receipt only).
  4) Print badge; provide welcome materials.
- If corporate PO or voucher: validate code in RegPro; no manual overrides without Manager approval.

### 7) Badge Reprint & Name Changes
- Reprint policy: 1 complimentary reprint; subsequent reprints $25 fee or manager waiver.
- Identity verification: last name + email + ID check if mismatch.
- Mark lost badge as void in RegPro; reprint new with unique barcode.
- Name change/substitution: permitted with company approval email or original purchaser present; update record and print.

### 8) Queue Management
- Real-time monitoring: Queue Lead updates a whiteboard every 5 minutes (count by section).
- Thresholds:
  - 10+ at Self-Check: redeploy 1 greeter to assist.
  - 20+ at Assisted: open additional station or convert Issue desk to Assisted temporarily.
  - 30+ overall: trigger Overflow Plan: deploy extra stanchions, triage line (QR ready vs not ready), announce wait times.
- Throughput targets: 1 attendee per station per 60–75 seconds peak; aim 50–60/hour per staffed station.
- ADA and VIP lanes: never merged; maintain priority.

### 9) Issue Resolution & Escalation
Common issues and first-line steps:
- Barcode not scanning: manual lookup by name; check check-in status.
- Payment failed: retry; switch to alternate terminal; if still failing, send secure payment link via RegPro.
- Missing registration: search by email variations; check duplicates; if not found, process onsite purchase or escalate.
- Speaker/Exhibitor list mismatch: check sponsor uploads; escalate to Sponsor Desk contact.
- Name misspelling: update record; reprint.
- Special accommodations: seat, water, quiet space; notify Accessibility POC.

Escalation matrix:
- Tier 1 (Station Agent or Greeter): up to 3 minutes trouble-shooting.
- Tier 2 (Troubleshooting Specialist): complex data issues, payment exceptions. SLA 5 minutes.
- Tier 3 (Registration Manager): policy exceptions, VIP support, financial overrides.
- Tier 4 (Platform Support/Venue IT): system outages, network failures.

Escalation contacts (example):
- Registration Manager: J. Patel, +1-555-0100
- IT/Badge Tech Lead: M. Rivera, +1-555-0101
- Finance Onsite: L. Chen, +1-555-0102
- Venue IT: ext. 7788
- Security: ext. 1100

### 10) Health, Safety, and Conduct
- Keep cables covered; stanchion feet inside tape lines.
- Hydration and 10-minute breaks every 2 hours; rotate stations.
- De-escalation script for upset attendees; call Security if threats occur.
- Infectious disease hygiene: hand sanitizer at each station; optional masks available.

### 11) End-of-Day Closing Checklist
- Reconcile counts: RegPro total check-ins vs. badge stock usage; variance ≤ 2%.
- Close Square terminals; verify $0 open tabs.
- Inventory consumables; refill for next day.
- Power down in reverse order (laptops > printers > UPS).
- Wipe and cover printers; secure badges and ribbons in lockable bins.
- Update Incident Log and Daily Desk Report; post in #reg-ops.
- Debrief (10 min): issues, wins, plan for tomorrow.

### 12) Post-Event Closeout (T+0)
- Export final attendance and reprint counts.
- Pack equipment by station ID; note any damage; return rentals.
- Archive incident log, staffing timesheets, EOD reports.
- Post-mortem within 5 business days: metrics vs. SLAs; improvement plan.

---

## Roles & Responsibilities
- Registration Manager (RM)
  - Owns SOP execution, policy decisions, SLAs, escalations.
- Shift Leads
  - Run briefings, assign breaks, monitor performance and morale.
- IT/Badge Tech Lead
  - Network, hardware, and printer setup; resolves outages; keeps spares ready.
- Queue Lead
  - Monitors queue health; moves staff between zones; triggers overflow plan.
- Station Agents (Assisted Check-In)
  - Execute standard check-in; maintain pace and accuracy.
- Self-Check Attendants
  - Assist kiosk users; keep printers fed; clear jams.
- Troubleshooting Specialists
  - Handle data, payment, and account exceptions; document resolutions.
- Greeters
  - Welcome, triage, and direct attendees; promote QR readiness.
- Badge Reprint/Onsite Sales Agents
  - Manage reprints, name changes, onsite purchases; ensure policy compliance.
- Accessibility POC
  - Ensures ADA compliance and support.
- Venue Liaison
  - Coordinates with venue for power, furniture, and safety.
- Security Liaison
  - Point person for incidents requiring security.

Comms
- Slack #reg-ops for updates; #reg-tech for technical alerts; radio channel 3 for on-floor.
- Code words: “Blue” = need manager at desk; “Gold” = VIP arrival; “Green” = open extra station.

---

## Staffing Plan & Roster

Staffing model assumptions:
- Peak throughput target: 8 assisted stations x 55/hour = 440/hour
- Self-check share: 40% of arrivals during peak
- Coverage includes redundancy for breaks and issues desk

Shifts by day (example names; adjust as needed)

Tue 14 Oct (07:00–18:00)
- Shift A (06:30–11:00)
  - Registration Manager: J. Patel
  - Shift Lead: A. Gomez
  - Queue Lead: T. Nguyen
  - Greeters: 3 (R. Shaw, D. Ali, P. Ortiz)
  - Self-Check Attendants: 3 (K. Lin, H. Baker, V. Rao)
  - Assisted Agents: 8 (S. Kim, L. Brown, G. Silva, E. Davis, N. Khan, W. Ortiz, C. Young, B. Lee)
  - Troubleshooting: 2 (M. Chen, F. O’Neil)
  - Reprint/Onsite Sales: 2 (J. Wu, I. Ahmed)
  - IT/Badge Tech Lead: M. Rivera
- Shift B (10:30–15:00)
  - Shift Lead: C. Patel
  - Queue Lead: same as A until 12:00, then J. Park
  - Greeters: 2
  - Self-Check Attendants: 2
  - Assisted Agents: 6
  - Troubleshooting: 1
  - Reprint/Onsite Sales: 1
  - IT/Badge Tech: on-call
- Shift C (14:30–19:00 close)
  - Shift Lead: R. Davis
  - Greeters: 2
  - Self-Check Attendants: 2
  - Assisted Agents: 4
  - Troubleshooting: 1 (part-time)
  - Reprint/Onsite Sales: 1

Wed 15 Oct (07:30–17:30)
- Shift A (07:00–11:00 peak)
  - RM: J. Patel
  - Leads: same composition as Tue A
- Shift B (10:30–15:00)
  - Slightly reduced: Assisted 5, Self-Check 2, Greeters 2
- Shift C (14:30–18:00 close)
  - Assisted 4, Self-Check 2, Reprint 1, Troubleshooting on-call

Thu 16 Oct (08:00–14:00)
- Shift A (07:30–11:30)
  - Assisted 6, Self-Check 2, Greeters 2, Reprint 1, Troubleshooting 1
- Shift B (11:00–15:00 closeout)
  - Assisted 3, Self-Check 1, Reprint 1, IT/Badge Tech present for teardown

Break plan:
- 10 minutes every 2 hours + 30-minute meal break for shifts >6 hours.
- Shift Leads stagger breaks; maintain minimum coverage:
  - Peak: Assisted ≥6, Self-Check ≥2, Greeters ≥2, Troubleshooting ≥1.

Briefings:
- Daily 06:45/07:15 (Tue/Wed) and 07:45 (Thu) — 10 minutes.
- End-of-day debrief: last 10 minutes of final shift.

On-call list:
- Platform support (RegPro): +1-555-0130
- Badge printer vendor: +1-555-0131
- Venue duty manager: +1-555-0132

---

## Dependencies and Contingencies

Dependencies:
- Venue: power drops, tables, stanchions, signage installation permissions.
- Registration platform: stable API and offline mode enabled.
- Badge printers: drivers installed; compatible ribbon stock.
- Payment: working internet or cellular data for Square terminals.

Contingency plans:
- Internet down:
  - Switch to MiFi hotspots (SSID: ACME-Backup). If full outage persists, move to Offline Mode in RegPro; capture names and emails; batch sync later.
- Power outage:
  - UPS provides 10–15 minutes; triage to manual check-in sheet; suspend printing; communicate ETA from venue.
- Printer jam or failure:
  - Use cleaning card; reboot printer; swap to spare if >2 minutes unresolved; log serial number and issue.
- Long queue overflow:
  - Open Issue Desk as Assisted; deploy additional greeter; print badge stock pre-emptively for pre-registered VIPs; announce QR readiness line.
- Platform outage:
  - Switch to CSV backup list (export at D-1) and manual badge write-ins on blank stock; collect business cards for reconciliation; offer reprint later.

---

## Data Security & Compliance
- Least-privilege access in RegPro; unique logins per staff; MFA for managers.
- No photographing attendee lists; no storing data locally on laptops.
- Payment handled on PCI-compliant terminals; staff never enter or write down PANs.
- For reprints, verify identity; do not disclose personal data aloud.
- Shred any temporary printed lists post-event.
- Display privacy notice at check-in; provide link/QR to policy.

---

## KPIs & Reporting
Real-time metrics (update hourly):
- Total check-ins, by ticket type
- Average processing time per station (manual timing sample of 10)
- Queue length snapshot every 15 minutes
- Reprint count and reasons
- Onsite sales count and revenue

Daily Desk Report (submitted by Shift Lead):
- Open/close times, staff on duty
- Peak queue length and time
- Incidents and resolutions
- Inventory usage (badges, lanyards, ribbons)
- Tech issues and downtime minutes
- Action items for next day

Targets:
- SLA: 80% processed ≤5 minutes
- Reprint rate < 7% of total
- Printer downtime < 2% per unit
- Data discrepancy corrections < 1% of total check-ins

---

## Scripts and Quick Guides

Greeter script:
- “Welcome to ACME Summit! Do you have your QR code ready? If yes, please use our Self-Check kiosks to the left. If you need assistance or have changes, our Assisted Check-In is straight ahead.”

De-escalation script:
- “I understand this is frustrating, and I’m here to help. Let me bring in our Registration Manager to resolve this quickly. Can I offer you a seat while I get them?”

Payment script:
- “We accept credit or contactless payment. Your receipt will be emailed—what’s the best email address to use?”

VIP arrival:
- “Welcome, [Title LastName]. We have your badge ready. May I escort you to the lounge?”

---

## Checklists

Opening (laminated)
- Power on UPS > printers > laptops
- Log in to RegPro; verify event day
- Test scan/print at each station
- Load consumables; verify printer ribbon status
- Square terminals online; $0.01 test voided
- Signage, stanchions, ADA lane clear
- Quick brief completed; queue board at zero

Mid-day
- Wipe printers and scanners
- Refill lanyards and badge stock
- Review KPIs; adjust staffing
- Validate MiFi battery levels

Closing
- Reconcile counts vs. prints
- Power down laptops > printers > UPS
- Secure consumables in locked bins
- Update Incident Log and Daily Desk Report
- Debrief; note next-day actions

---

## Forms & Templates

Incident Log (fields)
- Timestamp
- Reporter
- Category (Tech/Payment/Data/Safety/Other)
- Description
- Action Taken
- Escalation Level
- Status (Open/Closed)

Daily Desk Report (example)
- Date/Shift:
- Staff on duty (names/roles):
- Check-ins total:
- Peak queue length/time:
- Reprints (count/reasons):
- Onsite sales (count/revenue):
- Tech issues/downtime:
- Inventory used:
- Notes/Actions for tomorrow:

Lost Badge/Reprint Authorization
- Attendee name:
- Email:
- Reason for reprint:
- ID verified? Y/N
- Fee applied? $____
- Approved by:

Supply Requisition
- Item:
- Current qty:
- Threshold:
- Requested qty:
- Needed by:

Signage Copy
- “Self-Check In: Scan your QR code to print your badge.”
- “Assisted Check-In: Name lookup, changes, help here.”
- “ADA Priority Lane.”
- “VIP & Speakers.”

---

## References
- Registration platform runbook: RegPro Cloud Onsite Guide v3.1
- Badge printer quick start: Zebra ZC300 2-page setup (with cleaning card cycle)
- Venue operations manual: City Convention Center Exhibitor Services
- Accessibility standards: ADA 2010 Standards, relevant sections for service counters

---

## Responsibilities Summary Matrix

- Registration Manager: approvals, escalations, KPI accountability
- Shift Lead: staffing, breaks, daily reports
- IT/Badge Tech: hardware/software/network uptime, spares
- Queue Lead: queue thresholds, overflow triggers
- Agents (Assisted/Self-Check): check-in accuracy and speed
- Troubleshooting: data/payment issues, documentation
- Reprint/Onsite Sales: policy compliance, receipts
- Greeters: triage, QR readiness, wayfinding
- Accessibility POC: guest assistance, ADA compliance
- Venue/Security Liaison: safety, incident response

---

This SOP and staffing plan should be reviewed 7 days prior to the event and re-briefed with all team members on T-1 during setup. Adjust staffing counts and thresholds based on actual on-site metrics captured during the first peak period.