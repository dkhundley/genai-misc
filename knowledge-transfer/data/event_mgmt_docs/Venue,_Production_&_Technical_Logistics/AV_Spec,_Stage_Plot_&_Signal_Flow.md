# AV Spec, Stage Plot & Signal Flow
Document Type: Technical Rider, Stage Plot, and Signal Flow Diagram

## Overview
This document defines the complete audiovisual specification, stage layout, and signal flow for a mid-sized general session with a keynote, panel discussion, and a 5-piece house band. It is designed so any qualified venue or production team can execute consistently across venues.

- Audience: 500–800 attendees
- Room: Ballroom, approx. 120' x 80', ceiling 20'+
- Stage: 40' W x 24' D x 2' H, with 12' upstage drape line and two 8' ramps (SL/SR)
- Show Profile:
  - Keynote presenters (wireless handhelds and lavs)
  - Panel: up to 4 speakers at a 16' table
  - Band: 5-piece (drums, bass, guitar, keys, lead vocal)
  - IMAG and playback
  - Lighting for camera, stage wash, accents

Deliverables:
- Consistent gear spec and patching for audio, video, and lighting
- Stage plot and input/output lists
- Patch and signal flow diagrams
- Crew responsibilities, schedule, and dependencies

---

## Key Details

### 1) Audio Specification

- PA System
  - Mains: d&b V-Series (6x V8 per side), flown, 10–12° splay per array
  - Subs: 4x d&b V-SUB ground-stacked center cluster
  - Front fills: 4x d&b E8 across stage lip
  - System DSP: Lake LM44 or equivalent, system tuned to target of 95 dBA LEQ 15, -3 dB near/far

- Consoles & I/O
  - FOH: Yamaha CL5 (64 mono + 8 stereo) on Dante
  - Monitors: Yamaha QL5 side-stage (or CL3 acceptable) on Dante
  - Stageboxes: 2x Rio3224-D2 (32 in / 16 out each), located USL and USR
  - Network: Primary/secondary Dante with managed switches (Cisco SG350 or equivalent), QoS enabled

- Microphones & DIs (total inputs ≈ 34)
  - Presenters:
    - 4x Shure Axient Digital ADX1 lavs (DPA 4066 or 6066 headsets) + spare
    - 4x Shure Axient Digital ADX2 handheld (KSM9 or Beta58) + spare
  - Panel:
    - 4x Wired gooseneck table mics (Shure MX418D/C) with inline HPFs
  - Band:
    - Drums: Kick (Beta52), Snare Top/Bottom (SM57, e604), HH (KM184), Rack (e904), Floor (e904), OH L/R (KM184 pair)
    - Bass: DI (Radial J48), Mic (RE20 optional)
    - Guitar: SM57 on cab, optional second mic (e906)
    - Keys: Stereo DI (Radial ProD2)
    - Tracks: Stereo DI (Radial ProD2)
    - Lead Vox: Shure Beta58A wired
    - Backing Vox x2: Shure SM58 wired
  - Audience/Room:
    - 2x Audience mics (AKG C414 or similar) for recording/stream Q&A

- Wireless/RF
  - Total RF: up to 10 channels (8 active + 2 spares)
  - In-ears: 2x Shure PSM900 stereo IEM
  - Coordination: Use local scan + pre-coordination (RF Venue or Shure WWB). Keep >500 kHz spacing between adjacent carriers; intermod-safe set.
  - Antennas: 1x helical for RX diversity; 1x helical for IEM TX; mount on stands DSL/DSR, line-of-sight, >10’ from PA horns.

- Monitoring
  - Wedges: 4x d&b M4 or JBL SRX, mixes 1–4
  - IEM: 2 stereo mixes (Lead Vox, MD/Keys)
  - Sidefills optional, dependent on room

- Playback/Comms (Audio)
  - Playback Mac with QLab/PlaybackPro, 2-channel output (3.5mm or USB interface to DI)
  - Stage Announce (SA) mic at SM position
  - Clear-Com 2-channel analog: Ch A (Audio/Lighting), Ch B (Video/Stage)

- Processing & Recording
  - FOH inserts: Waves SoundGrid optional
  - 2-track and 32-track Dante multitrack record to DAW (Reaper), 48kHz/24-bit
  - Program audio to video switcher via Dante (Dante AVIO AES3 or Attero Tech unDIO)

- Power (Audio)
  - 60A 120/208V 3P for audio racks and PA amps (separate from lighting/video where feasible)
  - Clean grounding; isolated technical power if available

---

### 2) Video Specification

- Screens & Projection
  - Dual 16:9 fast-fold screens, 16' x 9', left/right of stage
  - Projectors: 2x 10,000–12,000 lumen laser (Panasonic RZ970 class), 1.6–2.1 lens, flown or rear-projection if depth allows
  - Confidence monitors: 2x 55" downstage at ±30° to lectern; 1x 32" DSM for band MD

- Cameras & Switching
  - Switcher: Blackmagic ATEM 2 M/E Production Studio 4K (or equivalent)
  - Cameras: 
    - Cam 1: Manned, center rear, 75–200mm
    - Cam 2: Manned, house left, 24–105mm
    - Cam 3: PTZ on rear truss for wide safety
  - Router/DA: Blackmagic Smart Videohub 20x20 for routing/iso
  - Program feed: 1080p59.94, SDI 3G, to projectors and recorders
  - ISO recorders: 2x HyperDeck Studio HD for PGM and clean feed
  - Graphics: Playback Mac (Key/Fill if lower-thirds needed via UltraStudio/DeckLink)
  - Scan converters/DS: Decimator MD-HX x2

- Signal Format
  - SDI backbone (12G where possible; minimum 3G)
  - HDMI converted to SDI at source
  - Fiber SDI runs if FOH >150’

- Program Audio
  - From FOH via Dante > AES de-embed to switcher or via analog/AES embedder
  - Return tally/comms to cameras as available

- Power (Video)
  - 100A 120/208V 3P for projectors, switcher, monitors, routers

---

### 3) Lighting Specification

- Console
  - MA3 Compact or onPC Command Wing + NP; backup showfile on USB

- Fixtures (typical)
  - 12x LED wash (Chauvet Rogue R2 Wash or similar)
  - 8x LED profiles with shutters (ETC Lustr Series 2) for key light zones
  - 8x Moving spots (Robe Esprite or MegaPointe)
  - 8x LED PAR uplights for backdrop/set
  - 2x 2-lite audience blinders (camera-safe)
  - 1x Hazer (DF-50 or equivalent), venue permitting

- Truss/Rigging
  - 50' FOH truss (key/fill), 50' upstage truss (backlight/effects), 2x 20' wing truss (side wash)
  - 8–10x one-ton points, per venue structure and plot
  - All rigging by certified rigger; load calcs available on request

- DMX & Power
  - At least 2 universes via Art-Net/sACN to DMX nodes
  - Universe 1: Key/profile + movers
  - Universe 2: Wash, uplights, blinders, hazer
  - Distro: 200A 3P for lighting, powerCON TRUE1 where possible

- Camera Lighting Targets
  - Presenters: 850–1,000 lux at 5600K CRI/TLCI >90, even ±10%
  - Panel table: 700–800 lux at 5600K
  - Band: 500–700 lux, color accents audience-safe

---

## Stage Plot

Top view (not to scale). DS = Downstage, US = Upstage, SL/SR = Stage Left/Right.

- Stage: 40' W x 24' D
- Lectern DSL, Panel table USC, Band USR/USC

```
      UPSTAGE DRAPE LINE
 ----------------------------------------------------------
 |                         | PANEL TABLE (16')           |
 |   KEYS (MD)             |  4x Gooseneck Mics          |
 |  [Keys L/R DI]          |                             |
 |      [IEM]              |                             |
 |                         |                             |
 |  GTR AMP    BASS AMP    |           DRUMS             |
 |  [SM57]     [RE20/DI]   |    [Kick/Snare/Toms/OH]     |
 |                         |                             |
 |-------------------------------------------------------- 
 |                                                           
 |                 OPEN STAGE / WALKWAY                   |
 |                                                           
 |  LECTERN (DSL)          DS CENTER               DSM 55" (SR) 
 |  [HH/Lav RX nearby]     [Mark X]                [Foldback]
 |
 | FF1    FF2             FF3     FF4
 ---------------------------------------------------------- 
         AUDIENCE
```

Monitor placements:
- Wedge 1: Lectern
- Wedge 2: Panel (near DS center)
- Wedge 3: Guitar/Bass
- Wedge 4: Drums
- IEM: Keys (MD), Lead Vox

Camera positions:
- Cam 1: Center rear
- Cam 2: House left
- PTZ: Rear truss center

Screens/projection: L/R of stage

---

## Audio Input List and Patch

Channel plan (Dante/console channels 1–48). Stageboxes: Rio A (USL), Rio B (USR).

| Ch | Source                  | Mic/DI                 | Stand       | Box | Notes                       |
|----|-------------------------|------------------------|-------------|-----|-----------------------------|
| 1  | Kick In                 | Beta52                 | Short boom  | B   | Gate                         |
| 2  | Snare Top               | SM57                   | Short boom  | B   |                              |
| 3  | Snare Bottom            | e604                   | Clip        | B   | Reverse polarity             |
| 4  | Hi-Hat                  | KM184                  | Boom        | B   |                              |
| 5  | Rack Tom                | e904                   | Clip        | B   | Gate                         |
| 6  | Floor Tom               | e904                   | Clip        | B   | Gate                         |
| 7  | OH L                    | KM184                  | Tall boom   | B   | XY/ORTF as space allows      |
| 8  | OH R                    | KM184                  | Tall boom   | B   |                              |
| 9  | Bass DI                 | Radial J48             | DI          | B   |                              |
| 10 | Bass Mic                | RE20                   | Boom        | B   | Optional                     |
| 11 | Guitar Amp              | SM57                   | Boom        | A   |                              |
| 12 | Keys L                  | Radial ProD2           | DI          | A   |                              |
| 13 | Keys R                  | Radial ProD2           | DI          | A   |                              |
| 14 | Tracks L                | Radial ProD2           | DI          | A   | From Playback rig            |
| 15 | Tracks R                | Radial ProD2           | DI          | A   |                              |
| 16 | Lead Vox                | Beta58A wired          | Tall boom   | A   | IEM send priority            |
| 17 | BGV 1                   | SM58                    | Tall boom   | A   |                              |
| 18 | BGV 2                   | SM58                    | Tall boom   | A   |                              |
| 19 | Lectern                 | Shure MX418D           | Desk        | A   | HPF 120 Hz                   |
| 20 | Present Lav 1 (RF)      | ADX1 + DPA 4066        | Bodypack    | A   | RF ch 1                      |
| 21 | Present Lav 2 (RF)      | ADX1 + DPA 4066        | Bodypack    | A   | RF ch 2                      |
| 22 | HH 1 (RF)               | ADX2/KSM9              | Handheld    | A   | RF ch 3                      |
| 23 | HH 2 (RF)               | ADX2/KSM9              | Handheld    | A   | RF ch 4                      |
| 24 | Panel Mic 1             | Shure MX418D           | Table       | A   |                             |
| 25 | Panel Mic 2             | Shure MX418D           | Table       | A   |                             |
| 26 | Panel Mic 3             | Shure MX418D           | Table       | A   |                             |
| 27 | Panel Mic 4             | Shure MX418D           | Table       | A   |                             |
| 28 | Audience Mic L          | C414                    | Tall boom   | FOH | For stream/Q&A               |
| 29 | Audience Mic R          | C414                    | Tall boom   | FOH |                              |
| 30 | Playback L (walk-in)    | QLab Mac               | DI          | A   |                              |
| 31 | Playback R (walk-in)    | QLab Mac               | DI          | A   |                              |
| 32 | SA Mic (Stage Announce) | SM58                   | Tall boom   | A   | SM control                   |

Spare RF/Utility:
- Ch 33: Spare HH (RF)
- Ch 34: Spare Lav (RF)

Output patch (FOH/Mon):
- L/R/Sub matrix to system DSP (Matrix 1 L, 2 R, 3 Sub)
- Matrix 4: Front fills
- Matrix 5–6: Record/Stream (post-mix, -18 dBFS target)
- Mix 1: Wedge Lectern
- Mix 2: Wedge Panel
- Mix 3: Wedge GTR/Bass
- Mix 4: Wedge Drums
- Mix 5–6: IEM Lead Vox (stereo)
- Mix 7–8: IEM Keys/MD (stereo)
- Talkback from Mon engineer to Mixes 5–8

Labeling & Color Code:
- Drums (Red), Bass (Blue), GTR (Green), Keys/Tracks (Yellow), Vox (Purple), Presenters/Panel (Orange), Playback/SA (White)

---

## Video Patch

Inputs to Switcher:
- SDI 1: Cam 1 (Rear)
- SDI 2: Cam 2 (HL)
- SDI 3: PTZ (Wide)
- SDI 4: Graphics 1 (Playback Mac via DeckLink/HDMI>SDI)
- SDI 5: Graphics 2 (Backup laptop via Decimator)
- SDI 6: FOH PGM Audio Embed (from Dante > AES > Embedder)

Outputs:
- PGM Out 1: Screen Left projector
- PGM Out 2: Screen Right projector
- AUX 1: Confidence monitors (Slides only)
- AUX 2: ISO Clean Feed (no lower-thirds)
- AUX 3: Downstage foldback 32" (Timer/Next slide)
- SDI to HyperDeck 1: Program record
- SDI to HyperDeck 2: Clean ISO record

Comms/Tally:
- Clear-Com belt packs at Cam 1/2; PTZ on director panel
- Tally via ATEM to manned cameras if supported

---

## Lighting Patch (Example)

Universe 1 (001–256):
- 001–048: ETC Lustr Profiles (Zones 1–8)
- 101–148: Robe Spots (1–8)
Universe 2 (001–256):
- 001–096: LED Wash (1–12)
- 101–116: Uplights (1–8)
- 151–158: Blinders (1–2)
- 201–205: Hazer/House practicals via relays

Base Cues:
- LX 1: Preset (walk-in)
- LX 5: Keynote (Lectern bright, audience dim)
- LX 10: Panel (table wash, soft backlight)
- LX 20: Band (color looks, movers slow)
- LX 99: House to full

---

## Signal Flow Diagrams (ASCII)

Audio (high level):
```
[Stage Mics/DI] 
     | XLR
[Rio A (USL)]   [Rio B (USR)]
     | Dante Primary/Secondary over CAT5e (VLAN/QoS)
        --> [FOH CL5] --(Matrices)--> [System DSP] --> [Amps] --> [PA]
                       \--(Dante)--> [DAW Recorder]
                       \--(Dante/AES)--> [Video Switcher/Embedder]

[FOH to MON via Dante] --> [Monitor QL5] --> [Wedges/IEM TX]
[T/B Mon] <--> [IEM Mixes]
```

Video:
```
[Cameras 1/2 SDI]   [PTZ SDI]    [Graphics SDI]
       \               |             /
               [ATEM Switcher/Rtr]
             /       |        \
   [Proj L SDI]  [Proj R SDI]  [HyperDecks]
           \                /
            [Confidence Mon (AUX Slides)]
```

Comms:
```
[Clear-Com MS] --XLR--> [Beltpacks: Cam1/Cam2/V1/SM]
Ch A: Audio/LX | Ch B: Video/Stage
```

---

## Responsibilities

- Producer/Show Caller
  - Owns show flow, cues, and comms discipline
- Technical Director (TD)
  - Oversees all departments; final safety and power sign-off
- FOH Audio Engineer
  - Mixes house and broadcast sends; manages RF with A2
- Monitor Engineer
  - Manages wedge/IEM mixes; coordinates with band MD
- A2 (Audio Utility/RF)
  - Mic handling, RF coordination, battery management, stage patch
- Video Director (V1)
  - Camera blocking, switch, graphics integration
- V2 (Shader/Utility)
  - Camera control, ISO records, cable management
- Lighting Director (L1)
  - Focus, programming, show ops; maintains camera lighting levels
- L2 (Electrician)
  - Distro, dimming, DMX/Power, fixture maintenance
- Rigger
  - All rigging points and truss per plot
- Stage Manager (SM)
  - Backstage traffic, stage turns, panel/band setups
- Hands (Local Crew)
  - Load-in/out, cable runs, general support

---

## Schedule & Execution Steps

Day -14 to -7 (Preproduction)
- Confirm room dimensions, rigging plot, power locations
- Advance with venue on dock times, union rules, noise curfew
- Lock input list, RF plan, screen sizes, projector throw

Day -2 (Paper Tech)
- Finalize show flow, cue sheets, Run of Show (ROS)
- Distribute labeling, patch sheets, and file naming conventions

Day -1 (Shop Prep)
- Build and test Dante network, ATEM/MA showfiles
- Charge/test RF, label mics and packs
- Pack lists checked; spares included (10–15%)

Day 0 (Show Day)
- 08:00 Truck at dock; Crew call
- 08:00–10:00 Rigging & power tie-in (Lighting/Video first, then Audio)
- 10:00–12:00 Hang PA, truss, run cabling; place consoles and video world
- 12:00–13:00 Lunch
- 13:00–14:30 Line check (Audio), projector focus, camera shading
- 14:30–15:30 Soundcheck (Band), monitor mixes
- 15:30–16:30 Lighting focus and looks; graphics check
- 16:30–17:00 Presenter mic fit, RF check, comms check
- 17:00 Doors; walk-in music/cues
- 17:30–19:30 Show
- 19:45–22:00 Strike and load out (as allowed by venue)

---

## Dependencies

- Venue
  - Power: 200A 3P for LX, 100A 3P for Video, 60A 3P for Audio (separate legs if possible)
  - Rigging: Approved points with load certs; lift access
  - Blackout capability and hazer approval
  - Internet (if streaming): Dedicated 20 Mbps up/down, hardline
  - Dock access for 26’ box truck or semi; storage for cases

- Client
  - Graphics delivery: 16:9, 1920x1080, .pptx and .mp4 H.264; due Day -2
  - Name keys, logos, and fonts provided
  - Run of Show locked Day -1 17:00

- Compliance & Safety
  - Fire egress clear; cable ramps in all crossings
  - All distro by licensed electrician; GFCI where required
  - Weight loads per rigging engineer

---

## Risk Management & Contingencies

- Redundancy
  - Spare RF HH and Lav pre-coordinated and labeled
  - Backup playback laptop mirrored over HDMI>SDI
  - Secondary Dante path; switches on UPS
  - Projector spares or cross-feeding L/R in failure mode

- Recording
  - Dual record on HyperDeck + DAW; media checked pre-show
  - Audio headroom: -18 dBFS nominal, peaks -6 dBFS

- RF
  - Pre-show full scan; record spectrum; assign backups
  - Fresh batteries: swap per segment or at intermission

- Weather/Noise
  - If outdoor/atrium: wind/noise plan (windscreens, lower PA SPL by zone)

---

## Labeling & File Naming

- Channels: “01_Kick”, “19_Lectern”, “24_Panel1”, etc.
- Cables: Heatshrink IDs each end: “RioA-CH01”, “ATEM-IN1”
- Showfiles:
  - Audio: “Event_MMDD_CL5.show”
  - Video: “Event_MMDD_ATEM.xml”
  - Lighting: “Event_MMDD_MA3.show”
  - ROS: “Event_MMDD_ROS_vX.xlsx”

---

## References & Templates

1) Blank Input List Template
```
| Ch | Source | Mic/DI | Stand | Box | Notes |
```

2) Blank Output Patch Template
```
| Output | Destination | Connector | Location | Notes |
```

3) Stage Plot Template (ASCII)
```
 ----------------------------------------------------------
 |                        UPSTAGE                         |
 |  [Pos/Source]   [Pos/Source]   [Pos/Source]            |
 |                                                       |
 |---------------------- PERFORMANCE ---------------------|
 |  [Lectern]     [Panel Table]     [DSM]                 |
 |  FF1   FF2        FF3   FF4                          |
 ----------------------------------------------------------
```

4) DMX Patch Template
```
Universe __ : Addr Start – End : Fixture Type : Qty : Notes
```

5) RF Coordination Checklist
- Room scan saved
- Intermod-safe frequencies assigned
- Antenna placement checked
- Pack/mic labels match console channels
- Spare kit programmed

6) Cable Plan Checklist
- Power first, then signal
- Audio left, video right when crossing
- SDI >50' on coax 12G or fiber
- Tape paths; ramps on crossings

---

## Notes for Venue & Vendor

- Submit rigging plot and power request 10 business days before show
- Confirm projector throw and screen sightlines based on final seating plan
- Provide updated CAD of room with hang points and obstructions
- Notify if ceiling height <18' or room length <100' to adjust PA/screen sizes

---

## Contact Matrix (Example)

- Producer/Show Caller: Jane Doe, +1-555-0100, jane@eventsco.com
- Technical Director: Mark Lee, +1-555-0101, mark@eventsco.com
- Audio Lead (FOH): Priya K., +1-555-0102
- Video Director: Luis R., +1-555-0103
- Lighting Director: Alex S., +1-555-0104
- Venue Ops: Hotel AV/Power, +1-555-0199

---

This specification, plot, and signal flow document provides the baseline for consistent technical execution. Any substitutions should be equivalent or better and approved by the Technical Director in advance.