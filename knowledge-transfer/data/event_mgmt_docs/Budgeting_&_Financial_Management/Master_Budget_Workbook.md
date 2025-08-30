# Master Budget Workbook
Comprehensive, itemized budget for events, covering expenses and revenues by category with built‑in version control, scenario analysis, and variance tracking. Delivered as a spreadsheet with tabs for assumptions, line items, and summary dashboards.

## Overview
The Master Budget Workbook (MBW) is the single source of truth for planning, tracking, and reporting the financial performance of an event or event portfolio. It enables:
- Top‑down assumptions (attendance, pricing, sponsor targets, FX rates, tax).
- Bottom‑up line items (venue, catering, production, travel, marketing, staff, etc.).
- Version control (baseline vs reforecast), variance tracking (Budget vs Forecast vs Actual), and audit trail.
- Dashboards that summarize P&L, cash flow timing, unit economics, and break‑even analysis.

Typical users: Event Lead, Finance Business Partner, Procurement, Accounts Payable, Marketing Ops, and Executive Sponsors.

## Workbook Structure (Tabs)
Create the workbook with the following tabs in order. Use short numeric prefixes for readability and to preserve order:

1) 00_ReadMe  
- Purpose, glossary, contact list, last updated date, and change history summary.

2) 01_Assumptions  
- Event metadata, calendar, capacity, pricing, discount assumptions, sponsor tiers, FX, tax rates, contingency %, payment terms.

3) 02_CoA_Map  
- Chart of Accounts (CoA) mapping for every category/line item. Includes department, cost center, GL code, and tax treatment.

4) 03_Revenue  
- Ticketing, sponsorship, exhibitor fees, merchandising, and ancillary revenue. Includes volume, price, fees, and timing.

5) 04_Expense  
- All Opex by category with detailed line items, vendor, quantity, rate, timing, and status (Planned/Proposed/Committed/Invoiced/Paid).

6) 05_Headcount  
- Internal staff time allocation, temporary staffing, contractors; loaded cost assumptions (salary, benefits, payroll tax).

7) 06_Capex (optional)  
- Capitalizable production assets; depreciation assumptions if applicable.

8) 07_Commitments  
- Purchase orders, signed SOWs, and status; links to vendor documents and approval IDs.

9) 08_Actuals_Import  
- Raw actuals from ERP/AP or bank uploads; unmodified import log with date stamps.

10) 09_Variance  
- Automated comparisons Budget vs Forecast vs Actual with variance drivers and commentary fields.

11) 10_Dashboard  
- P&L summary, cash flow curve, unit economics, break‑even chart, KPI tiles.

12) 11_ChangeLog  
- Version history: what changed, who changed it, when, why.

13) 12_Lookups  
- Controlled lists (categories, vendors, statuses, variance codes, currency codes).

## Naming, Versioning, and File Hygiene
- File naming: MasterBudget_[EventName]_[FY]_[vX.Y]_[YYYYMMDD].xlsx (e.g., MasterBudget_Summit2026_FY26_v1.3_20250815.xlsx).
- Versioning: 
  - v1.0 is the baseline (frozen) after executive approval.
  - Increment minor version (v1.1, v1.2…) for reforecasts or structural improvements.
  - Increment major version (v2.0) after material scope changes (>10% revenue or cost impact).
- Change control:
  - Every change to assumptions or formulas must be logged in 11_ChangeLog.
  - Lock formula ranges and protect dashboard/lookup tabs.
- Unique IDs:
  - Assign a persistent LineItemID to every line (e.g., EXP-000123). Do not reuse IDs.

## Key Steps to Set Up and Use the Workbook

1) Initialize the file
- Duplicate the template, rename using the convention, and update 00_ReadMe.
- Confirm tab protection and review data validation lists in 12_Lookups.

2) Populate Assumptions (01_Assumptions)
- Event basics: EventName, City, Venue, StartDate, EndDate.
- Capacity & mix: MaxCapacity, ExpectedAttendance, CompRate%.
- Pricing: TicketTiers (e.g., Super Early, Early, Standard), Price per tier, SalesMix%, Fee% (ticketing and payment).
- Sponsor tiers: Platinum/Gold/Silver packages, list price, target count, expected discount%.
- Taxes & fees: LocalTax% (e.g., 8.5%), VAT/GST where applicable, CateringServiceFee%.
- FX & currency: BaseCurrency (e.g., USD), FX rates (EUR, GBP); set rate dates and hedge assumptions if relevant.
- Payment terms: Deposit%, DueOnSign, Net30/Net45 norms.
- Contingency: Default 10% of direct costs unless contractually mitigated.

3) Map CoA (02_CoA_Map)
- For each category create: CategoryName, Subcategory, Department, CostCenter, GLCode, TaxCode, CapexFlag, AccrualMethod.
- Standard categories (event-focused):
  - Venue & Rentals, Catering & F&B, Production & AV, Staging & Decor, Power/Internet, Security & Safety, Travel & Lodging, Marketing & Creative, Ticketing & Merchant Fees, Staffing (Temp/Contract), Insurance & Permits, Speaker Fees & Honoraria, Swag & Printing, Waste & Sustainability, Contingency.

4) Build Revenue Model (03_Revenue)
- Tickets example columns: LineItemID, Tier, Units, Price, Discount%, NetPrice, Fees%, NetRevenue, RevenueMonth.
- Sponsorship example columns: Tier, ListPrice, Disc%, Units, SignedFlag, BillingMilestones (e.g., 50% on sign, 50% post), CoA.
- Example formulas:
  - NetPrice = Price * (1 - Discount%)
  - Ticket NetRevenue = Units * NetPrice * (1 - Fees%)
  - Sponsorship RecognizedRevenue by month using SUMIFS across BillingMilestones.

5) Build Expense Model (04_Expense)
- Required columns: LineItemID, Category, Subcategory, Vendor, Description, Qty, Unit, UnitCost, Markup/Fees%, LineTotal, Tax%, BudgetMonth, Status, CoA, Notes.
- Example formula:
  - LineTotal = Qty * UnitCost * (1 + Markup/Fees%) * (1 + Tax%)
- Timing:
  - Separate AccrualMonth (recognition) from CashMonth (payment). Use payment terms from 01_Assumptions.

6) Headcount (05_Headcount)
- Columns: Role, FTE, LoadedMonthlyCost, MonthsAllocated, Allocation% to Event, AccrualMonth.
- Example: Event Manager 0.5 FTE, $12,000/month loaded cost, Months 4–7, allocation 50% → Accrual per month = 12,000 * 0.5 = 6,000.

7) Commitments & Actuals (07_Commitments, 08_Actuals_Import)
- 07_Commitments: PO/SOW number, Vendor, Amount, ContractStart/End, PaymentSchedule, ApprovalID, Status.
- 08_Actuals_Import: Paste exports from ERP/AP with Date, Vendor, Invoice#, Amount, CoA, CostCenter; never edit imported rows—use transformation formulas elsewhere.

8) Variance Analysis (09_Variance)
- Columns: LineItemID, Category, Budget, Forecast, Actual, Variance_BvF, Variance_FvA, VarianceReasonCode, Commentary.
- VarianceReasonCodes (examples): Volume, Rate, ScopeChange, Timing, FX, Tax, Credit/Refund, ErrorCorrection.
- Example formulas:
  - Variance_BvF = Forecast - Budget
  - Variance_FvA = Actual - Forecast

9) Dashboards (10_Dashboard)
- KPIs:
  - Gross Revenue, Direct Costs, Gross Margin %, Net Margin %.
  - Cost per Attendee = Total Costs / Attendees.
  - Break-even Attendees = FixedCosts / (AvgTicketNet - VariableCostPerAttendee).
  - Sponsorship Fill = SignedValue / TargetValue.
  - Ticket Sell-through = TicketsSold / Capacity.
  - Cash Burn Curve per month (cumulative).
- Visuals: Monthly P&L bars, cash flow line, funnel for ticket tiers, variance waterfall.

10) Freeze Baseline and Reforecast
- Freeze v1.0 once approved; lock 01_Assumptions and 03–06 totals.
- Reforecast cadence: monthly, plus event milestones (T-12, T-8, T-4, T-2, T-1 weeks).
- Each reforecast increments minor version and logs rationale in 11_ChangeLog.

## Example Data (abbreviated)
Assumptions (01_Assumptions)
- Event: “Global Tech Summit 2026”, San Francisco, 2026-06-10 to 2026-06-12
- Capacity: 4,000; ExpectedAttendance: 3,500; CompRate: 5%
- Ticket tiers:
  - Super Early: $699, 20% of sales
  - Early: $899, 35%
  - Standard: $1,099, 45%
- Ticketing/Merchant Fees: 5.0%; LocalTax: 8.5%
- Sponsorship: Target $2,000,000 gross across 4 Platinum ($250k), 8 Gold ($100k), 20 Silver ($25k), expected blended discount 10%
- Contingency: 10% of direct costs
- FX: Base USD; EUR=1.08, GBP=1.28
- Payment terms: Net30; common deposits 30% on sign

Revenue snapshot (03_Revenue)
- Tickets (3,500 paid, net of 5% fees):
  - Weighted Avg Price ≈ $949
  - Ticket Net Revenue ≈ 3,500 * 949 * (1 - 0.05) ≈ $3,155,000
- Sponsorship (after 10% discount): ≈ $1,800,000
- Total Gross Revenue ≈ $4,955,000

Expense snapshot (04_Expense)
- Venue rental: $420,000 (50% deposit at T-16 weeks, balance T-2)
- Catering: 3,500 attendees * $85 pp = $297,500 + 24% service + 8.5% tax ≈ $400,000
- Production & AV: $750,000 (includes rigging, lighting, labor)
- Security & Safety: $95,000
- Marketing: $350,000 (paid media, creative, email tools)
- Travel & Lodging: $260,000
- Temp staffing: $120,000
- Insurance & permits: $45,000
- Swag & printing: $80,000
- Headcount allocation: $180,000
- Contingency (10% of direct): ≈ $274,000
- Total Costs ≈ $2,974,000
- Indicative Gross Margin ≈ 40%

Break-even
- FixedCosts (excl. variable per attendee items like catering): assume $2,500,000
- VariableCostPerAttendee: $120
- AvgTicketNet (after fees): ≈ $902
- Break-even Attendees ≈ 2,500,000 / (902 - 120) ≈ 3,206 attendees

## Responsibilities (RACI)
- Event Lead (Responsible; Approver on scope assumptions)
  - Owns volume, pricing strategy, sponsor targets, and scope changes.
- Finance Business Partner (Accountable)
  - Owns workbook structure, versioning, variance analytics, and approvals.
- Procurement (Responsible)
  - Updates 07_Commitments; ensures vendor costs align with 04_Expense.
- Accounts Payable/Finance Ops (Responsible)
  - Maintains 08_Actuals_Import; reconciles with ERP; flags mismatches.
- Marketing Ops (Consulted)
  - Provides ticket funnel, conversion forecasts, media spend timing.
- Sales/Sponsorship Lead (Responsible)
  - Updates sponsorship pipeline, signed deals, and billing milestones.
- IT/Data (Consulted)
  - Ticketing and CRM integrations; data governance.
- Executive Sponsor/CFO (Approver)
  - Approves baseline and reforecasts above threshold.

## Governance & Cadence
- Budget build
  - T-20 weeks: Draft v0.9 due (assumptions + first pass of line items).
  - T-16 weeks: Baseline v1.0 submitted for approval.
- Reforecast checkpoints
  - T-12, T-8, T-4, T-2, T-1 weeks; Post-event +30 days true-up.
- Monthly cycle (if multi-month program)
  - M+3 BD: Actuals posted; M+5 BD: Variance report circulated; M+7 BD: Reforecast locked.
- Approval thresholds
  - >$50k line item change or >$100k cumulative change → Executive approval.
  - Scope changes impacting attendee experience require Event Lead and Finance sign-off.

## Variance Tracking & Commentary
- Required field entries when variance exceeds ±5% or ±$10,000 (whichever greater).
- Use standardized VarianceReasonCodes (Volume, Rate, ScopeChange, Timing, FX, Tax, Credit/Refund, ErrorCorrection).
- Include corrective actions and owner with target date.

## Dependencies
- Systems
  - ERP/AP (e.g., NetSuite, SAP) for actuals and CoA.
  - Ticketing platform (Eventbrite, Cvent) for sales volume and fees.
  - CRM (Salesforce, HubSpot) for sponsorship pipeline and invoices.
  - HR/Payroll for loaded cost rates.
  - Contract repository (DocuSign, Ironclad) for POs/SOWs.
  - FX data source (Oanda, ECB) for monthly rates if multi-currency.
- Business milestones
  - Venue contract execution.
  - Production SOW finalization.
  - Sponsor package finalization and rate card.
  - Ticket price phase transitions.
  - Marketing campaign launch dates.

## Data Standards and Controls
- Sign conventions: Revenues positive; costs negative in P&L summary to simplify aggregation. Alternatively, store costs positive and flip signs only in the dashboard—be consistent.
- Data validation: Categories, vendors, statuses, and GL codes must use 12_Lookups lists.
- IDs and references: Each 04_Expense row must reference a 02_CoA_Map GL code; each 07_Commitments row must reference a 04_Expense LineItemID.
- Locked ranges: Protect formulas in 03–06, 09, and 10; only input cells remain editable.
- Audit trail: 11_ChangeLog must capture Date, User, Tab, CellRange, OldValue, NewValue, Reason.

## Scenario Analysis
- Use a Scenario selector in 01_Assumptions: Base, Best, Worst.
- Key drivers to toggle:
  - Attendance ±15%, Conversion rates, Discount rates, Sponsor fill %, Production scope level, FX ±5%.
- Implement with scenario-specific input columns and INDEX/MATCH or CHOOSE to feed 03–06.
- Dashboard displays Base by default with option to switch via a drop-down.

## Cash Flow vs Accrual
- AccrualMonth reflects when value is earned/consumed.
- CashMonth reflects payment timing per Deposit% and Net terms.
- Dashboard includes both P&L (accrual) and monthly cash flow to manage working capital.

## Quality Checks (include on 10_Dashboard or a hidden “Checks” area)
- P&L cross-foot: SUM of detail equals summary totals.
- No orphan records: COUNT of 04_Expense with missing CoA = 0.
- Timing checks: SUM Accrual ≈ SUM Actuals after post-event true-up.
- FX check: Flag if FX date > 30 days old.
- Variance completeness: % of lines with required commentary when thresholds triggered = 100%.

## Example Formulas and Structures
- SUMIFS for category totals:
  - =SUMIFS('04_Expense'!LineTotal,'04_Expense'!Category,"Catering",'04_Expense'!Status,"<>Cancelled")
- Variance:
  - =Forecast - Budget
  - =Actual - Forecast
- Break-even:
  - =FixedCosts / (AvgTicketNet - VariableCostPerAttendee)
- Named ranges:
  - Assump_Attendance, Assump_ContingencyPct, FX_USD_EUR
- Contingency line:
  - =Assump_ContingencyPct * SUMIFS(DirectCostRange, ExcludeCategories, {"Headcount","Capex"})

## Example Line Items (04_Expense, summarized)
- Venue main hall rental: Qty 3 days x $140,000/day = $420,000; Status: Committed; Accrual: Jun; Cash: Feb (30% deposit), May (70%)
- Catering F&B: 3,500 x $85 = $297,500 + svc/tax; Accrual: Jun; Cash: May/Jun
- Production (AV + labor): $750,000; Accrual: Jun; Cash: staggered per SOW
- Marketing Paid Media: $250,000 across Mar–May
- Ticketing fees: 5% of ticket gross; Accrual: upon sale month
- Temp staffing: $120,000; split across May–Jun

## Storage, Access, and Security
- Store in company SharePoint/Drive with restricted access.
- Permissions:
  - Finance, Event Lead: edit
  - Procurement, AP, Marketing Ops: edit their tabs only
  - Executives: view
- Enable file check-in/check-out; avoid simultaneous offline edits.
- Weekly backup copy: MasterBudget_[EventName]_Backup_[YYYYMMDD].xlsx

## References or Templates
- Template file path: [SharePoint]/Finance/Templates/MasterBudgetWorkbook_Template.xlsx
- Data dictionary: [SharePoint]/Finance/Docs/MBW_DataDictionary.docx
- CoA mapping reference: [ERP]/CoA_Export_[YYYYMM].csv
- Ticketing export mapping: [Docs]/Ticketing_To_MBW_Mapping.pdf
- Sample CSV structures:
  - 08_Actuals_Import columns:
    - Date, Vendor, Invoice#, Amount, Currency, CoA, CostCenter, PO#, Memo
  - 07_Commitments columns:
    - PO#/SOW#, Vendor, LineItemID, Description, Amount, Deposit%, SignDate, NetTerms, AccrualMonth, CashMonths, ApprovalID

## Quick Start Checklist
- [ ] Copy template, set version name, fill 00_ReadMe.
- [ ] Complete 01_Assumptions and 02_CoA_Map.
- [ ] Enter revenue model in 03_Revenue and expense lines in 04_Expense.
- [ ] Add headcount allocations in 05_Headcount.
- [ ] Set contingency and verify totals.
- [ ] Freeze baseline v1.0 after approvals.
- [ ] Load commitments and actuals monthly; reconcile variances in 09_Variance.
- [ ] Update dashboard and circulate monthly with commentary.

By following this structure and cadence, any team member can understand the financial posture of the event at a glance, identify risks early, make informed scope decisions, and deliver on revenue and margin targets with transparency and control.