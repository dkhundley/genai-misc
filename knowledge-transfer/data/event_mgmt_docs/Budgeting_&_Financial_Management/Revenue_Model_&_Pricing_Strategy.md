# Revenue Model & Pricing Strategy

Document owner: Finance Lead  
Version: 1.0  
Last updated: [fill in date]

## Overview
This document defines the event’s revenue model, pricing architecture, discounts, bundles, dynamic pricing rules, and the forecasting framework (including break-even and sensitivity scenarios). It is designed so any team member can implement pricing, forecast revenue, and monitor performance from day one.

Scope: A 2‑day, single‑track, in‑person conference with an optional virtual stream.

- Event dates: Dec 3–4, 2025
- Sales window: Apr 1–Dec 2, 2025
- Currency: USD
- Capacity (in-person): 600
- Target mix (baseline): 550 in‑person, 300 virtual
- Ticketing platform: [specify; e.g., Eventbrite, Hopin, Cvent]
- Payment fee assumption: 2.9% + $0.30 per transaction
- Sales tax: Collect where required by law (assume 0% in worked example; configure tax collection per jurisdiction)

Success metrics:
- Revenue: meet or exceed break-even by ≥15% margin
- Sell-through: ≥90% of in-person capacity
- CAC payback: ≤1.0 event cycle
- NRR from corporate/partner bundles ≥ 20% of total revenue

---

## Pricing Matrix

Assumptions for variable costs (per unit):
- In-person GA: $85 (catering $65, materials $7, badge $3, swag $10)
- In-person VIP: $170 (GA variable $85 + VIP lounge $20 + upgrade catering $40 + premium swag $25)
- Student/Nonprofit: $85
- Virtual: $4 (streaming + support)
- Workshop add-on (half-day): $35
- Networking dinner add-on: $90
- Processing fees: 2.9% + $0.30 per transaction (deduct from price to get net)

Note: Prices are customer-facing; all fees, taxes, and discounts applied at checkout per policy.

### Ticket Tiers (Time- and Inventory-Based)
- Tier advancement triggers:
  - Date thresholds and sell-through thresholds (see Dynamic Pricing Rules).
  - Holdback: 10% GA inventory for partners/sponsors.

| SKU | Type | Tier | Public Price | On-Sale Window (or Trigger) | Inventory Cap | Notes |
|-----|------|------|--------------|------------------------------|---------------|-------|
| GA-SEB | In-person GA | Super Early Bird | $399 | Apr 1–Apr 30 OR first 100 GA sold | 100 | Non-refundable promotional tier |
| GA-EB | In-person GA | Early Bird | $499 | May 1–Jul 31 OR 40% GA sold | 160 | |
| GA-STD | In-person GA | Standard | $599 | Aug 1–Nov 15 | 120 | |
| GA-LM | In-person GA | Last-Minute | $699 | Nov 16–Dec 2 or sell-out | 70 | Last 50 seats may surge (see rules) |
| VIP-SEB | In-person VIP | Super Early Bird | $899 | Apr 1–Apr 30 OR first 15 VIP sold | 15 | |
| VIP-EB | In-person VIP | Early Bird | $999 | May 1–Jul 31 OR 50% VIP sold | 20 | |
| VIP-STD | In-person VIP | Standard | $1,099 | Aug 1–Nov 15 | 25 | |
| VIP-LM | In-person VIP | Last-Minute | $1,199 | Nov 16–Dec 2 or sell-out | 20 | |
| STU | Student/Nonprofit | Flat | $249 | Apr 1–Dec 2 | 80 | Verification required; not combinable |
| VIRT-SEB | Virtual | Super Early Bird | $79 | Apr 1–Apr 30 | N/A | |
| VIRT-EB | Virtual | Early Bird | $99 | May 1–Jul 31 | N/A | |
| VIRT-STD | Virtual | Standard | $129 | Aug 1–Nov 15 | N/A | |
| VIRT-LM | Virtual | Last-Minute | $149 | Nov 16–Dec 2 | N/A | |

### Add-ons and Bundles
| SKU | Type | Price | Notes |
|-----|------|-------|-------|
| WS-HALF | Workshop (half-day) | $199 | Capacity by room; multiple sessions may run |
| DIN-NET | Networking Dinner | $229 | Offsite venue; dietary options included |
| BNDL-PRO | Pro Experience Bundle | $899 | GA Standard + Workshop + Dinner (12.5% off combined list); consumes 1 GA seat |
| TEAM-5 | Corporate 5-pack (GA) | 10% off per seat | Must purchase in single order; cap 15 bundles |
| TEAM-10 | Corporate 10-pack (GA) | 15% off per seat | Cap 10 bundles |
| VIRT-25 | Virtual Group License (25 seats) | $1,999 | Named or floating seats; 1 admin seat |
| VIRT-100 | Virtual Group License (100 seats) | $6,999 | Enterprise license; SSO optional |

Discount governance:
- Stacking not allowed (only one discount or bundle per cart).
- Exclusions: Student/Nonprofit, bundles, and group licenses cannot accept additional codes.
- Minimum advertised price (MAP): Never below Super Early Bird for each SKU.
- Expirations: All codes have explicit end dates and redemption caps.

---

## Dynamic Pricing Rules

Configure in the ticketing platform as automated rules with manual override by Finance Lead.

Triggers:
- Date-based: Advance tiers on scheduled dates.
- Inventory-based: Advance tiers when sell-through exceeds thresholds.
- Velocity-based: Adjust when weekly pace deviates from target.

Rules:
1. Tier advancement (dual trigger):
   - Advance to next tier when either:
     - Date threshold is reached, or
     - Sell-through of current tier ≥ 95% and weekly pace ≥ 120% of target.
2. Pace protection:
   - If trailing 7-day paid units < 50% of weekly target for a SKU, authorize a 48-hour, single-use code blast at 15% off (max 100 redemptions) excluding Student/Nonprofit and bundles.
3. Surge pricing (final week):
   - If remaining GA inventory < 50 seats and days to event ≤ 7, apply $50 surge to GA-LM (system SKU: GA-LM-SURGE).
4. Inventory holdback:
   - Reserve 10% of GA capacity for sponsor bundles and strategic partners; release any remainder 14 days before event.
5. Price floor/ceiling:
   - Floor = Super Early Bird price; Ceiling = Last-Minute + $50 surge (only in final 7 days).
6. Anti-abuse:
   - Unique codes with per-contact limits (e.g., 1 redemption/person); require email verification; log IP/device fingerprint for anomalies.

Reporting:
- Daily: Sell-through, pace vs. plan, tier status, conversion funnel.
- Weekly: Price realization (net ARPPU), discount leakage, and ROI by channel.

---

## Forecasting Model

Model outputs: Gross revenue, net revenue after processing fees, contribution margin (CM), break-even, and profit.

Key inputs:
- Prices by tier/SKU
- Planned unit sales per SKU (by week or tier)
- Variable cost per unit (by SKU)
- Processing fee assumption (2.9% + $0.30)
- Fixed costs
- Marketing mix and funnel assumptions (traffic, CTR, conversion)

Formulas:
- Processing fee per unit = (Price × 2.9%) + $0.30
- Net revenue per unit = Price − Processing fee
- Contribution margin per unit = Net revenue per unit − Variable cost per unit
- Total CM (per SKU) = Contribution margin per unit × Units sold
- Event CM = Sum of Total CM across all SKUs
- Profit (Loss) = Event CM − Fixed costs
- Break-even units (weighted) = Fixed costs ÷ Weighted average CM per unit

Funnel framework (illustrative baseline):
- Traffic: 120,000 unique sessions to landing pages
- Landing → Checkout start: 4.0%
- Checkout start → Purchase: 55%
- Overall website conversion: 2.2%
- Email campaign: Open 35%, CTR 4.5%, Purchase rate 3.0% (from click)
- Paid media: CPC $2.00; Purchase rate 1.2% from click; CAC ~$167
- Organic/referral: Purchase rate 2.5% from session

Use cohort-based forecasting:
- Split demand by channel and time period (aligned to tiers).
- Apply channel-specific conversion rates.
- Apply dynamic pricing triggers to reallocate demand to higher tiers as inventory/date thresholds are hit.

### Worked Example (Baseline Mix)
Projected units:
- GA: 390 units (100 SEB, 150 EB, 100 STD, 40 LM)
- VIP: 60 units (15 SEB, 20 EB, 15 STD, 10 LM)
- Student/Nonprofit: 60 units
- Pro Experience Bundles (GA + WS + Dinner): 40 units
- Virtual: 300 units (60 SEB, 100 EB, 100 STD, 40 LM)
- Add-ons sold separately: Workshop 80, Dinner 140

Fixed costs (example):
- Venue & security: $70,000
- AV & staging: $85,000
- Production staff & temp: $35,000
- Speaker fees/travel: $60,000
- Marketing fixed (creative/baseline media): $40,000
- Insurance, legal, permits: $10,000
- Ticketing platform base fee: $5,000
- Contingency (5% fixed): $15,250
- Total fixed costs: $320,250

Contribution margin summary (rounded):
- In-person GA (all tiers combined): ~$163,467 CM
- Pro Experience Bundles: ~$26,505 CM
- VIP (all tiers combined): ~$49,926 CM
- Student/Nonprofit: ~$9,389 CM
- Virtual (all tiers combined): ~$31,239 CM
- Add-ons sold separately: Workshop ~$12,634 CM; Dinner ~$18,488 CM
- Total Event CM: ~$311,648

Profit (Loss) = $311,648 − $320,250 = −$8,602 (near break-even; action required—see levers below)

Levers to close the gap (examples):
- Sell +60 additional GA at Standard/Late tiers: +~$31,800 CM
- Sell +10 VIP at higher tiers: +~$9,000 CM
- Sell +150 Virtual: +~$15,600 CM
- Drive +90 add-on purchases (mix): +~$12,900 CM
- Combined impact (illustrative stretch): +~$69,300 CM → Profit ~+$60,700

### Break-even Analysis
Method 1: Weighted attendees
- Weighted average CM per “unit” (across all SKUs in example) ≈ $311,648 ÷ 850 units ≈ $366.65
- Break-even units at this mix ≈ $320,250 ÷ $366.65 ≈ 873 units
- Baseline units sold in example: 850 → short by ~23 “units” at current mix

Method 2: In-person focus (excluding virtual)
- In-person attendees = 550 (includes bundles)
- In-person CM (incl. bundles, excl. separate add-ons) ≈ $249,287 → ~$453 CM/attendee
- Break-even in-person attendees alone (no virtual or add-ons) = $320,250 ÷ $453 ≈ 707 (over capacity). Therefore, plan assumes virtual and add-ons to close gap.

### Sensitivity Scenarios (Quick-Plan)
- Downside (0.8× volume, lower-tier skew, higher discount use)
  - Units: ~440 in-person, 220 virtual; add-ons −30%
  - Event CM: ~$230k–$240k
  - Profit (Loss): ~−$80k to −$90k
  - Mitigation: Pull forward tier changes, launch partner bundles, shift budget to higher-ROAS channels, expand virtual enterprise licenses.
- Baseline (as worked example)
  - Event CM: ~$312k; Profit: ~−$9k
  - Actions: Price testing on LM, increase urgency (scarcity banners), add 1–2 sponsors with ticket blocks, push corporate 10-packs.
- Stretch (sell-out; more high-tier; +150 virtual; +90 add-ons)
  - Units: 600 in-person, 450 virtual
  - Incremental CM: +~$69k vs. baseline
  - Event CM: ~+$381k
  - Profit: ~+$61k
  - Tactics: Speaker-led code campaigns, ABM for TEAM-10 and VIRT-100, PR hits near tier transitions.

---

## Discount & Code Strategy

- Standard partner code: 10–15% off GA/VIP Standard tier (not applicable to SEB, Student/Nonprofit, bundles). Redemption cap: 100 per partner. Unique UTM and code per partner.
- Speaker/influencer code: 20% off GA/VIP; limit 10 redemptions per speaker.
- Flash offers: 15% off for 48 hours during slow weeks; cap 200 redemptions event-wide.
- Corporate offers:
  - TEAM-5: 10% off list (must buy in single order; no further codes)
  - TEAM-10: 15% off list
- Governance: No stacking; expiration and caps enforced; report discount leakage weekly.

---

## Sales & Communications Timeline

- Apr 1: Launch SEB (30 days). Press release + email #1. Paid social burst.
- May 1: Auto-advance to EB. Publish 3 announced speakers. Partner code activation.
- Jun–Jul: EB push. Three partner webinars; ABM outreach to target accounts.
- Aug 1: Advance to Standard. Reveal agenda. Open bundles and add-ons. Begin retargeting.
- Oct 1: Corporate bundle reminder; sponsor ticket allocations due.
- Nov 1: Last Standard push. Seat map update (scarcity).
- Nov 16: Advance to Last-Minute. Enable LM surge rule from Nov 26 if <50 GA remain.
- Dec 1–2: Final 48-hour urgency campaign (no discounts; highlight value and logistics).

Cadence:
- Email: 2–3 per month (segment by behavior).
- Social/paid: Always-on retargeting; spikes at tier changes and content drops (speakers/agenda).

---

## Responsibilities

- Finance Lead (Doc owner)
  - Own pricing, forecasting, break-even analysis, and approvals for dynamic changes
  - Maintain P&L, margin tracking, and weekly reporting
- Ticketing Manager
  - Implement SKUs, tiers, rules, discount codes, bundles in platform
  - Ensure tax, fee, and receipt configurations are correct
- Marketing Lead
  - Own demand gen and channel mix; execute tier-transition campaigns
  - Manage partner codes, content drops, and funnel optimization
- Data Analyst/RevOps
  - Maintain dashboards (traffic, funnel, sell-through, price realization)
  - Run sensitivity and pacing reports; recommend pricing actions
- Sponsorship/Partnerships Lead
  - Drive corporate bundles, group licenses, and sponsor allocations
- Customer Support
  - Manage exchanges/refunds per policy; code troubleshooting; invoicing support
- Legal/Compliance
  - Review tax nexus, terms, cancellation/refund policy, and promotional T&Cs

Approval thresholds:
- Price changes within defined rules: Finance Lead + Marketing Lead
- Exceptions (below floor/above ceiling; special partner deals): CFO/GM approval

---

## Operational Policies

- Taxes and invoicing:
  - Configure tax collection based on venue jurisdiction; include tax line on invoices.
  - Offer invoicing for TEAM-10, VIRT-100, and sponsors; Net 14 terms.
- Refunds and transfers:
  - Refunds: Within 14 days of purchase and ≥45 days before event; 10% admin fee; no refunds after. Name transfers allowed until 3 days prior.
- Accessibility/Equity:
  - Scholarship/Hardship tickets: Up to 3% of in-person capacity (apply; approval by committee).
- Compliance:
  - Adhere to MAP policy; truthful advertising; opt-in for marketing communications; PCI compliance via platform.

---

## Dependencies

- Ticketing platform features:
  - Tiered pricing with date and inventory triggers
  - Discount code management (caps, expirations, exclusions)
  - Bundles/kits and add-ons
  - Tax and fee configuration
  - Reporting API for real-time dashboards
- Website/Martech:
  - UTM tracking; pixels for paid media; CRM integration
  - Landing pages for each tier/changeover (for scarcity/urgency)
- Finance systems:
  - GL accounts for ticket revenue, taxes, fees, COGS, and marketing
- Legal:
  - Event terms, refund policy, privacy policy, partner agreements

---

## References or Templates

1) Pricing Matrix Template (CSV headers)
- sku
- product_name
- type (GA/VIP/STUDENT/VIRTUAL/ADDON/BUNDLE)
- tier (SEB/EB/STD/LM/FLAT)
- public_price
- floor_price
- start_date
- end_date
- inventory_cap
- sell_through_trigger
- variable_cost
- processing_fee_percent
- processing_fee_fixed
- contribution_margin_formula
- exclusions (e.g., no-discount)
- notes

2) Forecasting Workbook (Tabs)
- Assumptions:
  - Fees, taxes, variable costs, fixed cost categories
- Pricing:
  - All SKUs with tier dates/prices/inventory caps
- Demand Plan:
  - Weekly traffic by channel; CTR; conv. rates; units by SKU/tier
- Revenue & CM:
  - Unit × price; fees; CM by SKU; Event CM; P&L
- Scenarios:
  - Downside/Base/Stretch toggles (volume, price mix, discount rate)
- Dashboard:
  - KPIs: Pace vs. plan, sell-through, ARPPU, CAC, profit forecast

Key cell formulas (example):
- Processing fee per unit = price*0.029 + 0.30
- Net/unit = price − processing_fee
- CM/unit = net/unit − variable_cost
- Total CM (SKU) = CM/unit × units
- Event CM = SUM(all SKU CM)
- Profit = Event CM − Fixed costs
- Break-even units = Fixed costs ÷ Weighted avg CM/unit

3) Weekly Revenue Report Checklist
- Units sold by SKU vs. plan
- Price realization (avg price vs. list)
- Discount usage and leakage
- Funnel performance by channel
- Inventory and tier status
- Recommended actions (price moves, campaigns)

---

## How to Use This Document (Step-by-Step)

1) Configure SKUs and tiers in the ticketing platform using the Pricing Matrix.
2) Set dynamic pricing rules and guardrails; load discount codes with caps and exclusions.
3) Build the Forecasting Workbook with current assumptions and demand plan.
4) Launch with SEB; monitor daily; run weekly pacing vs. plan reports.
5) Trigger tier transitions automatically; deploy flash offers only when pace thresholds signal.
6) Adjust channel mix and creative at tier changes to shift demand to higher-value SKUs.
7) Reforecast weekly; escalate if trending below break-even (activate bundles, corporate outreach, and group licenses).
8) Two weeks pre-event: release holdback inventory; consider surge pricing if conditions met.
9) Post-event: reconcile P&L; capture learnings for next cycle.

Questions or change requests: Contact Finance Lead and Ticketing Manager.