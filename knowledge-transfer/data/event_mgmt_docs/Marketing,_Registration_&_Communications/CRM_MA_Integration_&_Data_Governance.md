# CRM–MA Integration & Data Governance
Topic: Marketing, Registration & Communications

Document type: Integration specification and data dictionary  
Systems: Salesforce (CRM), Adobe Marketo Engage (MA)  
Last updated: 2025-08-23  
Owner: Marketing Operations

## Overview

### Purpose
Define how Salesforce and Marketo integrate to support marketing, event registration, and communications. This specification covers:
- Data mappings between systems
- Sync cadence and triggers
- Consent capture and governance
- Deduplication and identity resolution
- Segmentation rules for marketing and event communications
- Monitoring, security, and responsibilities

### Scope
- Lead/Contact, Account, Campaign, and Campaign Member synchronization
- Custom object: Event Registration
- Email/SMS consent and preference management
- Standard activity data (email sends/opens/clicks, web activity)
- Segmentation used for invites, reminders, and post-event comms

Out of scope
- Billing/ERP integrations
- Deep attribution modeling (beyond basic UTM capture)
- Non-Marketo marketing platforms

### Definitions
- CRM: Salesforce Sales Cloud
- MA: Adobe Marketo Engage
- Person: Lead or Contact (Marketo Person)
- SOT: Source of Truth
- PII: Personally Identifiable Information

---

## Architecture & Data Flow

### Systems & Objects
- Salesforce: Lead, Contact, Account, Campaign, Campaign Member, Task, Custom Object: Event_Registration__c
- Marketo: Person, Company, Program, Program Membership, Custom Object: Event_Registration_c (API name sample)

### Data Flow Summary
1. Inbound lead generation:
   - Web forms (Marketo) capture Person + Consent → Marketo dedup → Immediate sync to Salesforce Lead.
2. CRM updates (e.g., lifecycle stage, ownership):
   - Salesforce updates push to Marketo via Marketo Salesforce Sync user.
3. Event registration:
   - Marketo Programs manage registration and push registration records to Salesforce Event_Registration__c and Campaign Member statuses.
4. Preference center:
   - Marketo preference center writes to Marketo Person fields → syncs to Salesforce (central Consent object fields on Lead/Contact).
5. Activity data:
   - Marketo email activity is retained in Marketo; summarized metrics and key activities are written to Salesforce (Tasks or Activity History as needed).

### Data Flow Diagram (described)
- Source: Web/Form (Marketo) → Marketo Person (Consent captured) → Salesforce Lead (auto-convert per rules) → Account/Contact.
- Source: Salesforce user edits (e.g., Do Not Email) → Marketo Person (suppression).
- Source: Event landing page (Marketo) → Program member status change → Salesforce Campaign Member status + Event Registration record.

---

## Sync Cadence & Triggers

| Object/Field Group | Direction | Frequency | Trigger Logic | SLA |
|---|---|---|---|---|
| Lead/Contact core fields | Bi-directional | Near Real-Time (Marketo SFDC native sync ~5 min) | Field change in either system | <10 min |
| Consent/Preference fields | Bi-directional with CRM as SOT for global flags | Near Real-Time | Preference change, unsubscribe, DOI | <10 min |
| Account fields (Company) | CRM → MA | Near Real-Time | Company/account field change | <10 min |
| Campaigns & Program metadata | Bi-directional (limited) | Hourly | Program-Campaign sync job | <60 min |
| Campaign Members/Program Members | Bi-directional | Near Real-Time | Status change (Invited, Registered, etc.) | <10 min |
| Event Registration (custom object) | MA → CRM (write), CRM → MA (read) | Near Real-Time | Form submit; webhook success | <10 min |
| Activities (email sent/open/click) | MA → CRM (summary only) | Daily batch 02:00 UTC | Daily rollup | <24 hrs |
| UTM & web activity | MA → CRM (Lead/Contact + Campaign) | Near Real-Time | First touch; last touch | <10 min |

Note: Exact sync polling frequency may vary with Marketo SFDC sync; check API limits and backlog.

---

## Identity & Deduplication

### Unique Identifiers
- Primary key: Email (lowercased, trimmed) when present
- Secondary keys: Mobile phone (E.164 normalized), LinkedIn profile URL, CRM External_Id__c
- Cross-system link: Salesforce ID stored on Marketo Person (sfdcLeadId/sfdcContactId) and Marketo Lead ID stored on Salesforce (Marketo_Lead_Id__c)

### Dedup Rules (Marketo)
- Match-on-create:
  - If Email present: exact match on Email → update existing
  - If Email blank: block create; show error on form
- Secondary merge candidate:
  - Email matches OR (Phone E.164 matches AND LastName matches, FirstName initial matches)
- Marketo-to-Salesforce sync prevents duplicate insert when sfdcLeadId/sfdcContactId present

### Dedup Rules (Salesforce)
- Leads: Standard duplicate rule: Email exact match OR (Phone E.164 + LastName exact)
- Contacts: Email exact (required to match) or External_Id__c match
- Automatic lead conversion:
  - If Account exists by Domain (Company_Email_Domain__c) and Contact with same Email exists → attach as Contact (no new Lead)
- Merge policy:
  - Surviving record = most recently updated consent timestamp (Consent_Last_Updated__c), most complete profile (field completeness scoring)
  - Audit merged record IDs in Merge_Log__c

Example:
- John.Smith@example.com fills form twice; once as Smith John. Result: one Person, one Lead → deduped by Email. Latest UTM_Last_Touch overwrites Last_Touch fields; First_Touch fields locked after initial set.

---

## Consent, Preferences & Compliance

### Channels & Fields
- Email consent: Consent_Email_Status__c (values: Opted-In, Opted-Out, Soft-Opt-In, Unknown)
- SMS consent: Consent_SMS_Status__c (Opted-In, Opted-Out, Unknown)
- Phone (voice): Consent_Phone_Status__c (Do Not Call = true/false)
- Lawful basis (GDPR): Lawful_Basis__c (Consent, Contract, Legitimate Interest, N/A)
- Consent timestamps: Consent_Email_Timestamp__c, Consent_Source__c, Consent_Notes__c
- Region for compliance scope: Data_Privacy_Region__c (EU/UK, US, APAC, LATAM)

SOT: Email/SMS consent is mastered in Marketo, except where CRM is updated by Support/Privacy operations—latest timestamp wins.

### Capture Points
- Marketo forms (required checkboxes where legally required)
- Preference center (Marketo landing page with REST update)
- CRM manual updates (logged with reason code)

### Double Opt-In (DOI)
- EU/UK leads: DOI required. Process:
  1) User submits form with consent checkbox
  2) DOI email sent with expiring token (72 hours)
  3) On confirm: Consent_Email_Status__c = Opted-In; Consent_Email_Timestamp__c set; Program success = “DOI Confirmed”
  4) If unconfirmed, remain Soft-Opt-In for 30 days, limited comms (transactional only)

### Suppression Logic
- Do Not Email = true if Consent_Email_Status__c = Opted-Out OR Email_Invalid__c = true OR Hard_Bounce = true OR Global_Suppression__c = true
- Unsubscribes in any system propagate both ways within 10 minutes
- Transactional exceptions tagged with Legal_Basis = Contract and Program.Channel = Transactional

### Retention & Deletion
- Inactive Person (no activity, no opps, no events) for 24 months in EU/UK → anonymize or delete
- Right to be Forgotten: CRM Admin triggers deletion workflow → Marketo API delete + activity purge within 30 days. Audit in Privacy_Request__c

---

## Data Mapping & Dictionary

Key: D = Direction (→ indicates flow), SOT = Source of Truth, Req = Required

### Person / Lead / Contact Core

| Salesforce Field | Marketo Field | Type | D | SOT | Req | Transform | Notes |
|---|---|---|---|---|---|---|---|
| Lead.Email / Contact.Email | Email | Email | Bi | Marketo | Yes | lowercase/trim | Primary dedup key |
| Lead.FirstName / Contact.FirstName | FirstName | Text | Bi | Marketo | Yes | Proper case | |
| Lead.LastName / Contact.LastName | LastName | Text | Bi | Marketo | Yes | Proper case | |
| Lead.Company | Company | Text | Bi | Marketo (create), SFDC (accounted) | Yes (Lead) | n/a | For Contacts, mapped from Account.Name |
| Lead.Phone / Contact.Phone | Phone | Phone | Bi | SFDC | No | E.164 | Secondary dedup |
| Lead.MobilePhone / Contact.MobilePhone | MobilePhone | Phone | Bi | Marketo | No | E.164 | SMS consent related |
| Lead.Title / Contact.Title | Title | Text | Bi | Marketo | No | Normalize | Title normalization list |
| Lead.Country / Contact.MailingCountry | Country | Text | Bi | Marketo | Yes | ISO-3166 name | See normalization rules |
| Lead.State / Contact.MailingState | State | Text | Bi | Marketo | Conditional | ISO-3166-2 (US/CA codes) | |
| Lead.LeadSource | Acquisition_Program_Name | Text | SFDC→MKTO (First Touch), MKTO→SFDC (Last Touch) | Shared | Yes | See UTM mapping | Controlled values |

### Consent & Preferences

| Salesforce Field | Marketo Field | Type | D | SOT | Req | Transform | Notes |
|---|---|---|---|---|---|---|---|
| Lead.DoNotEmail / Contact.HasOptedOutOfEmail | Unsubscribed | Boolean | Bi | Latest timestamp | Yes | n/a | Auto-set from Consent_Email_Status__c |
| Consent_Email_Status__c | ConsentEmailStatus_c | Picklist | Bi | Latest timestamp | Yes | n/a | Values standardized |
| Consent_Email_Timestamp__c | ConsentEmailTimestamp_c | Datetime | Bi | Marketo | Yes | UTC | |
| Consent_SMS_Status__c | ConsentSMSStatus_c | Picklist | Bi | Latest timestamp | No | n/a | |
| Lawful_Basis__c | LawfulBasis_c | Picklist | Bi | Marketo | Yes (EU/UK) | n/a | |
| Preference_Topic_Subscriptions__c (JSON) | TopicSubscriptions_c (JSON) | Text (long) | Bi | Marketo | No | Validate JSON schema v1 | Multi-topic preferences |

### UTM & Web Attribution

| Salesforce Field | Marketo Field | Type | D | SOT | Notes |
|---|---|---|---|---|---|
| UTM_Source_First__c | UTMSourceFirst_c | Text | MKTO→SFDC (first write only) | Marketo | Set once |
| UTM_Source_Last__c | UTMSourceLast_c | Text | MKTO→SFDC | Marketo | Overwrite on new session |
| UTM_Campaign_Last__c | UTMCampaignLast_c | Text | MKTO→SFDC | Marketo | |
| First_Web_Visit_Date__c | First_Web_Visit_Date_c | Date | MKTO→SFDC | Marketo | |

### Account / Company

| Salesforce Field | Marketo Field | Type | D | SOT | Notes |
|---|---|---|---|---|---|
| Account.Id | CompanyId | ID | SFDC→MKTO | SFDC | Link only |
| Account.Name | Company | Text | SFDC→MKTO | SFDC | For Contacts |
| Account.Industry | Industry | Text | SFDC→MKTO | SFDC | Normalize to NAICS group |
| Account.EmployeeCount | EmployeeCount | Number | SFDC→MKTO | SFDC | Bucket in MA |

### Campaigns & Program Membership

| Salesforce Field | Marketo Field | Type | D | SOT | Notes |
|---|---|---|---|---|---|
| Campaign.Id | Program.SFDC Id | ID | Bi | SFDC | Syncs to Program |
| Campaign.Type | Program.Channel | Text | SFDC→MKTO | SFDC | E.g., Event, Webinar |
| Campaign Member.Status | Program Member.Status | Picklist | Bi | MKTO | Mapped statuses below |

### Event Registration (Custom)

| Salesforce Field (Event_Registration__c) | Marketo Field (Event_Registration_c) | Type | D | SOT | Notes |
|---|---|---|---|---|---|
| Name | Name | Text | MKTO→SFDC | MKTO | UUID or composite key |
| Person__c (Lead/Contact lookup) | PersonId | Reference | MKTO→SFDC | MKTO | via SFDC ID |
| Event_Code__c | EventCode_c | Text | MKTO→SFDC | MKTO | e.g., EVT-2025-SUMMIT |
| Registration_Status__c | RegistrationStatus_c | Picklist | Bi | MKTO | Registered/Waitlisted/Cancelled |
| CheckIn_Status__c | CheckInStatus_c | Picklist | Bi | MKTO | Attended/No-show |
| Registration_Date__c | RegistrationDate_c | DateTime | MKTO→SFDC | MKTO | UTC |
| Ticket_Type__c | TicketType_c | Picklist | MKTO→SFDC | MKTO | General/VIP/Speaker |
| Source__c | Source_c | Text | MKTO→SFDC | MKTO | Form name or API |

---

## Campaign & Registration Status Mapping

Canonical statuses for in-person/virtual event Programs/Campaigns:

| Business State | Marketo Program Member Status | Salesforce Campaign Member Status |
|---|---|---|
| Invited | Invited | Sent |
| Registered | Registered | Registered |
| Waitlisted | Waitlisted | Waitlisted |
| Cancelled | Cancelled | Cancelled |
| Attended | Attended | Attended |
| No-Show | No-Show | No-Show |

Rules:
- Only one terminal attendance status (Attended or No-Show)
- Status progression allowed: Invited → Registered → Attended/No-Show or Cancelled
- Changes push within 10 minutes; Salesforce is reporting SOT for pipeline tie-out

---

## Segmentation Rules (Marketing, Registration, Communications)

All segments must include: Do Not Email = false AND Email is not blank AND Deliverability = Valid.

### Global Examples
- Newsletter Eligible:
  - Consent_Email_Status__c in (Opted-In, Soft-Opt-In) AND TopicSubscriptions includes “Newsletter”
- Product Interest: “Event Platform”
  - Inferred from last 6 months web pages containing /event/ OR last 90 days campaign UTMs containing “event”

### Event Lifecycle Segments (for a given Event_Code = EVT-2025-SUMMIT)
- Invitees:
  - Region within event target regions AND Lifecycle_Stage in (Prospect, MQL, Customer) AND Not registered for Event_Code AND Has not received Invite in 30 days
- Registrants:
  - Event Registration where Registration_Status__c = Registered
- Waitlist:
  - Registration_Status__c = Waitlisted
- Reminder-Send 24h:
  - Registration_Status__c = Registered AND Event_Start_Time within next 24 hours AND Not checked in
- Post-Event Follow-up (Attendees):
  - CheckIn_Status__c = Attended AND Received Follow-up = false
- Post-Event Nurture (No-shows):
  - CheckIn_Status__c = No-Show AND Received Follow-up = false
- VIP Track:
  - Ticket_Type__c = VIP OR Account.Tier__c = Tier 1

Example Marketo Smart List (pseudologic) for Registrants:
- Program Status is Registered in Program “EVT-2025-SUMMIT”
- AND Unsubscribed = false
- AND Email Invalid = false

---

## Data Quality & Normalization

- Country normalization: Map user input to ISO-3166 country names. Example: “U.S.” → “United States”
- State codes (US/CA): Convert to 2-letter codes. Example: “California” → “CA”
- Phone normalization: Convert to E.164; block non-numeric characters; infer default country from Country if missing
- Name casing: Proper case on First/Last, preserve all-caps abbreviations (e.g., IBM)
- Title normalization: Map common variants (e.g., “C.E.O”, “Chief Executive Officer”) to “CEO” for analytics
- Disallowed emails: Reject role accounts on gated content (admin@, info@, support@) unless Account exists
- Bounce handling:
  - Hard bounce in Marketo sets Email_Invalid__c = true in SFDC; suppress further sends
  - Soft bounce threshold: 3 consecutive in 30 days → Temp suppress for 14 days
- UTM enforcement: Require at least utm_source, utm_medium on paid channels; drop to “unknown” if missing; log in UTM_Violations__c

---

## Error Handling, Monitoring & SLAs

- Sync backlog alert: If Marketo SFDC sync backlog > 30 minutes → PagerDuty alert to MOPs
- API error retries: 429/5xx retries with exponential backoff up to 5 attempts; dead-letter queue (DLQ) Event_Registration errors to Integration_Failures__c
- Field mapping drift: Nightly job validates field existence and picklist parity; discrepancies create Jira ticket
- Data contract tests: For each deploy, verify:
  - Required fields exist and are visible to sync user
  - Picklist values include required statuses
  - Sample record roundtrip within SLA
- SLAs:
  - Consent changes propagated <10 minutes
  - Registration status updates <10 minutes
  - Daily summaries by 02:00 UTC

---

## Security & Access

- Principle of least privilege:
  - Marketo Sync User (Salesforce): Read/Write on Lead/Contact/Account/Campaign/Campaign Member; R/W on Event_Registration__c; no delete on Accounts
  - Salesforce Integration User (Marketo): Limited to required fields
- API credentials in secure vault (e.g., AWS Secrets Manager); rotation every 90 days
- IP allowlisting for Marketo Callbacks/Webhooks
- Encryption:
  - TLS in transit; platform-level encryption at rest
  - Sensitive fields (MobilePhone) masked in UI for non-privileged roles
- Audit:
  - Field history tracking on consent fields
  - Access logs retained 24 months

---

## Responsibilities

| Role | Responsibilities |
|---|---|
| Marketing Operations (Owner) | Maintain mappings, segments, Marketo Programs, preference center, DOI process; monitor sync and data quality |
| CRM Administrator | Field creation, page layouts, validation rules, duplicate rules, campaign configuration, custom object management |
| Data Privacy Officer | Approve consent language, lawful basis, retention and deletion policies; audit compliance |
| Event Operations | Define Event Codes, ticket types, registration workflows; ensure on-site check-in integration |
| RevOps/Analytics | UTM governance, attribution models, reporting integrity |
| Engineering (Integration) | Webhook endpoints, DLQ processing, monitoring, environment management |
| Support/CS | Update consent upon verbal requests; log reason codes |

RACI: MOPs (R/A), CRM Admin (R), DPO (A), Eng (R), Event Ops (C), RevOps (C), Support (R), Exec Sponsor (I)

---

## Dependencies & Prerequisites

- Approved consent language and privacy policy URLs
- Salesforce fields created and accessible to Marketo Sync User (profile/permission set)
- Marketo fields created with exact API names listed
- Campaign Member Status values configured globally to match table above
- Event_Registration__c object deployed with fields and permissions
- Preference center landing page and DOI email/template approved
- UTM taxonomy published and enforced
- Integration credentials provisioned and stored in vault
- Sandboxes available for end-to-end testing

---

## Change Management

- Versioning: Semantic version on this spec (e.g., v1.3.0); changelog maintained
- RFC required for:
  - New fields, picklist value changes
  - Consent logic changes
  - Dedup rule modifications
- Deployment steps:
  1) Create fields in SFDC Sandbox; grant permissions
  2) Create fields in Marketo; map to SFDC fields
  3) Update sync user profiles/permission sets
  4) Run data contract tests; validate with sample records
  5) Migrate to production during low-traffic window
  6) Monitor backlog and error logs for 24 hours
- Backfill:
  - For new consent fields, backfill from existing Unsubscribed and Email Invalid fields
  - For Event_Registration historical data, bulk upsert using composite keys (Person + Event_Code + Registration_Date)

---

## Example Timelines

- New event launch (e.g., Summit 2025):
  - T-30 days: Create Program/Campaign; configure statuses; open registration
  - T-21 days: First invite segment build and QA
  - T-7 days, T-1 day: Reminders via segments
  - T+1 day: Attendance status sync; send follow-ups by segment
  - T+7 days: Report rollups in Salesforce dashboards

- Consent model update:
  - Week 1: RFC, legal review, sandbox build
  - Week 2: Preference center updates, DOI templates
  - Week 3: Production deploy, backfill, monitoring

---

## References & Templates

- UTM Taxonomy Template (example)
  - utm_source: google, linkedin, email, direct
  - utm_medium: cpc, social, email, referral
  - utm_campaign: EVENT_SUMMIT2025_INVITE, PRODUCT_LAUNCH_Q1
  - utm_content: variant_a, speaker_jane_doe
- Consent Language Snippet (example; legal to approve)
  - “I agree to receive marketing communications by email from [Company]. I can withdraw consent at any time. Privacy Policy: https://example.com/privacy”
- DOI Email Template
  - Subject: “Please confirm your subscription”
  - CTA link with expiring token parameter: https://go.example.com/confirm?token={{token}}
- Preference Center Fields
  - Newsletter, Events & Webinars, Product Updates, Partner Offers (checkboxes; mapped to TopicSubscriptions JSON)
- API Endpoints (Engineering)
  - Marketo → SFDC Sync: Native connector
  - Event Check-in Webhook (optional): POST https://api.example.com/events/checkin
- Dashboards
  - Salesforce: “Event Performance” (Registrations, Attendance, No-show rate), “Email Deliverability” (Hard bounce rate), “Consent Trends”

---

## Appendix: Sample Records

- Person:
  - Email: alex.lee@example.com
  - Consent_Email_Status__c: Opted-In
  - Lawful_Basis__c: Consent
  - UTM_Source_First__c: linkedin
  - UTM_Campaign_Last__c: EVENT_SUMMIT2025_INVITE

- Event Registration:
  - Event_Code__c: EVT-2025-SUMMIT
  - Registration_Status__c: Registered
  - CheckIn_Status__c: Attended
  - Ticket_Type__c: VIP
  - Registration_Date__c: 2025-06-12T14:21:00Z

---

## Key Steps (Implementation Checklist)

1) Provision sync users and IP allowlists  
2) Create/verify all fields in Salesforce and Marketo (names, types, visibility)  
3) Configure Campaign Member Status globally as per mapping  
4) Build Marketo Programs and SFDC Campaigns (one-to-one)  
5) Implement consent fields, DOI flow, and preference center  
6) Configure dedup rules in Salesforce; validate Marketo dedup behavior  
7) Deploy Event_Registration custom object and Marketo custom object; map fields  
8) Set up monitoring: backlog alerts, DLQ handling, field parity tests  
9) QA end-to-end with test leads (opt-in, opt-out, registration, attendance)  
10) Go live; monitor SLAs and error logs for 24–48 hours

This document serves as the operational blueprint for Marketing Operations, CRM Administration, and Engineering to deliver a compliant, reliable integration that supports event marketing, registration, and communications at scale.