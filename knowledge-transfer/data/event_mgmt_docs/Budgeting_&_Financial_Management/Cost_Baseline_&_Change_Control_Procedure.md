# Cost Baseline & Change Control Procedure (SOP)

Document ID: FIN-SOP-004  
Version: 1.0  
Effective Date: 2025-09-01  
Owner: PMO Director (Budgeting & Financial Management)  
Applies To: All projects/programs over $100,000 total budget or >90 days duration

---

## 1. Purpose
This SOP establishes how to create, approve, maintain, and change the cost baseline for projects and programs. It defines variance thresholds that trigger action and sets the formal change request and approval process to control budget, forecast, and funding.

## 2. Scope
- New and in-flight projects/programs with a Baseline At Completion (BAC) ≥ $100,000.
- All capital and operating expenditures (CapEx and OpEx).
- All cost categories: labor, subcontractors, materials, travel, and other direct costs (ODC).
- Integrated with scope, schedule, risk, procurement, and finance processes.

## 3. Definitions and Key Concepts
- Cost Baseline: The time-phased, approved budget by WBS element (excludes management reserve). Used to measure and control cost performance.
- BAC (Budget at Completion): Total approved cost baseline.
- Contingency: Budget for identified risks (owned by PM; released via standard CR).
- Management Reserve (MR): Budget for unknowns (owned by Sponsor/Executive; released via elevated approval).
- Control Account: A management control point where scope, budget, actuals, and earned value are integrated.
- EAC: Estimate at Completion = AC + ETC or BAC/CPI (see Section 10).
- ETC: Estimate to Complete = current forecast of remaining costs.
- Variance thresholds: Predefined limits that trigger analysis or a CR (Section 7).

---

## 4. Overview
The cost baseline is established after scope and schedule are approved and before major commitments. It is time-phased monthly and aligned to the Work Breakdown Structure (WBS). Variances are monitored monthly. When thresholds are exceeded or changes are proposed that affect cost, a formal Cost Change Request (CCR) is raised, analyzed, and approved per the approval matrix. Approved changes update the baseline version and downstream systems (PPM, ERP, and procurement).

---

## 5. Roles and Responsibilities
- Project Manager (PM)
  - Develops initial cost estimates and baseline; maintains forecasts and variance analysis.
  - Initiates CCRs; implements approved changes; communicates updates.
- Finance Controller (FC)
  - Validates cost assumptions, rates, capitalization rules; ensures ledger alignment.
  - Co-approves per matrix; updates financial systems.
- PMO Cost Analyst
  - Ensures coding structure, time-phasing, and EV/CPI consistency; maintains baseline register and change log.
- Procurement Lead
  - Aligns POs and change orders to approved baseline; validates vendor pricing and terms.
- Executive Sponsor
  - Approves high-impact changes, MR releases, and scope-driven budget changes.
- Change Control Board (CCB)
  - Cross-functional body (PM, FC, Procurement, Sponsor delegate, Risk Lead) that evaluates and approves mid/high-level CCRs.
- Functional/Delivery Leads
  - Provide impact analysis and revised estimates.
- Risk Lead
  - Confirms contingency drawdown against risk register; updates risk exposure.

RACI note: PM (R/A), FC (A/C), PMO Cost Analyst (C/R), Procurement (C/R), Sponsor (A), CCB (A).

---

## 6. Dependencies and Inputs
- Approved scope baseline and WBS (SOW, charter).
- Integrated master schedule (IMS) with resource-loaded activities.
- Resource plan and rate cards; vendor quotes/proposals.
- Risk register with quantified cost risks (e.g., P-mean or P50).
- Financial policies (capitalization, burden, tax), chart of accounts (CoA).
- Contracts/POs and procurement strategy.
- Tools: PPM (e.g., Smartsheet/Clarity), ERP (e.g., NetSuite/SAP), Timesheet (e.g., Tempo), BI (e.g., Power BI).

---

## 7. Variance Thresholds and Triggers
These thresholds are monitored monthly (and at major milestones). A trigger mandates, at minimum, a variance analysis; some require a CCR per Section 9.

- Work Package Level:
  - Cost variance (CV) > ±10% or ±$5,000 (greater of) in a month → analysis; CCR if forecast impact persists >2 months or affects BAC.
- Control Account Level:
  - Cumulative variance > ±5% or ±$20,000 (greater of) → analysis; CCR if ETC increases or de-scopes.
- Project Level:
  - Forecast EAC exceeds BAC by >3% or >$50,000 (greater of) → CCR required.
  - CPI < 0.90 for 2 consecutive months → CCR required with recovery plan.
- Contingency:
  - Single draw >$25,000 or cumulative use >50% of contingency before 50% project completion → CCR to replenish or rebaseline.
- Management Reserve (MR):
  - Any MR use requires Sponsor approval and CCR.
- Scope/Schedule Trigger:
  - Approved scope change affecting cost any amount → CCR.
  - Schedule extension >20 calendar days with cost impact → CCR.
- Rate/Price Trigger:
  - Labor rate or vendor price increase >3% versus baseline → CCR.

---

## 8. Establishing the Cost Baseline (Procedure)
Target timeline: within 10 business days after scope and schedule approval.

Step 1: Gather Inputs
- Final WBS (level 3–4), IMS, resource plan, rate cards, vendor quotes, risk register, financial policy, and funding constraints.

Step 2: Estimate Costs
- Bottom-up estimate by WBS and cost category (labor hours x loaded rates; vendor quotes; materials; travel).
- Apply taxes, burden/overheads per policy; confirm CapEx vs OpEx split with Finance.

Step 3: Determine Reserves
- Contingency: quantitative risk-based (e.g., P50 of cost risk exposure) or 7–12% of base cost if quantitative not available. Document method.
- MR: set by Sponsor, typically 5–10% of BAC; excluded from cost baseline.

Step 4: Time-Phase the Budget
- Distribute by month aligned to IMS; define fiscal calendar; freeze coding.
- Minimum granularity: monthly; WBS control accounts roll up to project.

Step 5: Create Control Accounts and Coding
- Assign control account managers; set WBS, Org, CoA, and project codes for ERP integration.
- Example coding: PRJ-ACME-23 | WBS 1.2.3 | Cost Cat: Labor | Dept: ENG.

Step 6: Baseline Review and Approval
- PM compiles Baseline Package: narrative assumptions, basis of estimate, time-phased budget, reserve rationale, and alignment to scope/schedule.
- FC validates rates and CapEx/OpEx; PMO checks structure; Sponsor/CCB approves.
- Upon approval: Version the baseline (e.g., BL v1.0), lock in PPM, and sync to ERP.

Example Baseline Summary (Project ACME-Deploy)
- BAC = $2,500,000 (Contingency $200,000 included; MR $150,000 excluded)
  - Labor: $1,350,000 (54%)
  - Subcontractors: $700,000 (28%)
  - Materials: $300,000 (12%)
  - Travel/ODC: $150,000 (6%)
- Time-phasing: 14 months, peak spend months 5–8.
- CPI target: 0.95–1.05; SPI target: 0.95–1.05.

---

## 9. Cost Change Control Procedure
Purpose: To evaluate and implement changes that affect cost baseline, contingency, MR, or forecast.

Trigger: Any item in Section 7 or Sponsor directive.

Service Levels
- Initiation: within 2 business days of trigger detection.
- Triage: within 2 business days by PMO Cost Analyst.
- Impact Analysis: within 5 business days (unless otherwise agreed).
- Decision: within 3 business days of CCB meeting.
- Implementation: within 2 business days of approval.

Steps
1) Identify and Log
- PM/Lead identifies trigger; opens a Cost Change Request (CCR) in PPM; assigns ID (e.g., CCR-2025-017).
- PMO logs in Change Log; classifies type (scope, estimate, rate, contingency draw, MR release, transfer).

2) Triage
- PMO verifies completeness; confirms threshold and routing (see Approval Matrix).

3) Impact Analysis
- PM/Leads quantify impact by WBS and month: base cost, contingency, MR, funding source; schedule impact; risk/quality implications.
- FC validates rates and GL impact; Procurement validates vendor quotes/COs; Risk Lead confirms contingency logic.

4) Review and Decision
- PM presents to approvers/CCB with options and recommendation.
- Approval recorded with conditions (funding source, not-to-exceed, effective date).

5) Implement
- PM updates baseline version (e.g., BL v1.1), ETC/EAC, and control accounts.
- FC updates ERP budgets; Procurement issues PO change orders.
- PMO updates Change Log; communicates to stakeholders; update reports and dashboards.

6) Close and Audit
- Verify implementation in systems; attach evidence (signed CCR, PO CO, ERP screenshot).
- Update lessons learned if impact >$50,000 or >2% BAC.

---

## 10. Calculations and Reporting Standards
- CV = EV − AC; CPI = EV / AC.
- EAC common methods:
  - EAC = AC + ETC (bottom-up)
  - EAC = BAC / CPI (for cost performance trend)
- VAC = BAC − EAC.
- Forecasts updated monthly; variance analysis provided for any threshold breach.

Monthly Financial Package (due by the 5th business day)
- Summary: AC vs Plan, EAC vs BAC, CPI trend.
- Top 5 variances and drivers; mitigation plans.
- CCR status: submitted/approved/rejected; cumulative effect on BAC.

---

## 11. Approval Matrix
Use both amount and percent to determine level; the stricter path applies. All MR usage needs Sponsor approval regardless of amount.

- Up to $10,000 and ≤0.5% of BAC, no scope change:
  - Approver: PM and FC; notify PMO.
- >$10,000 to $50,000 or ≤1% of BAC:
  - Approver: PM, FC, Functional Lead; notify PMO.
- >$50,000 to $250,000 or >1%–5% of BAC:
  - Approver: CCB (PM, FC, Procurement, Risk Lead, Sponsor delegate).
- >$250,000 or >5% of BAC, or any scope baseline change:
  - Approver: Executive Sponsor; CCB recommendation required.
- Any MR release:
  - Approver: Executive Sponsor.
- Labor rate table or financial policy changes (any value):
  - Approver: FC plus Sponsor delegate.
- Schedule slippage >20 days with cost impact:
  - Approver: CCB; Sponsor notified.

Notes
- If funding source is external (grant/client), include Client Representative in approval as required by contract.
- If capitalization is affected, FC must explicitly approve CapEx/OpEx treatment.

---

## 12. Communication and Stakeholder Updates
- After approval, PM issues a Change Notice within 1 business day to: Sponsor, FC, Procurement, Team Leads, Reporting PMO, and Client (if applicable).
- Update RAID log and risk exposure if contingency/MR is used.
- Update dashboards by next reporting cycle.

---

## 13. Audit, Compliance, and Records Retention
- Maintain baseline versions, CCRs, and supporting evidence for 7 years or per contract, whichever is longer.
- Ensure traceability from CCR → baseline version → ERP budget → PO/CO → invoice.
- Unauthorized spend (actuals without approved budget) must be escalated to Sponsor within 2 business days.

---

## 14. KPIs and Continuous Improvement
- CCR cycle time: median ≤10 business days.
- % spend within thresholds: ≥90% of control accounts monthly.
- Rework rate: ≤10% of CCRs requiring re-submission.
- Forecast accuracy: |EAC − AC at completion| ≤5%.
- Audit exceptions: zero material findings.

---

## 15. References
- Scope Control SOP (SCP-SOP-002)
- Schedule Management SOP (SCH-SOP-003)
- Risk Management SOP (RSK-SOP-001)
- Procurement & Contract Change Order SOP (PRC-SOP-006)
- Corporate Financial Policies (capitalization, tax, burden)
- Tool Guides: PPM, ERP, Timesheet, BI

---

## 16. Templates and Forms

A) Cost Baseline Register (minimum fields)
- Project ID and Name
- Baseline Version (e.g., BL v1.0), Effective Date
- BAC (by cost category and total)
- Contingency amount and basis
- MR amount (excluded from BAC)
- Time-phased budget by month (12–24 columns)
- Control Accounts list with owners
- Assumptions and exclusions
- Integration codes (WBS, CoA, cost center, project code)

B) Cost Change Request (CCR) Form
- CCR ID:
- Project ID/Name:
- Requestor and Role:
- Date Submitted:
- Type: [Scope | Estimate Change | Rate/Price Change | Contingency Draw | MR Release | Budget Transfer]
- Description of Change (what, where, why):
- Business Justification (benefits, compliance, risk):
- Affected WBS/Control Accounts:
- Cost Impact Summary:
  - Current Baseline (BAC):
  - Proposed Change (+/−):
  - Use of Contingency: [amount]
  - MR Requested: [amount]
  - Net New Funding Required: [amount]
  - Monthly time-phased impact (next 6 months):
- Schedule Impact (days/milestones):
- Funding Source (budget reallocation, new funds, external client):
- Alternatives Considered:
- Risk/Quality/Compliance Impacts:
- Approvals (names, titles, dates, signatures or e-approvals):
- Implementation Plan (systems to update, owners, due dates):
- Attachments (quotes, BOE, schedule snippet, rate tables)

C) Change Log (tracked by PMO)
- CCR ID, Title
- Submit Date, Status (Open/Approved/Rejected/Implemented)
- Type, Amount, % BAC
- Approver Level (PM/CCB/Sponsor)
- Baseline Version Affected
- ERP/PO references
- Notes

D) Monthly Variance Analysis Note (per control account)
- Plan (current month), Actual, Variance
- ETC update and rationale
- Recovery actions and owners
- Threshold check result

---

## 17. Example Scenario (How to Apply)
Context
- Project ACME-Deploy; BAC $2,500,000 (Contingency $200,000; MR $150,000).
- Vendor notifies 6% price increase for network gear; impact $37,000 over baseline; delivery unchanged.

Action
- Trigger: Rate/Price >3% and amount >$10,000.
- PM opens CCR-2025-017 within 2 business days; attaches vendor letter and revised quote.
- Impact Analysis: $37,000 increase; propose using $25,000 from contingency and $12,000 budget transfer from underspent training line; no schedule impact.
- Approval Path: $37,000 → PM + FC + Functional Lead (per matrix).
- Decision within 3 business days; approved.
- Implementation: Update BL to v1.1; ERP budget adjusted; Procurement issues PO change order; dashboard updated for next cycle.

---

## 18. Quick Checklist (for PMs)
- Do I have approved scope, schedule, rates, and vendor quotes?
- Is the baseline time-phased monthly and coded correctly?
- Have I documented contingency and MR separately?
- Did I review variance thresholds with the team?
- If a threshold is breached, did I submit a CCR within 2 business days?
- After approval, did I update baseline, ERP, POs, and communicate?

---

For questions or training requests, contact the PMO Cost Management team at pmo-costs@company.com.