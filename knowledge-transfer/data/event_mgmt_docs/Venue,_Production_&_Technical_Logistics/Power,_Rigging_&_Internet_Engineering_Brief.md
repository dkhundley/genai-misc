# Power, Rigging & Internet Engineering Brief
Venue, Production & Technical Logistics

Document purpose: This brief defines electrical distribution, rigging loads/points, and network architecture for attendee and production needs. It provides load calculations, network topology, implementation steps, responsibilities, and safety/compliance requirements so a cross-functional team can execute without additional context.

Event context (example): 3‑day technology conference, 1,500 attendees, in-person. Spaces include a General Session (GS) ballroom, 8 breakout rooms, 1 registration lobby, and an expo with 20 exhibitor booths.

Dates (example): 
- Load-in: Tue–Wed (2 days)
- Event: Thu–Sat (3 days)
- Strike: Sun (1 day)

Venue (example): Downtown Convention Center  
- GS Ballroom: 200 ft x 120 ft x 30 ft clear height, floor loading 350 psf, steel grid above ceiling; house company switches on stage left/right and upstage.  
- Breakouts: 8 rooms, approx. 50 ft x 40 ft each, ceiling height 18–22 ft, limited rigging points in 4 rooms.  
- IT MPOE and MDF in Level 1 closet; fiber runs to Level 2 IDFs.

Contacts (example):
- Technical Director (TD): td@agency.com, +1‑555‑0100
- Head Electrician (HE): electrics@venue.com, +1‑555‑0101
- Head Rigger (HR): rigging@venue.com, +1‑555‑0102
- Network Lead (NL): netops@agency.com, +1‑555‑0103
- Safety Officer (SO): safety@agency.com, +1‑555‑0104

---

## Overview

Scope:
- Engineer and deploy safe, code-compliant power distribution for lighting, video, audio, broadcast, back-of-house, and exhibitor services.
- Engineer rigging points, loads, and hoist plan for GS truss/LED wall/PA and necessary breakouts.
- Engineer attendee/production network: WAN, LAN, Wi‑Fi, security, QoS, and monitoring.

Success criteria:
- Zero electrical or rigging safety incidents; all permits and sign‑offs complete.
- Measurable power capacity margin ≥ 20% on each major feeder under show conditions.
- Rigging factor of safety compliant with venue and ANSI/ESTA guidelines; point loads within structural allowances.
- Attendee Wi‑Fi median throughput ≥ 15 Mbps down/5 Mbps up; authentication success rate ≥ 99%; production network jitter < 15 ms for live streams.

---

## Key Details

- Total expected maximum simultaneous users on Wi‑Fi: ~900 devices (60% concurrency of 1,500 attendees), plus production (~120 devices) and exhibitors (~80 devices).
- Peak simultaneous broadcast streams: 2 x 1080p60 main feeds, 1 x 4K archive capture, 8 x breakout capture (1080p30).
- Rigged elements: 100 ft x 50 ft FOH lighting truss; 10 m x 4 m 2.6 mm LED wall; L/R line arrays; center cluster; 2 x delay trusses; drape; scenic headers.

---

## Power Engineering

Standards and codes:
- NEC 2023, Articles 520/530 (theaters/motion picture), 250 (grounding), 590 (temporary power).
- OSHA 29 CFR 1926 Subpart K; NFPA 70E.
- GFCI per NEC for all 120 V receptacles accessible to non-qualified personnel.
- All distro listed for temporary use; cam-lok connectors with locking covers.

House power and primary distribution (GS):
- House company switches:
  - SL 400 A, 120/208 V 3‑phase wye, cam‑lok
  - SR 400 A, 120/208 V 3‑phase wye, cam‑lok
  - Upstage 200 A, 120/208 V 3‑phase wye, cam‑lok
- Portable generator (contingency): 150 kW trailer‑mount, 120/208 V 3‑phase wye, 5‑wire with neutral bonding switch; 25 ft from egress, bonded to venue ground when paralleled; only if utility power compromised.

Connected load summary (GS, example):
- Lighting: 120 LED fixtures (avg 200 W) + 16 movers (470 W) + control/DMX (500 W)  
  Estimated average: (120 x 0.2) + (16 x 0.47) + 0.5 ≈ 24 + 7.5 + 0.5 = 32 kW  
  Peak with effects: 40 kW (diversity 0.8 applied to nameplate)
- Video/LED wall: 10 m x 4 m @ 2.6 mm; area = 40 m²  
  Avg: 300 W/m² → 12 kW; Peak: 800 W/m² → 32 kW (limit via brightness cap to 60% → peak ~19 kW)
- Audio: Amplifiers, consoles, RF racks: avg 6 kW; peak 12 kW (sub hits). Power factor corrected amps.
- Broadcast/control/IT (GS): 5 kW avg; 8 kW peak.
- Scenic/drape motors (active): negligible steady load; 16 x 1‑ton hoists @ 7 A each during movement only (480 V preferred; else 208 V via phase couplers).
- HVAC: House system, not on show power.

GS feeder allocation (recommended):
- Lighting: SL 400 A 120/208 V 3φ → 200 A average draw (32–40 kW); 4/0 Cu per phase; double neutral 2 x 4/0 Cu for harmonics.
- Video: SR 200 A 120/208 V 3φ → 60–95 A average (12–19 kW); 2/0 Cu; double neutral recommended.
- Audio: Upstage 200 A 120/208 V 3φ → 30–60 A avg (6–12 kW); 2/0 Cu; isolated ground if available; separate from lighting/video to minimize noise.
- Control/IT: Tap from video or dedicated 100 A 3φ with clean ground; avoid sharing with dimming/LED wall PSUs.

Breakouts power:
- Each room: 100 A 3φ company switch or distro; typical connected load 8–12 kW per room:
  - Lighting: 4–6 kW (LED)
  - Video: 2–3 kW (projector/LED wall)
  - Audio: 1–2 kW
  - IT: 0.5–1 kW
- Expo: 20 booths @ 5 A each (120 V) = 12 kW + 30% diversity = 9 kW avg. Provide 4 x 20 A quad boxes per 10 ft aisle segment; GFCI where public accessible.

Distribution equipment (typical):
- 3 x 400 A disconnects with cam‑lok tails, 65 kAIC, integral metering.
- 4 x 200 A distros with L21‑30 and Edison duplexes; breakers labeled by zone.
- 12 x 100 A satellite distros for truss drops, backstage, FOH.
- 40 x 20 A circuits (120 V) for backline, scenic, client devices.
- Power factor/capacitor banks not required; LED drivers are PFC-rated (>0.9 PF).

Feeder and cabling:
- Feeder for 400 A: 4/0 Cu per phase, 4/0 Cu ground, doubled neutral (2 x 4/0 Cu).
- Feeder for 200 A: 2/0 Cu per phase and neutral; consider doubled neutral for video/LED.
- SOOW 6/4 and 12/3 cables for branch circuits; all runs secured, matted in public areas.

Grounding and bonding:
- Use 120/208 V 3φ wye with solidly grounded neutral. Bond all distros to system ground. If generator used, establish single point neutral bond (generator or transfer switch) per NEC; install two 8 ft ground rods bonded to venue grounding electrode system.

Protection and metering:
- Clamp meters at each company switch; log current per leg during rehearsals and at show open.
- Aim for ≤ 80% of breaker ratings continuous (NEC 125% rule for continuous loads).

Power management:
- Limit LED wall brightness to ≤ 60% to cap peak draw; use wall PSU monitoring.
- Sequence power-up: 1) Distros, 2) Audio racks, 3) Lighting, 4) Video/LED wall, 5) IT/broadcast. Reverse for power-down.

Acceptance testing:
- IR thermometer spot check on cam‑loks and lugs at 30 min into show; ΔT ≤ 25°F over ambient.
- GFCI trip test on sample outlets; record in log.
- Earth continuity test from distros to main bond: < 1 Ω.

---

## Rigging Engineering

Standards and codes:
- ANSI/ESTA E1.6 (Powered Hoist Systems), E1.21 (Temporary Structures), E1.22 (Fire Safety Curtain areas), E1.43 (Performer Flying—if applicable).
- OSHA 1926 Subpart R; venue-specific rigging rules.  
- All hardware WLL with minimum 8:1 design factor for life safety (typical for slings/steel); hoists per manufacturer.

Structural assumptions (venue-provided):
- Ballroom steel grid with uniform allowable load 4,000 lb per beam panel and point load max 2,000 lb at designated nodes; spacing 20 ft x 20 ft; no more than 6,000 lb within any 20 ft square without engineering review. Seismic Z = moderate.

Truss and points overview (GS):
- FOH Truss: 100 ft span of 20.5 in box truss, centerline ~60 ft from stage edge, 6 pick points at ~20 ft spacing.
- Stage Truss: 80 ft span upstage, 4 pick points.
- LED Wall Support: 10 m x 4 m wall hung from dedicated 40 ft truss, 4 pick points.
- Audio L/R Arrays: 2 x line array hangs, each with 1 pick point + 1 safety (bridle if needed).
- Delay Trusses: 2 x 30 ft truss, each with 2 pick points.
- Drape and Scenic Headers: distributed loads off stage truss.

Estimated weights:
- FOH Truss: Truss (4.5 lb/ft x 100 ft x 2 chords) ~900 lb; fixtures/cables/di’s ~1,300 lb; total ≈ 2,200 lb + 10% contingency = 2,420 lb → per point (6) ≈ 403 lb.
- Stage Truss: Truss ~450 lb; lights ~900 lb; soft goods 200 lb; total ≈ 1,650 lb + 10% = 1,815 lb → per point (4) ≈ 454 lb.
- LED Wall: Panels 80 x 12 kg ≈ 960 kg = 2,116 lb; frame/rigging 300 lb; truss 300 lb; cables 100 lb; total ≈ 2,816 lb + 10% = 3,098 lb → per point (4) ≈ 775 lb.
- Audio Arrays: Each hang 12 boxes @ 70 lb = 840 lb + frame 120 lb + cabling 40 lb = 1,000 lb + 10% = 1,100 lb → per point ≈ 1,100 lb (use 1‑ton hoist).
- Delay Trusses: Each 30 ft with 12 fixtures, total per truss ≈ 600 lb → per point (2) ≈ 300 lb.

Hoists and hardware:
- 16 x 1‑ton (2,000 lb WLL) CM Lodestar D8+ hoists for primary picks.  
- 8 x 1/2‑ton hoists for delay and drape as needed.  
- Slings: 1/2 in GAC with appropriate thimbles; WLL ≥ 5,600 lb.  
- Shackles: 3/4 in alloy, WLL 4.75 ton; safety factors per manufacturer.  
- Bridle angles to maintain leg angle ≥ 60° to minimize tension. Include beam clamps where direct attachment allowed.

Point load verification:
- Maximum point load calculated = ~1,100 lb (audio L/R). Under 2,000 lb node limit.  
- Sum within any 20 ft square: e.g., LED wall 2 points + stage truss 2 points ≈ 2 x 775 + 2 x 454 = 2,458 lb < 6,000 lb limit.  
- Provide stamped verification if venue requires for combined loads; TD to submit final rigging plot to venue structural engineer.

Deflection:
- Keep truss midspan deflection under L/240 under full load. For 100 ft FOH, evaluate with manufacturer tables; add midspan point if needed.

Clearances and egress:
- Maintain 18 in clearance from sprinklers; 3 ft around exit signage; do not block HVAC diffusers if possible.  
- Minimum 6 ft 8 in head clearance above audience areas under flown truss.

Hoist power and control:
- 208 V 3φ hoist distro; calculations: 16 hoists x 7 A running = 112 A, non‑coincident with show load; provide dedicated 100–125 A 3φ service.  
- Motion only during load-in/focus unless TD authorizes show moves.

Inspection and sign‑off:
- Pre‑rig inspection with HR; daily visual check before doors.  
- Tag and log each point with load and inspection status.  
- Rescue plan: reach poles, ladders, or lift access; define fall arrest anchorage for riggers (5,000 lb rated).

---

## Internet & Network Engineering

Objectives:
- High-density attendee Wi‑Fi with fair-sharing and low latency.
- Isolated, high-availability production network with QoS for streaming/VoIP.
- Exhibitor access with rate limits and VLAN isolation.
- Full monitoring/telemetry and rapid incident response.

WAN:
- Primary DIA: 1 Gbps symmetric fiber, /29 public block, handoff RJ45 10/100/1000Base‑T or SFP.  
- Secondary: 500 Mbps cable or 5G enterprise gateway with static IP; BGP preferred; otherwise health‑checked failover.  
- Allocation targets (policy, adjustable):
  - Production/Broadcast: 300 Mbps guaranteed
  - Attendee Wi‑Fi: up to 500 Mbps aggregate
  - Exhibitors: 100 Mbps aggregate
  - Overhead/Management: 50 Mbps

Core topology:
- Core stack: 2 x 10G‑capable L3 switches in stack (MLAG/VSS), located in NOC near MDF.  
- Firewall: HA pair, capable ≥ 2 Gbps throughput with IPS off, ≥ 1.5 Gbps with basic IPS.  
- Distribution: 4 x 48‑port PoE+ (or 802.3bt for higher power APs), 10G uplinks to core.  
- IDFs: FOH, Stage Left, Stage Right, Expo; single‑mode fiber to core (2 x 10G per IDF).

VLANs and addressing (RFC1918):
- VLAN 10 Production Wired: 10.10.10.0/23, DHCP 10.10.10.50–10.10.11.200
- VLAN 20 Production Wi‑Fi: 10.10.20.0/23
- VLAN 30 Streaming Encoders: 10.10.30.0/24 (static IPs)
- VLAN 40 VoIP/Comms: 10.10.40.0/24, LLDP‑MED, DSCP 46 EF
- VLAN 50 Registration/Badge: 10.10.50.0/24
- VLAN 60 Exhibitors: 10.10.60.0/22
- VLAN 70 Attendee Wi‑Fi: 10.10.70.0/20 (supports ~4,000 leases)
- VLAN 99 Management/OOB: 10.10.99.0/24 (controller, switches, APs)
- Gateway IPs assigned on core; ACLs isolate VLANs (deny inter‑VLAN except specific allow rules).

Wi‑Fi design:
- Standard: Wi‑Fi 6/6E where available; prefer 5 GHz; optionally enable 6 GHz SSID for capable devices (production-only).  
- Attendee SSID: Open with captive portal; DHCP rate‑limit to 8–12 hour leases; per‑client limits 10 Mbps down/5 Mbps up; 5 GHz only, 2.4 GHz disabled except in registration.  
- Production SSID: WPA2‑Enterprise (RADIUS) or WPA3‑Enterprise; 5 GHz + 6 GHz; per‑client limits 50 Mbps with QoS exceptions.  
- Exhibitor SSID: WPA2‑PSK unique per exhibitor (PSK‑per‑user if supported), 5 GHz; per‑client limit 20 Mbps; client isolation on.  
- RF plan (GS):  
  - AP density: 20 APs ceiling‑mounted over GS (approx. 1 AP per 75 seats), directional antennas where possible; 4–6 APs per large breakout; 2–3 APs per small breakout; 6 APs in expo; 4 APs in lobby/registration. Total ~56–62 APs.  
  - Channel plan: 5 GHz: 8 non‑overlapping 40 MHz channels (or 20 MHz if interference): 36/40/44/48/149/153/157/161; disable DFS if local radar history is problematic. 6 GHz: 80 MHz channels for production only.  
  - Power: Start EIRP at 8–12 dBm in GS to improve spatial reuse; increase only if coverage gaps observed.  
  - Features: 802.11k/v enabled; 802.11r fast roam on production; band‑steering to 5/6 GHz; client load‑balancing on.

QoS:
- Mark streaming encoder traffic DSCP 46 (EF) inbound at switch ports; guarantee min 200 Mbps on WAN with priority queue.  
- VoIP DSCP 46; Comms/Intercom DSCP 46 or 34 as vendor requires.  
- De‑prioritize large updates/cloud sync on attendee VLANs (DSCP 0).

Security:
- NAC/RADIUS for production devices; MAC‑auth bypass for encoders as needed.  
- ACLs: Attendee VLAN to Internet only; Exhibitors to Internet plus their own public IPs; Production VLANs to specific services (SRT/RTMP endpoints, cloud control).  
- mDNS constrained to breakout presentation devices via gateway proxy.  
- WIPS monitor only; avoid de‑auth.  
- Logging: Netflow/sFlow, syslog to central server; time synced via NTP.

DHCP/DNS:
- Redundant DHCP for attendee and exhibitor VLANs (split scopes); reservations for production.  
- Local DNS cache/forwarders on firewall/core.

Monitoring and tests:
- NMS (e.g., PRTG/LogicMonitor) for switch/AP health; CWAP survey during rehearsals; iPerf3 servers on production VLAN.  
- Synthetic tests: HTTP, DNS, captive portal, RADIUS auth; record pass/fail per room.  
- Event dashboards: WAN utilization, AP client counts, top talkers, retransmission rates.

Port map (examples):
- Encoders (Stage): VLAN 30, static IP 10.10.30.11–.20
- Vision control (GS): VLAN 10, DHCP reservations
- Registration PCs/Printers: VLAN 50
- Exhibitor uplinks (if any): VLAN 60 with private SSIDs

---

## Responsibilities

- Technical Director (TD): Owns final system design, schedule, and coordination; approves changes; leads daily production meetings.
- Head Electrician (HE): Leads all power tie‑ins, distro layout, and load verification; maintains power logs; ensures NEC compliance.
- Head Rigger (HR): Produces rigging plot, supervises point installation, hoist operation, inspections, and daily sign‑offs.
- Network Lead (NL): Designs/implements WAN/LAN/Wi‑Fi; manages security/QoS/monitoring; runs validation tests; provides help desk staffing.
- Safety Officer (SO): Conducts JHA, oversees PPE, lockout/tagout, fall protection, and emergency response plans.
- Venue Representative: Confirms house capabilities, approves rigging points, coordinates permits and after‑hours access.
- Stage Manager: Sequencing of show power-up/down, ensures no hoist motion during public occupancy without authorization.
- Vendors (Lighting, Video, Audio, LED, Staging): Provide updated equipment lists with power draws and weights; adhere to distro and rigging assignments.

---

## Dependencies

- Venue documentation: As‑built electrical one‑line diagrams; rigging plot with load ratings; IT demarc details and fiber path maps.
- Approvals: Venue structural sign‑off on rigging; electrical tie‑in authorization; internet order confirmation and demarc test.
- Equipment lead times:  
  - DIA circuit: 30–45 days (order ASAP)  
  - Rental gear (hoists/truss/LED/APs): 2–3 weeks  
  - Lift access and overnight storage permissions
- Safety: JHA and Method Statement approved prior to load‑in; MSDS for any hazers/fluids; permitting if generator used.

---

## Implementation Steps and Timeline

T‑30 to T‑14 days:
- Finalize floor plan, rigging plot, and power one‑line; submit to venue for approval.
- Confirm WAN order and IP allocation; schedule ISP turn‑up and test.
- Lock equipment lists; update load and weight calculations with actual SKUs.
- Create SSIDs, VLANs, ACLs in staging; generate QR codes for production SSID.

T‑7 days:
- Pre‑production tech check (remote): validate configs on lab switches/APs/firewalls.  
- Safety meeting invites; circulate JHA and LOTO procedures.  
- Print labels for distros, breakers, cables, APs, and switch ports.

Load‑in Day 1:
- Rigging: Install points, hang truss/hoists; no loads applied until inspection.  
- Power: HE verifies company switches; land feeders; test voltages, phase rotation, and ground continuity; label panels.  
- Network: Deploy core, firewalls, and IDF uplinks; verify WAN; bring up management VLAN.

Load‑in Day 2:
- Fly truss and set trim; hang fixtures, LED wall, arrays; HR inspection and sign‑off.  
- Power: Run branch circuits; balance phases to within ±10%; metering baseline.  
- Network: Install APs; perform quick RF survey; validate SSIDs; captive portal test; RADIUS auth test.  
- Technical rehearsals: Power peak observation; update power log; Wi‑Fi load tests with 100 test clients.

Event Days:
- Daily pre‑flight: power temperature checks, rigging visual inspection, NOC health review.  
- Show operations: NOC staffed; incident response within 5 min; track KPIs.  
- Post‑show: controlled power‑down; save configs and logs.

Strike:
- Power down in reverse sequence; lockout; remove feeders; coil and inventory.  
- Lower truss; de‑rig; inspection for damage; return venue to original condition.  
- Network: Archive configs, export monitoring graphs, finalize incident report.

---

## Safety and Compliance

- PPE: Hard hats, safety boots, high‑viz; fall arrest for work at height; lockout/tagout for any energized work (qualified personnel only).
- Egress: Maintain 6 ft clear around exits; no cable crossings at doorways without ADA ramps; all audience-area cables matted/taped.
- Fire safety: Keep 3A:40B:C extinguishers at dimmer/LED power racks and NOC.
- Weather (if loading dock exposed): Wind limits for lift operations per manufacturer.

---

## References and Templates

References:
- NEC 2023 Articles 250, 520, 530, 590
- ANSI/ESTA E1.6‑1/2/3, E1.21, E1.43
- OSHA 29 CFR 1926 Subparts K and R
- IEEE 802.11ax/802.11be guidelines for high‑density deployments

Templates/Examples (adapt as needed):
- Power one‑line description:
  - Utility → Main Service → Company Switch SL 400 A → 400 A Distro L1 → 200 A Distro L1A (FOH) + 100 A Satellites
  - Utility → Company Switch SR 200 A → 200 A Distro V1 (LED Wall) + 100 A Control
  - Utility → Company Switch Upstage 200 A → 200 A Distro A1 (Audio)
- Labeling convention:
  - Feeders: FEED‑[Location]‑[Amps] (e.g., FEED‑SL‑400A)
  - Circuits: [Distro]-[Phase]-[Breaker]-[Device] (e.g., L1A‑B‑20‑LED PSU Row 1)
  - Rigging points: P‑[GridCoord]‑[Load lb] (e.g., P‑C3‑775)
  - Switch ports: [Closet]-[Switch]-[Port]-[VLAN] (e.g., IDF‑SL‑S1‑Gi1/0/12‑V30)
- SSID plan:
  - SSID: Event‑Attendee (VLAN 70, rate limit 10/5 Mbps, portal)
  - SSID: Event‑Production (VLAN 20, WPA2‑E, bypass portal, QoS)
  - SSID: Event‑Exhibitor (VLAN 60, PSK per booth, client isolation)
- Power log (sample):
  - Time / SL A‑B‑C Amps / SR A‑B‑C Amps / Upstage A‑B‑C Amps / LED Brightness % / Notes
- Rigging inspection checklist:
  - Hardware WLL verified; hoist chains free of twists; slings protected at edges; cotter pins installed; safety steels on arrays; tag lines present.

---

## Notes and Assumptions

- All wattage and weight figures are conservative estimates; update with as‑shipped equipment sheets before final sign‑off.
- Neutral conductors for LED/video are doubled due to harmonic currents. Monitor neutral temperatures during rehearsals.
- If venue prohibits certain attachment methods, convert applicable picks to bridles to compliant beams.
- If DFS channels are stable per site survey, enable to increase 5 GHz channel availability.

---

## Change Management

- Any change affecting loads, points, or VLAN/QoS must be submitted to TD and documented in the Change Log with: description, risk, rollback plan, and approvals (TD + HE/HR/NL as applicable).
- Emergency deviations allowed only to resolve an active incident; log within 1 hour post‑incident.

---

## Deliverables

- Final power one‑line with panel schedules and breaker assignments.
- Final rigging plot with point loads and hoist list; venue approval letter.
- Final network diagram with VLANs, IP plan, SSIDs, ACLs, QoS policies.
- Daily safety checklists, power logs, and NOC health reports.
- Post‑event report with metrics, incidents, and recommendations.