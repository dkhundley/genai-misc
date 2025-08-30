# Attendee Experience & Onsite Services
## Badging, Access Control & Credential Hierarchy

Document Title: Badging, Access Control & Credential Hierarchy  
Document Description: Defines badge types, access levels, encoding specs, and checkpoint layouts for secure flow. Format: credential matrix and checkpoint map.

Version: 1.0  
Owner: Access Control Lead (Registration & Onsite Services)  
Last Updated: 2025-08-23

---

## Overview

This document establishes the credential hierarchy, badge specifications, access levels, device configurations, checkpoint layout, and operating procedures for controlling attendee movement at the Global Tech Summit 2026.

Event profile:
- Name: Global Tech Summit 2026
- Dates: August 12–14, 2026 (Move-in: Aug 10–11; Move-out: Aug 15)
- Venue: Metro Convention Center (Halls A–B, Ballroom C, Meeting Rooms 101–120)
- Expected volume: 5,000 attendees; peak ingress 2,200/hour
- Access control approach: Hybrid (NFC/QR handhelds + fixed portals at high throughput points)

Objectives:
- Ensure only authorized individuals enter controlled zones.
- Maintain safe, efficient flow with ADA accommodations.
- Provide auditability and rapid incident response.
- Enable degraded operations during network interruptions.

---

## Key Details

### 1) Zones and Checkpoints

Defined zones:
- Z1 Lobby & Registration
- Z2 Expo Hall (Halls A–B)
- Z3 General Session (Ballroom C)
- Z4 Breakouts (Meeting Rooms 101–120)
- Z5 Back-of-House (BOH: docks, service corridors)
- Z6 Green Room & Speaker Ready
- Z7 Press Room
- Z8 Staff Office & Operations Hub
- Z9 Sponsor Suites
- Z10 Evening Events (Offsite)

Primary checkpoints (physical control points):
- CP1 Registration Lobby (entry to credentialed areas)
- CP2 Expo Hall North Entrance (fixed portals)
- CP3 Expo Hall South Entrance (fixed portals)
- CP4 General Session Ballroom entry (handheld lanes)
- CP5 BOH Access (secured door readers)
- CP6 Speaker Ready / Green Room
- CP7 Press Room Entrance
- CP8 Staff Office
- CP9 Sponsor Suites Corridor
- CP10 Evening Event (Offsite venue wristband + NFC)

Open hours (subject to final schedule):
- Move-in (Aug 10–11): CP2/3/5 open for Exhibitors, Crew, Staff (07:00–20:00)
- Show days (Aug 12–14):
  - CP1 Registration: 07:30–18:00
  - CP2/3 Expo Hall: 09:30–17:30
  - CP4 General Session: 08:30–10:30 and 15:30–17:00
  - CP5 BOH: 06:00–22:00
  - CP6 Speaker Ready: 07:00–17:00
  - CP7 Press Room: 08:00–17:00
  - CP8 Staff Office: 07:00–20:00
  - CP9 Sponsor Suites: 09:00–18:00
  - CP10 Evening Event (Aug 13 only): 18:30–22:30

Throughput assumptions:
- Fixed portal (RFID/NFC gate): ~1,200 persons/hour/lane
- Handheld scanner lane (NFC/QR): ~600 persons/hour/lane
- Visual check lane (fallback): ~300 persons/hour/lane

---

### 2) Credential Hierarchy (Badge Types and Access)

Legend:
- Y = Full access during show hours
- T = Time-bound access (see notes)
- M = Move-in/move-out only (Aug 10–11, 15)
- E = Escorted only with Staff/Security
- — = No access

| Badge Type        | Z1 Lobby | Z2 Expo | Z3 Gen Session | Z4 Breakouts | Z5 BOH | Z6 Green/Speaker | Z7 Press | Z8 Staff Office | Z9 Suites | Z10 Evening |
|-------------------|----------|---------|----------------|--------------|--------|------------------|----------|-----------------|-----------|-------------|
| Attendee          | Y        | Y       | Y              | Y            | —      | —                | —        | —               | T (invited) | T (ticket) |
| Speaker           | Y        | Y       | Y              | Y            | E      | Y                | —        | —               | T (invited) | T (ticket) |
| Exhibitor         | Y        | Y       | T (as ticketed)| Y            | M      | —                | —        | —               | Y (if sponsor) | T (ticket) |
| Sponsor (Staff)   | Y        | Y       | Y              | Y            | E      | —                | —        | —               | Y         | T (ticket) |
| VIP               | Y        | Y       | Y (priority)   | Y            | —      | T (escorted)     | —        | —               | Y         | Y          |
| Media/Press       | Y        | Y       | Y              | Y            | —      | E                | Y        | —               | T (invited) | T (ticket) |
| Staff (Ops)       | Y        | Y       | Y              | Y            | Y      | Y                | Y        | Y               | Y         | Y          |
| Production Crew   | Y        | Y       | Y              | Y            | Y      | Y                | —        | Y               | —         | T (working)|
| Security          | Y        | Y       | Y              | Y            | Y      | Y                | Y        | Y               | Y         | Y          |
| Vendor (Facility) | Y        | E       | E              | E            | Y      | E                | —        | E               | —         | —          |

Notes:
- Time-bound entries: Sponsor Suites (Z9) by invitation windows; Evening Event (Z10) by ticket scan and exchange for wristband.
- BOH (Z5) is strictly restricted—only Staff, Crew, Security, and approved Vendors.

Role codes:
- ATT, SPK, EXH, SPN, VIP, MED, STF, CRW, SEC, VEN

---

### 3) Badge Design & Encoding Specifications

Physical badge:
- Size: CR80 (86 x 54 mm), vertical orientation
- Stock: 30 mil PVC core with 0.3 mil holographic overlay, UV reactive watermark
- Lanyards (breakaway): color-coded by role
  - ATT Blue #1E73BE, SPK Purple #6F52ED, EXH Orange #F28C28, SPN Teal #1EBEA5, VIP Gold #C8A048,
    MED Red #C23B22, STF Black #2B2B2B, CRW Gray #7A7A7A, SEC Navy #1B2A41, VEN Green #3C9D32
- Visual cues:
  - Role label in 24pt bold; color bar top edge; iconography (e.g., mic for Speaker, shield for Security)
  - BOH Allowed indicator “BOH” printed in small black box (Staff/Crew/Security only)
  - Photo: required for Staff, Crew, Security; optional for others
  - QR code front; NFC logo indicator

Encoding:
- QR Code: Version 5, ECC H
- NFC: NTAG213, NDEF text record (read-only)
- Optional UHF for portals: EPC Gen2 (RAIN RFID) encoded with 96-bit EPC per schema

Data model (logical credential):
- badgeId: UUIDv4
- personId: GUID (from registration system)
- roleCode: one of [ATT, SPK, EXH, SPN, VIP, MED, STF, CRW, SEC, VEN]
- access: array of zone codes [Z1..Z10], with time constraints where applicable
- validFrom/validTo: ISO8601 UTC timestamps
- eventId: GTS-2026
- sig: digital signature of payload (ECDSA P-256, SHA-256), base64

QR payload (JSON, compact):
{
  "eid":"GTS-2026",
  "bid":"1b8f1b3f-93b2-4fc1-8a5a-5a4c3ac62fd1",
  "rid":"ATT",
  "acc":{"Z1":"Y","Z2":"Y","Z3":"Y","Z4":"Y","Z9":"T","Z10":"T"},
  "vf":"2026-08-10T00:00:00Z",
  "vt":"2026-08-15T06:00:00Z",
  "s":"MEUCIQCO0...truncated...Wg=="
}

NFC NDEF text contents:
GTS-2026|1b8f1b3f-93b2-4fc1-8a5a-5a4c3ac62fd1|ATT|2026-08-10T00:00:00Z|2026-08-15T06:00:00Z|MEUCIQCO0...Wg==

UHF EPC layout (96-bit):
- Header 8b, Filter 3b, Partition 3b
- Company Prefix 24b, BadgeId hash 48b, Role 10b
- Example Company Prefix: 0x15ACCE; BadgeIdHash: first 48 bits of SHA-256(bid)

Security:
- Private signing key stored in HSM; public key distributed to devices.
- Devices validate signature offline; CRL updated every 30 min when network available.
- Lost/badged revoked list stored locally and synchronized.

Privacy:
- No PII in QR/NFC. All PII remains in registration system; devices query by badgeId if needed.

Printing specs:
- DPI 300; black resin for text; CMYK for color bar.
- Onsite reprint includes “REPRINT” watermark and logs reason.

---

### 4) Devices, Software, and Configuration

Devices:
- Handheld scanners (Android) with NFC + 2D imager: 40 units
- Fixed portals (dual-lane gates) with RAIN RFID + NFC pad: 6 units (3 at CP2, 3 at CP3)
- Door readers (BOH, rooms): 12 PoE units
- Badge printers (retransfer): 6 with lamination modules

Software:
- Access Control App v4.2 (supports offline signature validation)
- Portal Controller v3.1
- Registration System: RegFlow 2026
- Integration: REST API with OAuth2 (client credentials)

Configuration highlights:
- Roles-to-zones mapping uploaded as JSON policy
- Time windows for Z9, Z10 configured as events
- Device groups: PORTAL_EXPO, HH_GEN, HH_GUEST, DOOR_BOH
- Throughput mode:
  - Portals: NFC priority; fallback to UHF EPC when NFC absent
  - Handhelds: NFC tap; fallback QR scan; visual check as last resort

Network:
- Dedicated VLAN for access control; WPA2-Enterprise for handhelds; PoE for door readers
- Local edge appliance caches CRL and policy; UPS-backed

---

### 5) Checkpoint Map and Staffing Plan

Checkpoint equipment and staffing:

- CP1 Registration Lobby
  - 10 handheld scanners (guest flow)
  - 6 badge printers at Registration counters
  - Staff: 1 Lead, 8 Agents, 4 Floaters
  - Functions: badge pickup, reprint, help desk; not a hard access control point

- CP2 Expo Hall North
  - 3 portal lanes + 2 handheld lanes (1 ADA wide lane)
  - Staff: 1 Supervisor, 6 Ushers, 2 Troubleshooters
  - Expected peak: 1,800 pph

- CP3 Expo Hall South
  - 3 portal lanes + 2 handheld lanes
  - Staff: 1 Supervisor, 6 Ushers, 2 Troubleshooters

- CP4 General Session Ballroom
  - 6 handheld lanes (2 priority/VIP)
  - Staff: 1 Supervisor, 8 Ushers, 2 VIP Hosts

- CP5 BOH
  - 4 door readers (docks and service corridors), no public lanes
  - Staff: 1 Security Lead, 4 Guards

- CP6 Speaker Ready / Green Room
  - 2 door readers + 2 handhelds
  - Staff: 1 Room Manager, 2 Attendants

- CP7 Press Room
  - 1 door reader + 1 handheld
  - Staff: 1 Press Manager, 1 Attendant

- CP8 Staff Office
  - 1 door reader
  - Staff: 1 Ops Coordinator

- CP9 Sponsor Suites Corridor
  - 2 handhelds at corridor; suites managed by sponsors
  - Staff: 1 Corridor Host, 2 Attendants

- CP10 Evening Event (Offsite)
  - 6 handheld lanes, wristband issuance
  - Staff: 1 Lead, 10 Ushers, 2 Security

Signage and lane layout:
- Clearly marked role-based lanes at CP4 (VIP Priority lanes).
- ADA lane minimum 36” width at CP2/CP3 with ramped turnstile.
- “Tap or Scan” visual instructions with iconography at each point.

---

### 6) Operating Procedures

Ingress flow (show days):
1. Attendee approaches checkpoint.
2. Tap NFC; if fail, scan QR; if fail, visual cue check + manual lookup.
3. Device verifies signature and validity; checks zone/time policy and CRL.
4. Green: Gate opens / usher waves through. Red: Deny with reason displayed.
5. If denied:
   - Common reasons: Invalid zone, outside time window, revoked, expired.
   - Direct to Resolution Desk or CP1 Registration for reprint/upgrade.

Onsite badge issue and reprint:
- SLA: Standard issue <3 minutes; reprint <7 minutes.
- Required verification:
  - Attendee: photo ID + email confirmation
  - Staff/Crew/Security: government ID + pre-approved staffing list
- Lost badge policy:
  - First reprint: free for Attendee; staff must report to manager
  - Second reprint: $50 fee or manager approval
  - Previous credential revoked immediately; record reason code

Escort protocol (zones marked “E”):
- Only Staff or Security may escort; handheld must log entry with “Escort” flag and escort badgeId.
- Vendor entries logged with purpose and expected duration.

Incident handling:
- If gate/device fails: switch lane to handheld; portal taken offline (cone and sign).
- Network down: devices operate offline; continue validating signatures; CRL considered stale after 6 hours—Security Lead decides on visual check thresholds.
- Counterfeit detection: verify hologram/UV watermark; confiscate if fraudulent and notify Security Lead.
- Medical or safety incident: hold lanes to create egress path; follow venue safety protocol.

Data retention:
- Access logs stored locally and synced to cloud; 90-day retention then anonymized.
- Incident and reprint logs retained for 1 year.

---

## Responsibilities

- Access Control Lead (Owner)
  - Owns matrix, policies, device config, and change control.
- Registration Lead
  - Manages data flows, printing, reprints, and attendee support.
- Security Lead
  - Oversees checkpoint staffing, incident response, BOH enforcement.
- IT/Network Engineer
  - VLAN, Wi-Fi, PoE, edge caching, uptime monitoring.
- Vendor: Access Hardware/Software
  - Supplies devices, portals, and onsite tech support; ensures firmware at required versions.
- Zone Managers (Expo, General Session, Breakouts, Press, Suites)
  - Enforce local policies; coordinate with Access Control Lead on exceptions.
- Volunteer/Ushers
  - Lane management, wayfinding, ADA assistance.
- Compliance & Privacy Officer
  - Ensures data minimization and retention compliance.

Escalation tree (real-time):
- Lane Usher → Checkpoint Supervisor → Security Lead → Access Control Lead → Event Director

---

## Dependencies

- Finalized registration fields and role codes (T-30 days)
- Signed-off credential matrix and zone map (T-28 days)
- Integration credentials and API endpoints (T-21 days)
- Device inventory and shipping to venue (T-10 days)
- Power and network drops at checkpoints approved (T-10 days)
- Venue plan and fire marshal egress approvals (T-14 days)
- Signage artwork and print (T-10 days)
- Wristbands for offsite event (color-shift, tamper-evident) (T-7 days)

---

## Timeline and Milestones

- T-45 days: Draft credential matrix; initial vendor coordination
- T-30 days: Freeze roles/zones; begin device provisioning
- T-21 days: Complete API integration and signature key distribution
- T-14 days: Dry-run in warehouse; portal and handheld functional tests
- T-7 days: Final signage print; staff training materials distributed
- T-2 days: Onsite install of portals, door readers; network validation
- T-1 day: Full end-to-end rehearsal; import final reg list; issue test badges; CRL sync test
- Show Days: Daily 07:00 stand-up; 17:30 debrief and metrics review
- T+1 day: Decommission devices; export logs; key revocation; vendor check-in
- T+7 days: Postmortem with metrics and lessons learned

---

## Testing & Acceptance Criteria

- Signature validation offline for 100% of test badges (50-sample across all roles)
- CRL sync within 5 minutes after revoke action (online mode)
- Portal throughput ≥1,100 pph/lane sustained for 10 minutes
- Handheld denial reasons accurate for 10/10 scripted negative tests
- ADA lane unobstructed; gate opening force <5 lbf where applicable
- BOH doors fail-safe on fire alarm and relock on reset

---

## Risk & Contingency

- Network outage: enable Local-Only Mode; rotate staff to visual checks; deploy paper wristbands for Z10 if needed.
- Printer failure: swap to hot spare; maintain 20% extra consumables (ribbons, cards, laminates).
- Counterfeit attempt surge: escalate to Security; switch to photo verification for suspect roles; random secondary checks.
- Data breach concern: immediate key revocation; devices accept only previously cached credentials; issue day-specific wristbands for Z2/Z3.

---

## References & Templates

Policy JSON (roles-to-zones):
{
  "version":"2026.1",
  "eventId":"GTS-2026",
  "roles":{
    "ATT":["Z1","Z2","Z3","Z4","Z9:T","Z10:T"],
    "SPK":["Z1","Z2","Z3","Z4","Z6","Z9:T","Z10:T"],
    "EXH":["Z1","Z2","Z4","Z5:M","Z9:Y?Sponsor","Z10:T"],
    "SPN":["Z1","Z2","Z3","Z4","Z9","Z10:T"],
    "VIP":["Z1","Z2","Z3","Z4","Z6:T","Z9","Z10"],
    "MED":["Z1","Z2","Z3","Z4","Z7","Z9:T","Z10:T"],
    "STF":["Z1","Z2","Z3","Z4","Z5","Z6","Z7","Z8","Z9","Z10"],
    "CRW":["Z1","Z2","Z3","Z4","Z5","Z6","Z8","Z10:T"],
    "SEC":["Z1","Z2","Z3","Z4","Z5","Z6","Z7","Z8","Z9","Z10"],
    "VEN":["Z1","Z5","Z8:E"]
  }
}

CSV template (badge export to printer):
badgeId,personId,firstName,lastName,roleCode,company,photoUrl,validFrom,validTo,notes
uuid-...,guid-...,Alex,Nguyen,ATT,Example Corp,https://...,2026-08-10T00:00:00Z,2026-08-15T06:00:00Z,
uuid-...,guid-...,Priya,Shah,SPK,Keynote Inc,https://...,2026-08-10T00:00:00Z,2026-08-15T06:00:00Z,Keynote Thu

Device configuration checklist:
- Time synced (NTP) ±2s
- Policy version 2026.1 applied
- Public key fingerprint matches: 1F:7A:9C:...:B2
- Offline cache loaded: 6,000 records
- CRL updated <30 min ago
- Test scans: 5 pass, 2 deny scenarios

Signage templates (content cues):
- “Tap NFC or Scan QR” with icons; lane name; role badges permitted; ADA symbol; “Have your badge visible”
- Color-coded headers matching role colors

SOPs:
- Lost badge process flowchart
- Escort logging procedure
- End-of-day device reconciliation and charging

Vendor contacts:
- Access Control Vendor Onsite Lead: +1-555-012-8844
- Registration System Support: +1-555-019-2244
- Venue Security Control: radio channel 3 / landline +1-555-014-9900

---

## Change Control

- Any change to credential matrix or zones requires:
  - Written approval from Access Control Lead and Security Lead
  - Policy JSON increment (minor version)
  - Device policy push and spot verification at 2 checkpoints
  - Communication to Supervisors via daily briefing notes

---

## Quick Start (Day 0 Cheat Sheet)

- Power on and sign in handhelds; verify policy version and CRL timestamp.
- Perform 5 test scans per lane (ATT, SPK, EXH, STF, DENY).
- Open lanes: 1 ADA, 2 General, 1 VIP where applicable.
- Brief staff: denial reasons, reroute paths to CP1, radio call signs.
- Monitor throughput dashboard; add lanes if queue >8 minutes.
- Log incidents and reprints; debrief at 17:30.