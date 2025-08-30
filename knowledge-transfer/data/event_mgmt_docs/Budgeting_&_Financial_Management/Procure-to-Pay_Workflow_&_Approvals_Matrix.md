# Procure-to-Pay (P2P) Workflow & Approvals Matrix
Topic: Budgeting & Financial Management  
Document owner: Finance Operations  
Version: 1.0 | Last updated: 2025-08-23 | Applies to: All departments, all spend types (OPEX/CAPEX)

---

## Overview
This document maps the end-to-end procure-to-pay process—from vendor selection through payment—so any team member can request, approve, receive, and pay for goods/services in a compliant, controlled, and timely manner. It includes:
- A swimlane process diagram (with text fallback)
- Approval thresholds and who must approve
- Required documentation and system touchpoints
- Target timelines and SLAs
- Exceptions and escalation paths

Scope includes purchases above $100 (or local petty cash threshold) that will be paid by the company via PO and invoice.

Primary systems:
- eProcurement/ERP: Coupa or NetSuite (PR/PO, receipts, 3-way match)
- Contract Management: Ironclad or DocuSign CLM
- AP Automation: Tipalti or Bill.com (invoice capture, payments)
- Ticketing (optional): Jira/ServiceNow intake for PR initiation

---

## Swimlane Process Diagram

Mermaid (renderable in supported viewers):
```mermaid
flowchart TD
  subgraph RQ[Requisitioner]
    A0[Identify Need & Budget] --> A1[Gather Requirements & Quotes (≥2 for >$25k)]
    A1 --> A2[Create Purchase Requisition (PR) with docs]
    A7[Confirm Receipt in system]
  end

  subgraph BO[Budget Owner / Dept Mgr]
    B0[Budget Check & Approval]
  end

  subgraph PRC[Procurement]
    P0[Validate PR & sourcing method]
    P1[Competitive Bid or Sole Source Review]
    P2[Negotiate & Finalize Pricing/Terms]
    P3[Create/Dispatch Purchase Order (PO)]
  end

  subgraph LEG[Legal]
    L0[Contract Review & Redlines]
  end

  subgraph SEC[IT Security / Risk]
    S0[Security & Privacy Review (SaaS/IT)]
    S1[Vendor Risk & Insurance Validation]
  end

  subgraph VEN[Vendor]
    V0[Sign Contract & Accept PO]
    V1[Deliver Goods/Services]
    V2[Submit Invoice (matches PO)]
  end

  subgraph AP[Accounts Payable]
    AP0[Capture & Code Invoice]
    AP1[3-Way Match (PO, Receipt, Invoice)]
    AP2[Resolve Exceptions]
    AP3[Schedule Payment per Terms]
    AP4[Pay & Post to GL]
  end

  A0 --> B0 --> P0
  P0 -->|> $25k?| P1
  P1 --> P2
  P2 --> L0
  L0 --> S0
  S0 --> S1
  S1 --> P3
  P3 --> V0 --> V1 --> A7
  A7 --> AP0 --> AP1
  AP1 -->|Mismatch| AP2 --> AP1
  AP1 -->|Match| AP3 --> AP4
  V2 --> AP0
```

Text fallback (major handoffs):
- Requisitioner: Identify need and budget → collect quotes → create PR with documents.
- Budget Owner/Dept Manager: Verify budget availability and approve PR.
- Procurement: Validate sourcing method → bid/sole-source review → negotiate → create and dispatch PO.
- Legal: Review and approve contract (if applicable).
- IT Security/Risk: Review security, privacy, insurance, and vendor risk (if applicable).
- Vendor: Sign contract/accept PO → deliver → submit invoice referencing PO.
- AP: Capture invoice → 3-way match → resolve exceptions → schedule and release payment → post to GL.

---

## Step-by-Step Process (What to do and what to attach)

1) Identify Need and Budget (Req)
- Confirm the expense aligns to an approved budget line (OPEX/CAPEX) and cost center.
- Timeline: Same day.
- Attach: Business justification (1–2 sentences), preliminary scope or SOW draft.

2) Sourcing and Quotes (Req + Procurement for larger spend)
- For purchases >$25,000: Obtain ≥2 comparable quotes or a competitive RFP. If sole source, complete Sole Source Justification.
- For IT/SaaS: Request security questionnaire and data processing details early.
- Timeline: 1–10 business days depending on complexity.
- Attach: Quotes, bid tabulation, draft SOW/specs.

3) Create Purchase Requisition (Req)
- Create PR in ERP: include item/service description, quantity, unit price, tax, freight, GL account, cost center, project code, and planned delivery dates.
- Include vendor (if new, start onboarding now).
- Timeline: Same day.
- Attach: Quotes, SOW, bid tab, sole-source form (if used), budget reference.

4) Budget Owner / Department Approval (Manager/Owner)
- Verify business need, coding, and budget capacity.
- Timeline SLA: 2 business days.

5) Procurement Review (Procurement)
- Validate sourcing method, pricing reasonableness, and category policy.
- Initiate contract if needed; ensure PO terms apply for standard buys.
- Timeline SLA: 2–5 business days.

6) Risk, Legal, and Security Reviews (As needed)
- Legal: Contract, terms deviations, DPAs, SOWs.
- IT Security: SaaS/IT systems, data privacy, integrations.
- Risk/Insurance: COI requirements, supplier risk tiering, W-9/W-8.
- Timeline: 3–10 business days (parallel where possible).
- Attach: Redlines, DPIA/IT questionnaire, COI, W-9/W-8BEN-E, sanctions screening.

7) PO Creation and Dispatch (Procurement)
- Convert approved PR to PO. Include delivery locations, incoterms (if physical goods), and reference contract number.
- Dispatch PO to vendor; “no PO, no pay” notice included.
- Timeline: 1 business day.

8) Delivery and Receipt (Requisitioner/Receiving)
- Verify goods/services received; record receipt in ERP with quantities/date.
- For services, confirm milestones; upload signed timesheets or deliverable acceptance.
- Timeline: Within 1 business day of receipt.
- Attach: Packing slip, acceptance memo, milestone sign-off.

9) Invoice Submission (Vendor)
- Vendor emails or e-invoices referencing PO number and line items; one invoice per PO where possible.
- Timeline: Per vendor; encourage e-invoice portal usage.

10) Invoice Processing and 3-Way Match (AP)
- AP captures invoice → auto-codes → matches to PO and receipt.
- If mismatch, AP opens exception ticket to requisitioner/procurement.
- Timeline SLA: 3 business days from complete invoice.

11) Payment and Posting (AP)
- Payment per contractual terms (default Net 30 unless otherwise approved).
- Payment runs: ACH weekly on Wednesdays; wires Mon–Fri cutoff 1 PM local; checks only by exception.
- Remittance advice emailed to vendor; GL posted and documents archived.

12) Record Retention and Audit (Finance)
- Retain PR/PO, approvals, contracts, invoices, receipts, and payment confirmations for 7 years (or local statutory requirement).

---

## Approvals Matrix (Who must approve and when)

Notes:
- All thresholds refer to total commitment (incl. taxes, freight) per PO or contract year value.
- “AND” means cumulative approvals required; “OR” means either role can approve based on org size.

| Spend Tier | Category/Trigger | Required Approvals | Additional Reviews | Contract Signature Authority |
|---|---|---|---|---|
| $0–$4,999 | Any | Dept Manager (cost center owner) | — | Dept Head (if contract ≤ $5k) |
| $5,000–$24,999 | Any | Dept Manager AND Budget Owner (if different) | Procurement validation | Dept Head (≤ $25k) |
| $25,000–$99,999 | Any | Dept Manager AND Budget Owner AND Procurement | Legal if contract or T&Cs; Bid/sole-source doc | VP (owning function) or Procurement Director |
| ≥ $100,000 | Any | Dept Manager AND Budget Owner AND Procurement AND Finance Controller | Legal mandatory; Risk/Insurance; Competitive bid or CFO-approved sole source | CFO (or COO) |
| Any Amount | IT/SaaS handling company or personal data | Above approvals by spend | IT Security/Privacy review; DPA as needed | Same as spend tier |
| Any Amount | CAPEX | Above approvals by spend AND Finance Controller | Fixed asset policy compliance | CFO for ≥ $100k CAPEX |
| Any Amount | Contract deviates from standard terms (indemnity, liability, data) | Above approvals by spend | Legal mandatory | As per spend tier; Legal must sign off on terms |
| Sole Source | >$25k without competition | Above approvals by spend | Sole Source Justification approved by Procurement + Finance | As per spend tier |

Turnaround SLAs (business days): Manager 2; Procurement 2–5; Legal 3–7; IT Security 3–7; Finance Controller 2; CFO 3.

---

## Responsibilities (RACI Summary)

- Requisitioner (R): Define need, gather quotes, create PR, confirm receipt, support exceptions.
- Department Manager/Budget Owner (A): Approve spend, ensure budget availability and coding accuracy.
- Procurement (R/A): Sourcing method, negotiations, PO creation, supplier onboarding coordination.
- Legal (C/A for terms): Contract review, DPAs, NDAs, order forms with non-standard terms.
- IT Security/Risk (C): Security review, privacy impact, vendor risk tiering, insurance/COI.
- Accounts Payable (R): Invoice capture, 3-way match, exception handling, payment execution, GL posting.
- Finance Controller (A/C): Policy compliance, CAPEX classification, high-value approvals.
- CFO/COO (A): Executive approval for ≥ $100k or as policy dictates.
- Vendor (R): Provide quotes, accept PO/contract, deliver, timely invoice referencing PO.

R = Responsible, A = Accountable, C = Consulted.

---

## Controls and Required Documentation by Stage

- PR stage: Quotes or bid tab (if ≥$25k), SOW/spec, budget reference, sole-source form if applicable.
- Vendor onboarding: W-9 (US) or W-8 (non-US), banking details (verified), COI meeting limits, sanctions screening, diversity status (if tracked), tax forms.
- Contract stage: Master agreement or order form; DPA/SCCs (if data); proof of insurance; legal approval memo.
- PO stage: Final scope, pricing, delivery terms, contract reference number.
- Receipt stage: Packing slip, delivery confirmation, services acceptance/milestone sign-off.
- AP stage: Supplier invoice (PO number, line-item detail), exception resolution notes, payment confirmation.
- Audit trail: System-stamped approvals, change logs, user IDs.

Key controls:
- No PO, no pay.
- 3-way match mandatory for inventory and standard buys; 2-way match allowed for specific services (pre-approved categories) with documented acceptance.
- Segregation of duties: Requester cannot approve own PR; AP cannot create and approve vendor master changes.

---

## Timelines and Typical Durations

- Simple purchase (<$5k, no contract): 1–3 business days to PO; Net 30 payment after invoice.
- Moderate buy ($5k–$25k, standard terms): 3–7 business days to PO.
- Complex buy (>$25k, contract/security/legal): 2–6 weeks to PO depending on negotiations and reviews.
- Vendor onboarding: 2–3 business days after complete documents received.

Payment cycles:
- ACH: Weekly on Wednesdays
- Wires: Daily, cut-off 1 PM local
- Checks: By exception, Fridays
- Early-pay discounts: Take if discount yield ≥ company WACC threshold (Finance to compute).

---

## Dependencies and Systems

- Approved budgets and cost centers in ERP
- Vendor master data accuracy and onboarding documents
- Contract templates and clause library maintained by Legal
- Security questionnaires and DPIA templates maintained by IT Security
- AP automation configured for OCR/e-invoice intake and 3-way match
- Sourcing policy thresholds published and reviewed annually

---

## Exceptions and Escalations

- Emergency purchases: Obtain verbal approval from Dept Head and Procurement; follow with PR within 1 business day; CFO approval required if >$25k.
- Retroactive (after-the-fact) POs: Discouraged; requires Finance Controller approval; tracked as policy exceptions.
- Invoice without PO: Return to vendor with instructions to include PO; if valid exception category, AP requires email approval chain and creates a “confirming PO” with Controller sign-off.
- Over-receipt/price overage: >10% variance routes to Procurement and Budget Owner for change order approval.
- Disputed invoices: AP puts on hold; Procurement leads resolution with vendor within 5 business days.

Escalation path:
- Missing approval SLA by >2 days: Notify next-level manager → Procurement Lead → Finance Controller.

---

## KPIs and Reporting

- Cycle time PR-to-PO (median): Target ≤ 5 business days
- First-pass match rate (3-way): Target ≥ 85%
- On-time payment rate: Target ≥ 95% within terms
- % spend under contract: Target ≥ 80%
- Exception rate (invoices without PO): Target ≤ 2%
- Savings captured vs. baseline quote: Tracked by Procurement

---

## References and Templates

Company templates (stored in SharePoint/CLM):
- Purchase Requisition Form (PR) – PR-Template.docx
- Sole Source Justification – SSJ-Form.docx
- Bid Tabulation Worksheet – BidTab.xlsx
- Statement of Work (SOW) Template – SOW-Standard.docx
- Master Services Agreement – MSA-Standard.docx
- Data Processing Addendum – DPA-Standard.docx
- Security Questionnaire (SaaS/IT) – SecQ.xlsx
- Vendor Onboarding Packet – VOP.zip (W-9/W-8, ACH form, COI requirements)
- Receiving/Milestone Acceptance Form – Acceptance.pdf

External references:
- IRS W-9: https://www.irs.gov/forms-pubs/about-form-w-9
- IRS W-8 Series: https://www.irs.gov/forms-pubs/about-form-w-8

---

## Glossary

- PR (Purchase Requisition): Internal request to buy goods/services.
- PO (Purchase Order): External commitment document issued to vendor.
- 3-Way Match: Match among PO, goods receipt, and invoice.
- DPA: Data Processing Addendum (privacy agreement).
- COI: Certificate of Insurance.
- OPEX/CAPEX: Operating vs. Capital expenditures.

---

## Quick Start Checklist (Requester)

- [ ] Confirm budget and GL/cost center
- [ ] Gather quotes (≥2 if >$25k) or complete sole-source form
- [ ] Draft SOW/specs
- [ ] Start vendor onboarding if new supplier
- [ ] Create PR with all attachments and accurate coding
- [ ] Respond to Procurement/Legal/Security questions promptly
- [ ] Receive and record goods/services on delivery

---

## Change Log

- 1.0 (2025-08-23): Initial release with swimlane, approvals matrix, and documentation requirements.