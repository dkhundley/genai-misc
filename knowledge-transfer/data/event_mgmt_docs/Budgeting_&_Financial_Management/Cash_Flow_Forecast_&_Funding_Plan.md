# Cash Flow Forecast & Funding Plan

Document title: Cash Flow Forecast & Funding Plan  
Topic: Budgeting & Financial Management  
Audience: Event and operations teams, finance, and leadership

## Overview

Purpose: Provide a reliable, actionable view of cash inflows/outflows, deposit schedules, and contingency reserves to ensure liquidity for the event lifecycle. Outputs include:
- A rolling 12-month cash flow spreadsheet (with base/optimistic/pessimistic scenarios)
- A monthly burn chart
- Funding trigger points and predefined actions

Scope: Applies to mid-size events (example below: 600-person conference), but structure scales to any program.

Tools: Google Sheets or Excel, bank portal, accounting system, CRM/contract tracker.

Cadence:
- Daily: Bank balance check and cash alerts
- Weekly: Update forecast and AR/AP status; 15-min “cash huddle”
- Monthly: Present updated forecast, burn chart, and trigger status to leadership/board

Key definitions:
- Net Burn: Cash outflows minus operating inflows (excludes financing flows like debt draws)
- Runway: Available operating cash / average next-3-month net burn
- Minimum Liquidity: The lower of $25,000 or 5% of total event budget, plus restricted reserves
- Restricted Reserve: Ring-fenced cash for contingencies (separate line item)

---

## Key Steps

1) Set up the workbook (single source of truth)
- Tabs: Assumptions, Inflows, Outflows, Cash Flow (Summary), Burn Chart, Triggers, Scenario_Pessimistic, Scenario_Optimistic
- Naming: “EventName_CashFlow_YYYYMMDD_vX.xlsx”
- Access: Finance Lead (edit), Event Director (edit), CEO/Board (view)

2) Establish assumptions
- Event date: Mid-June 2026
- Currency: USD
- Payment terms: Vendors Net-30; sponsorship invoices due on signature (50%) and 30 days pre-event (50%)
- Ticket settlement: T+2 days (credit card processor)
- Payroll: 15th and last day of month; average loaded monthly cost $35,000
- Software/registration fee: $2,000/month
- Reserve target: 3 months fixed OPEX (payroll + software) = ~$111,000; plan to build via monthly transfers

3) Build inflows
- Revenue streams: Ticket sales (by phase), Sponsorships (by contract + collection schedule), Exhibitors, Grants
- Add other inflows: Refunds, tax rebates, financing (LOC/bridge), interest
- Capture expected dates (not just month) and terms; include probability for pipeline if needed

4) Build outflows
- Fixed OPEX: Payroll, software, insurance
- Vendor milestones: Venue, catering, AV, decorators, printing/signage, swag, marketing, travel
- Taxes and fees: Sales tax, ticketing/platform fees
- Reserve transfers: Planned monthly amounts until reserve target met

5) Reconcile to bank and test
- Opening cash = reconciled bank balance at start of period
- Confirm that Ending Cash(t-1) = Opening Cash(t)
- Run a simple integrity check: Opening Cash + Total Inflows − Total Outflows = Ending Cash

6) Add scenarios
- Base: Contracted and high-probability revenue; agreed vendor schedules
- Pessimistic: −20% ticket volume, sponsorships slip 30 days, add 10% cost overruns on variable vendors
- Optimistic: +10% ticket volume, on-time sponsorships, 5% savings on AV and catering

7) Create the burn chart
- Plot monthly net operating cash (exclude financing) and highlight trend/averages
- Highlight months where burn exceeds forecast tolerances

8) Define triggers and actions
- Set thresholds for runway and minimum liquidity; document who does what, by when
- Pre-approve drawdown documents for LOC and align board approvals for bridge options

9) Operate the cadence
- Weekly cash huddle (Finance, Event Ops, Sales/Sponsorship): review changes in AR/AP, deposits due, risks, and trigger status
- Monthly leadership review: approve changes, cost controls, or funding actions

---

## Example: 6-Month Cash Flow (Base Case)

Context: 600-person conference (June), budget ~$450k. Opening cash: $200,000. Reserve strategy: $10,000/month transfers Feb–May to restricted reserve.

Inflows assumptions:
- Sponsorships: $180,000 total; 50% on signature, 50% in May (30 days pre-event)
  - Jan: 3 sponsors sign (3 × $15k) = $45k
  - Feb: 2 sponsors sign (2 × $15k) = $30k
  - Apr: 1 sponsor signs ($15k)
  - May: All balances due (6 × $15k) = $90k
- Ticket sales: $230,000 total; monthly flow = Jan 10k, Feb 20k, Mar 60k, Apr 80k, May 50k, Jun 10k
- Exhibitors: $40,000 total; Mar 15k, Apr 25k
- Grant: $20,000 in Feb
- Line of Credit (LOC): $50,000 draw in June to maintain liquidity

Outflows assumptions:
- Payroll: $35,000/month
- Software/registration: $2,000/month
- Marketing: Jan 10k, Feb 15k, Mar 15k, Apr 12k, May 8k, Jun 5k
- Venue: $90,000 total; Jan 27k, Apr 36k, Jun 27k
- Catering: $120,000 total; Apr 24k, Jun 96k
- AV: $70,000 total; Mar 21k, Jun 49k
- Insurance: Jan 6k
- Printing/Signage: May 12k
- Swag: May 8k
- Travel/Lodging (staff): May 5k, Jun 15k
- Reserve transfers: Feb–May $10k/month

Table notes:
- Net Cash Flow includes reserve transfers and excludes financing unless shown (LOC in June).
- Restricted Reserve balance tracked separately to compute Available Operating Cash.

Cash flow summary (USD):

| Month | Opening Cash | Inflows | Outflows | Net Cash Flow | Ending Cash | Reserve Transfer | Reserve Balance | Available Operating Cash |
|------|---------------|---------|----------|---------------|-------------|------------------|-----------------|--------------------------|
| Jan  | 200,000       | 55,000  | 80,000   | -25,000       | 175,000     | 0                | 0               | 175,000                  |
| Feb  | 175,000       | 70,000  | 62,000   | 8,000         | 183,000     | 10,000           | 10,000          | 173,000                  |
| Mar  | 183,000       | 75,000  | 83,000   | -8,000        | 175,000     | 10,000           | 20,000          | 155,000                  |
| Apr  | 175,000       | 120,000 | 119,000  | 1,000         | 176,000     | 10,000           | 30,000          | 146,000                  |
| May  | 176,000       | 140,000 | 80,000   | 60,000        | 236,000     | 10,000           | 40,000          | 196,000                  |
| Jun  | 236,000       | 60,000* | 229,000  | -169,000      | 67,000      | 0                | 40,000          | 27,000                   |

*June inflows include $10,000 tickets + $50,000 LOC draw.

Runway check (end of May, before June outflows):  
- Available Operating Cash: $196,000  
- Next-3-month average net burn (operating only, excluding financing): approx. $84,667 (Mar -8k, Apr +1k, Jun -219k → take next-3 months May–Jul realistically; for illustration, focus on known heavy month Jun)  
- Result: Sufficient as of May, but June would fall below minimum without LOC draw; hence planned $50,000 draw to maintain Available Operating Cash ≥ $25,000.

---

## Deposit Schedules (Example)

Customer and sponsor receipts:
- Sponsorships ($180k total)
  - 50% on contract: Jan (3 sponsors, $45k), Feb (2 sponsors, $30k), Apr (1 sponsor, $15k)
  - 50% balances: May ($90k)
- Exhibitors ($40k): Mar ($15k), Apr ($25k)
- Ticket sales ($230k): Jan ($10k), Feb ($20k), Mar ($60k), Apr ($80k), May ($50k), Jun ($10k)

Vendor deposits and milestones:
- Venue ($90k): Jan 30% ($27k), Apr 40% ($36k), Jun 30% ($27k)
- Catering ($120k): Apr 20% ($24k), Jun 80% ($96k)
- AV ($70k): Mar 30% ($21k), Jun 70% ($49k)

Reserve schedule:
- Restricted Reserve transfers: $10k/month in Feb–May, target reserve $40,000 by end of May

---

## Burn Chart (Operating Net Cash, Excluding Financing)

Monthly net operating cash (USD):
- Jan: -25,000
- Feb: +8,000
- Mar: -8,000
- Apr: +1,000
- May: +60,000
- Jun: -219,000

Visual (relative scale; bars approximate):

Jan  ▉▉▉▉▉▉▉▉▉▉ (-25k)  
Feb  ▉ (+8k)  
Mar  ▉▉▉▉ (-8k)  
Apr  ▉ (+1k)  
May  ▉▉▉▉▉▉▉▉▉▉▉▉ (+60k)  
Jun  ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ (-219k)

Interpretation:
- Cash-light months (Jan, Mar) due to deposits and marketing spend
- Positive months (Apr, May) from ticketing and sponsorship balances
- Event month (Jun) is outflow-heavy; plan ahead with funding and AP timing

---

## Funding Trigger Points

Thresholds and actions to ensure liquidity:

- Green (Runway ≥ 6 months and Available Operating Cash ≥ Reserve Target + $50k)
  - Action: Operate normally; opportunistic early-pay discounts with vendors

- Yellow (Runway 3–6 months OR Available Operating Cash < Reserve Target + $25k within 60 days)
  - Action (within 7 days):
    - Accelerate AR: Offer 2% discount for early sponsor/exhibitor payment
    - Tighten expense approvals to Director level; pause non-critical marketing tests
    - Reforecast weekly; confirm LOC capacity and documentation

- Orange (Runway 1–3 months OR forecasted Available Operating Cash < $25k within 30 days)
  - Action (within 5 days):
    - Initiate LOC draw to maintain ≥ $25k Available Operating Cash
    - Freeze new hires/contractors; defer non-essential capex and swag upgrades
    - Renegotiate vendor milestone timing (shift 10–20% to post-event if feasible)
    - Launch ticket flash sale to bring forward cash receipts

- Red (Runway < 1 month OR negative Available Operating Cash forecast within 14 days)
  - Action (within 48 hours):
    - Execute pre-approved bridge financing or invoice factoring
    - Reduce discretionary OPEX by 20% immediately
    - Board-level daily oversight until Green/Yellow status restored

Governance:
- Finance Lead owns trigger monitoring (updated weekly)
- Event Director owns vendor renegotiations and spend controls
- CEO approves LOC/bridge draws; Board approves equity/convertible options

---

## Responsibilities

- Finance Lead (Owner)
  - Maintain and publish weekly cash flow forecast and trigger status
  - Reconcile to bank; manage LOC/financing documentation
  - Run scenario analyses; update burn chart

- Event Director
  - Confirm vendor schedules, deposits, and any scope changes
  - Approve discretionary spend within limits; escalate for overages
  - Coordinate with vendors to shift milestones if needed

- Sales & Sponsorship Lead
  - Maintain sponsorship and exhibitor pipeline and collection schedule
  - Trigger early-payment incentives and follow up on AR

- AP/AR Specialist
  - Issue invoices on contract signature; monitor collections
  - Schedule payments per approved forecast and vendor terms

- CEO/Board
  - Approve funding actions beyond pre-set thresholds
  - Review monthly liquidity pack and scenario outcomes

- Legal/Contracts
  - Ensure payment terms and cancellation clauses support cash needs
  - Prepare pre-approved documents for LOC/bridge financing

---

## Dependencies

- Executed contracts with clear payment schedules (clients and vendors)
- Accurate CRM/pipeline and invoicing data for sponsorships/exhibitors
- Payroll calendar and benefits/taxes schedule
- Accounting system for AP aging and accruals
- Bank line of credit availability and covenants
- Payment processor settlement timing and fees
- Tax compliance calendar (sales/use taxes, withholding)

---

## References and Templates

- Cash Flow Template (Google Sheets): [link placeholder]
  - Key formulas:
    - Ending Cash (month t) = Opening Cash + Total Inflows − Total Outflows
    - Available Operating Cash = Ending Cash − Reserve Balance
    - Runway (months) = Available Operating Cash / AVG(next 3 months’ net operating burn)
- Burn Chart Template: [link placeholder]
- Trigger Tracker & Actions Log: [link placeholder]
- AR Collections Playbook (email templates, discount offers, call cadence): [link placeholder]
- Vendor Negotiation Guide (milestone shifts, early-pay discounts, service deferrals): [link placeholder]

---

## Practical Tips

- Front-load inflows: Align sponsorship invoicing to contract signature and add late fees
- Spread deposits: Negotiate vendor schedules to match revenue peaks (Apr/May)
- Separate reserve account: Keep restricted reserve in a distinct sub-account for clarity
- Update weekly: Reflect actual collections and payment commitments immediately
- Communicate early: Share trigger status in weekly huddles; no surprises in event month
- After-action: Post-event, release a portion of reserves once all critical vendor bills clear and AR collected

---

## Glossary

- AR/AP: Accounts Receivable/Payable
- LOC: Line of Credit
- Net Burn: Outflows − operating inflows (excludes financing)
- Runway: Months until Available Operating Cash reaches zero, at current burn
- Restricted Reserve: Ring-fenced cash to handle unforeseen costs without jeopardizing operations

This document, combined with the templates and cadence above, gives any team immediate, actionable guidance to forecast cash, visualize burn, and execute funding steps to ensure uninterrupted event delivery.