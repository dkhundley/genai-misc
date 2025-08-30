# Registration Flow UX & Form Field Map
Version: 1.0  
Owner: Event Marketing Ops  
Last Updated: 2025-08-23

## Overview
Purpose: Define the end-to-end registration experience, including screen flow, required data, conditional logic, payment options, and communications triggers. This document enables Product, Design, Engineering, Marketing Ops, and Support to implement and operate the registration system without additional context.

Scope:
- Single- and group-registration for the “Summit 2025” event (in-person with optional virtual add-on)
- Public, paid registration with promo codes, taxes/VAT, and invoice option
- Integrations: Payment gateway (Stripe), CRM (Salesforce), Marketing Automation (Marketo), Email (SendGrid), SSO (Auth0)

Success KPIs:
- ≥4.6/5 average UX rating post-checkout survey
- ≥70% mobile completion rate
- ≤2% payment decline rate
- ≤10% abandonment from Ticket Selection to Payment
- <24h SLA for invoice approvals

Primary Personas:
- Attendee (new/returning)
- Group Coordinator (registering 2–20 attendees)
- Speaker/Sponsor (pre-verified code unlocks $0 ticket type)

Key Constraints:
- PCI compliance (tokenized payments only; no card storage on our servers)
- GDPR/CCPA compliant consent and data retention
- Accessibility WCAG 2.1 AA

---

## High-Level Registration Journey
Entry Points:
- Event website CTA (Register), email campaigns, paid ads (with UTM), speaker/sponsor portal (code unlock)

User Flow:
1) Landing: Event details + “Register” CTA  
2) Ticket Selection: Choose ticket type/quantity (+ add-ons)  
3) Account: Sign in or create account (SSO)  
4) Attendee Details: Profile/requirements per attendee  
5) Billing & Payment: Billing address, taxes, payment method  
6) Review & Confirm: Final check, terms, pay/submit  
7) Confirmation: Receipt, QR code, calendar invite, next steps

---

## Wireframes (ASCII)

1) Landing (eventsite.com/summit2025)
```
-------------------------------------------------------
| Summit 2025 | Date: Oct 14–16, 2025 | San Diego, CA |
|-----------------------------------------------------|
| Highlights | Agenda | Speakers | Venue | Register →  |
|-----------------------------------------------------|
| Hero: [Register Now]                                 |
| Secondary CTA: [Convince Your Manager PDF]           |
| Footer: Policies | Contact | Language                |
-------------------------------------------------------
```

2) Ticket Selection (…/register/tickets)
```
-------------------------------------------------------
| Select Your Ticket                                   |
|-----------------------------------------------------|
| [ ] General Admission - $995 - In-person             |
| [ ] Virtual Pass - $249                              |
| [ ] Student - $199  (Requires .edu or ID upload)     |
| [ ] Sponsor/Speaker - $0 (Requires code)             |
| Quantity: [ 1 ]  Add Group? [Add another attendee]   |
| Add-ons:                                             |
|   [ ] Workshop A - $199  [i]                         |
|   [ ] Evening Reception - $99                        |
| Promo code: [________]  [Apply]                      |
| [Continue]                                           |
-------------------------------------------------------
```

3) Account (…/register/account)
```
-------------------------------------------------------
| Create Account or Sign In                            |
|-----------------------------------------------------|
| Email: [___________________]                         |
| [Continue]                       [Sign in with Google]|
| Already have an account? [Sign in]                  |
| Consent: [ ] I agree to the Privacy Policy.         |
-------------------------------------------------------
```

4) Attendee Details (…/register/attendees)
```
-------------------------------------------------------
| Attendee 1 Details                                   |
|-----------------------------------------------------|
| First Name [____]  Last Name [____]  Preferred Name |
| Email [____]  Phone [____]                          |
| Company [____]  Job Title [____]                    |
| Country [▼]  State/Region [▼]* conditional           |
| Dietary: [▼]  Accessibility needs: [textarea]       |
| Marketing Opt-in [ ]                                |
| For Student: Upload ID [Upload]                     |
| For Speaker: Session ID [____]                      |
| [Add another attendee]  [Continue]                  |
-------------------------------------------------------
```

5) Billing & Payment (…/register/payment)
```
-------------------------------------------------------
| Billing & Payment                                    |
|-----------------------------------------------------|
| Billing Contact:                                     |
|  Name [____] Email [____]                           |
|  Address [____] City [____] Country [▼] State [▼]*  |
|  Postal Code [____] Company VAT No. [____]* EU only |
| Tax shown: $XX.XX                                    |
| Payment Method:                                      |
|  (•) Credit/Debit Card [Card Element]               |
|  ( ) Apple Pay / Google Pay (if supported)          |
|  ( ) ACH (US)                                        |
|  ( ) Invoice / PO (≥$2,500 or ≥5 tickets)           |
| Invoice Fields: PO No. [____]  Terms [Net 30]       |
| [Review Order]                                      |
-------------------------------------------------------
```

6) Review & Confirm (…/register/review)
```
-------------------------------------------------------
| Review Order                                         |
|-----------------------------------------------------|
| Tickets x Qty | Add-ons | Subtotal | Tax | Total    |
| Attendees: [View/Edit]                               |
| Billing: [View/Edit]                                 |
| Promo code: [ABC10]  -$99                            |
| Terms: [ ] I accept Terms & Code of Conduct          |
| [Pay $1,293.00]                                      |
-------------------------------------------------------
```

7) Confirmation (…/register/confirmation)
```
-------------------------------------------------------
| You're Registered!                                   |
|-----------------------------------------------------|
| Order #: ORD-2025-001234                             |
| Download Receipt | Add to Calendar (.ics)            |
| QR Code for check-in                                 |
| Manage Registration [Link]                           |
| Next steps: Hotel block, Travel tips, Join Slack     |
-------------------------------------------------------
```

---

## Detailed Steps, Fields, and Logic

### 1) Landing
- Purpose: Drive to registration; capture UTMs.
- Data captured:
  - utm_source, utm_medium, utm_campaign, utm_content, referrer, landing_page_url
- Logic:
  - “Register” CTA links to /register/tickets with UTMs persisted via session storage.

### 2) Ticket Selection
- Required:
  - ticket_type (enum: general, virtual, student, sponsor_speaker)
  - quantity (int: 1–20; >1 triggers group flow)
  - selected_add_ons (array of add_on_ids)
  - promo_code (optional)
- Conditional:
  - student ticket: validation later for .edu or ID upload
  - sponsor/speaker: must enter valid unlock code
- Validation:
  - ticket inventory check (real-time seat availability)
  - promo code apply endpoint validates code, discount type (fixed/percent), usage limits, eligibility
- Error states:
  - Sold out → “Join waitlist?”; disables payment steps if selected
  - Invalid or expired promo code → inline error; allow retry

### 3) Account
- Options: SSO (Google/LinkedIn/Auth0) or email-based account create/sign-in
- Required:
  - email (unique; lowercased)
  - privacy consent checkbox (GDPR lawful basis: consent)
- Logic:
  - If existing email: prompt to sign in (passwordless magic link optional)
  - If SSO: prefill profile from OAuth claims where available

### 4) Attendee Details (per attendee)
- Required fields:
  - first_name, last_name (2–50 chars)
  - email (unique per attendee; can match buyer email)
  - company, job_title
  - country (ISO 3166-1 alpha-2)
- Conditional fields:
  - state_province required if country in [US, CA, AU, BR, IN]
  - student_id_upload required OR email domain ends with .edu for student ticket
  - speaker_session_id required if ticket_type = sponsor_speaker
  - accessibility_needs: optional free text; triggers accessibility coordinator notification if provided
  - dietary_preference: enum [none, vegetarian, vegan, kosher, halal, gluten_free, dairy_free, nut_allergy, other]
- Group flow:
  - Up to 20 attendees; progress indicator; add/remove attendee; copy details toggle (for company fields only)
- Duplicate detection:
  - If attendee email already registered for same event: offer “Manage existing registration” instead of new

### 5) Billing & Payment
- Required (billing contact):
  - billing_name, billing_email, billing_address1, city, country, postal_code
  - state_province conditional as above
- Tax/VAT:
  - Tax computed via tax service (Avalara) based on event locale and attendee billing country/state
  - EU VAT: show vat_number when billing_country in EU; validate via VIES; if valid and non-IE (event in IE example), apply reverse charge (0% VAT)
- Payment Methods:
  - Credit/Debit (Stripe Elements)
  - Apple Pay/Google Pay if device/browser supports
  - ACH (US only; plaid/Stripe ACH); 3–5 day settlement; hold ticket but mark “Pending”
  - Invoice/PO if total >= $2,500 or quantity >= 5:
    - Required: company_name, po_number, accounts_payable_email
    - Auto-email PDF invoice; due Net 30; registration status: “Pending Payment”
- Anti-fraud:
  - Address verification (AVS), CVV, 3DS2 challenge for EU/UK
  - Rate limiting: max 5 attempts per 15 minutes per IP

### 6) Review & Confirm
- Required:
  - Accept terms_of_service and code_of_conduct
- Logic:
  - Reprice before charge (server-side) to prevent tampering
  - Lock inventory for 10 minutes on review screen; auto-release if timeout
- Error handling:
  - Payment declined: show reason code, retry options, fallback method

### 7) Confirmation
- Outputs:
  - Order ID, line items, taxes, total, payment status
  - QR code (format: PDF417) containing check-in token (opaque, expiring after event)
  - .ics calendar file with venue and QR code link
- Comms:
  - Email: confirmation + receipt sent to buyer; ticket(s) to attendees
  - For invoice/ACH: “Pending payment” email with instructions
- Post-actions:
  - CRM: create/update Lead/Contact + Campaign Member with status “Registered”
  - MA: add to “Registered” program; schedule reminder emails

---

## Form Field Map (by Section)

Ticket Selection
- ticket_type: enum [general, virtual, student, sponsor_speaker] (required)
- quantity: integer 1–20 (required)
- selected_add_ons: array<add_on_id> (optional)
- unlock_code: string (required if sponsor_speaker)
- promo_code: string (optional)

Account
- account_email: email (required)
- sso_provider: enum [google, linkedin, none] (optional)
- privacy_consent: boolean (required)

Attendee (repeats per attendee)
- first_name: string 2–50 (required)
- last_name: string 2–50 (required)
- preferred_name: string 0–50 (optional)
- email: email (required, unique per attendee per event)
- phone: E.164 string (optional; required for SMS reminders if opted in)
- company: string 2–100 (required)
- job_title: string 2–100 (required)
- country: ISO 3166-1 alpha-2 (required)
- state_province: string (conditional)
- dietary_preference: enum (optional)
- accessibility_needs: string 0–500 (optional; triggers internal alert)
- marketing_opt_in: boolean (optional)
- student_id_upload: file (required if student ticket and no .edu email)
- speaker_session_id: string (required if sponsor_speaker)

Billing & Payment
- billing_name: string (required)
- billing_email: email (required)
- billing_company: string (optional; required for invoice)
- address1/address2/city: string (required except address2)
- country: ISO code (required)
- state_province: string (conditional)
- postal_code: string (required; country-specific regex)
- vat_number: string (conditional EU; VIES validation)
- payment_method: enum [card, apple_pay, google_pay, ach, invoice] (required)
- po_number: string (required if invoice)
- ap_email: email (required if invoice)

Review
- accept_terms: boolean (required)
- accept_code_of_conduct: boolean (required)

---

## JSON Schema (Registration Payload)
Note: Simplified for clarity. Draft-07.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Summit 2025 Registration",
  "type": "object",
  "required": ["order", "attendees", "billing", "consents"],
  "properties": {
    "context": {
      "type": "object",
      "properties": {
        "utm": {
          "type": "object",
          "properties": {
            "source": {"type": "string"},
            "medium": {"type": "string"},
            "campaign": {"type": "string"},
            "content": {"type": "string"}
          },
          "additionalProperties": false
        },
        "referrer": {"type": "string", "format": "uri"}
      },
      "additionalProperties": false
    },
    "order": {
      "type": "object",
      "required": ["ticket_type", "quantity", "add_ons", "currency"],
      "properties": {
        "ticket_type": {"type": "string", "enum": ["general", "virtual", "student", "sponsor_speaker"]},
        "quantity": {"type": "integer", "minimum": 1, "maximum": 20},
        "add_ons": {
          "type": "array",
          "items": {"type": "string", "pattern": "^ADDON_[A-Z0-9_]+$"},
          "uniqueItems": true
        },
        "promo_code": {"type": "string"},
        "unlock_code": {"type": "string"},
        "currency": {"type": "string", "enum": ["USD", "EUR", "GBP"]}
      },
      "additionalProperties": false
    },
    "account": {
      "type": "object",
      "required": ["email", "privacy_consent"],
      "properties": {
        "email": {"type": "string", "format": "email", "maxLength": 254},
        "sso_provider": {"type": "string", "enum": ["google", "linkedin", "none"]},
        "privacy_consent": {"type": "boolean"}
      },
      "additionalProperties": false
    },
    "attendees": {
      "type": "array",
      "minItems": 1,
      "maxItems": 20,
      "items": {
        "type": "object",
        "required": ["first_name", "last_name", "email", "company", "job_title", "country"],
        "properties": {
          "first_name": {"type": "string", "minLength": 2, "maxLength": 50},
          "last_name": {"type": "string", "minLength": 2, "maxLength": 50},
          "preferred_name": {"type": "string", "maxLength": 50},
          "email": {"type": "string", "format": "email", "maxLength": 254},
          "phone": {"type": "string", "pattern": "^\\+?[1-9]\\d{7,14}$"},
          "company": {"type": "string", "minLength": 2, "maxLength": 100},
          "job_title": {"type": "string", "minLength": 2, "maxLength": 100},
          "country": {"type": "string", "pattern": "^[A-Z]{2}$"},
          "state_province": {"type": "string"},
          "dietary_preference": {"type": "string", "enum": ["none","vegetarian","vegan","kosher","halal","gluten_free","dairy_free","nut_allergy","other"]},
          "accessibility_needs": {"type": "string", "maxLength": 500},
          "marketing_opt_in": {"type": "boolean"},
          "student_id_upload": {"type": "string", "format": "uri"}, 
          "speaker_session_id": {"type": "string"}
        },
        "additionalProperties": false
      }
    },
    "billing": {
      "type": "object",
      "required": ["name", "email", "address1", "city", "country", "postal_code", "payment_method"],
      "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "company": {"type": "string"},
        "address1": {"type": "string"},
        "address2": {"type": "string"},
        "city": {"type": "string"},
        "country": {"type": "string", "pattern": "^[A-Z]{2}$"},
        "state_province": {"type": "string"},
        "postal_code": {"type": "string"},
        "vat_number": {"type": "string"},
        "payment_method": {"type": "string", "enum": ["card", "apple_pay", "google_pay", "ach", "invoice"]},
        "po_number": {"type": "string"},
        "ap_email": {"type": "string", "format": "email"}
      },
      "additionalProperties": false
    },
    "consents": {
      "type": "object",
      "required": ["terms", "code_of_conduct"],
      "properties": {
        "terms": {"type": "boolean"},
        "code_of_conduct": {"type": "boolean"}
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

Validation Rules (selected):
- email: RFC 5322 validation and domain MX check (server-side)
- postal_code: country-specific patterns (e.g., US: ^\\d{5}(-\\d{4})?$, CA: ^[A-Za-z]\\d[A-Za-z][ -]?\\d[A-Za-z]\\d$)
- VAT: VIES API response must be “valid”
- student ticket: require (.edu email) OR student_id_upload not null
- sponsor/speaker ticket: unlock_code must map to pre-approved list; lock to email domain if configured
- ACH: lock ticket but status “Pending” until bank settlement event received
- Invoice: status “Pending Payment”; auto-cancel if unpaid after 30 days unless extended

---

## Payment Options and Rules
- Currencies: USD primary; EUR/GBP supported based on billing country
- Taxes:
  - US: state/local tax for event state if applicable to admissions
  - EU: VAT rules; reverse charge where applicable
- Refund Policy:
  - 100% refund until T-30 days, 50% until T-14, no refund after T-14; transfers allowed up to T-3
- Fees:
  - Absorb card processing fees; add $25 fee for invoice payments
- Receipts:
  - Line-itemized PDF receipt via SendGrid templates with tax breakdown and VAT info

---

## Communications Plan
Trigger-Based Emails (SendGrid; transactional):
- Order Confirmation (immediate): to buyer + each attendee
  - Subject: You’re registered for Summit 2025!
  - Includes: Order ID, QR code link, .ics, hotel info, manage link
- Payment Receipt (immediate if paid)
- Pending Payment (invoice/ACH): instructions + due date
- Abandoned Registration (no activity after 30 min on tickets/account): send at +2h with resume link
- Pre-Event Reminders:
  - T-30: Travel/Hotel checklist
  - T-7: Badge QR + agenda highlights
  - T-1: Venue map + check-in instructions
- Post-Event:
  - T+1: Survey link + session recordings (if virtual add-on)
- SMS (optional, if opted-in): T-1 reminder and day-of updates

Calendar Invite (.ics) fields:
- DTSTART: 20251014T090000
- DTEND: 20251016T170000
- LOCATION: San Diego Convention Center, CA
- DESCRIPTION: Include manage-registration URL and QR link

---

## Data Mapping and Integrations
CRM (Salesforce):
- Lead/Contact upsert by email
- Campaign: Summit 2025
  - Member Statuses: Sent, Visited (registered), Attended, No Show
- Custom Fields:
  - Ticket Type, Add-ons, Registration Source (UTM), VAT Number, Payment Status, Invoice Number

Marketing Automation (Marketo):
- Program: Summit 2025 Registration
- Smart Lists: Registered, Pending Payment, Abandoned
- Tokens: {{my.eventDate}}, {{my.manageUrl}}, {{lead.Ticket_Type}}

Payment Gateway (Stripe):
- Customer = buyer email
- PaymentIntent with amount, currency, tax_amount
- Metadata: order_id, ticket_type, quantity, utm_campaign

Email (SendGrid):
- Templates: REG_CONFIRM_2025, RECEIPT_2025, PENDING_PAY_2025, REMINDER_T7, REMINDER_T1
- Dynamic data: names, QR URL, line items

Analytics (GA4 + CDP):
- Events:
  - view_item_list (tickets page), add_to_cart (ticket_type, qty), begin_checkout, add_payment_info (method), purchase (value, tax)
  - form_error (field, error_code)
- UTM persistence: sessionStorage → appended on API calls

---

## Accessibility, Localization, and Performance
- Accessibility:
  - WCAG 2.1 AA: labels, focus states, ARIA for errors, color contrast, keyboard-only navigation
  - Error summaries at top; inline error messages programmatically associated
- Localization:
  - Languages: EN, FR, DE, ES; date/time localized; currency formats by locale
  - Address forms adapt by country (state/postcode order, labels)
- Performance:
  - Lighthouse ≥ 90 on mobile; lazy-load add-on images; client-side input masking; defer non-critical scripts

---

## Edge Cases and Error Handling
- Waitlist:
  - When sold out: “Join Waitlist” flow collects name/email/company; CRM status “Waitlisted”
- Duplicate Registration:
  - If attendee email already registered → show manage link and transfer option
- Name Changes/Transfers:
  - Self-serve until T-3; audit log event REG_TRANSFERRED
- Cancellations/Refunds:
  - Portal supports automated refunds based on policy windows; otherwise manual request workflow
- Timeouts:
  - 10-minute inventory hold; extend on user activity; show countdown; release on expiry
- Compliance:
  - Data retention: anonymize attendee PII after 24 months unless consent for ongoing marketing

---

## Responsibilities
- Product Manager:
  - Owner of scope, acceptance criteria, prioritization, KPIs
- UX/UI Designer:
  - High-fidelity designs; accessible components; localization specs
- Front-End Engineer:
  - Implement screens, validation, analytics events
- Back-End Engineer:
  - APIs, pricing/tax logic, inventory, payment integration, webhooks
- Marketing Ops:
  - CRM/MA mappings, email templates, UTM governance, promo codes
- Finance:
  - Tax config, invoice terms, reconciliation
- Legal/Privacy:
  - Terms, Code of Conduct, consent language, data retention policy
- QA:
  - Test plan, cross-browser/device, payment scenarios, i18n
- Support/Registration Desk:
  - Manage inquiries, transfers, invoices, onsite check-in

---

## Dependencies
- Stripe account with Apple/Google Pay enabled; ACH and 3DS configured
- Avalara (or equivalent) tax integration and EU VAT VIES access
- Auth0 SSO apps (Google, LinkedIn) configured
- SendGrid templates and verified sending domain
- Salesforce and Marketo API credentials and field mappings
- Content: Terms, Code of Conduct, Privacy Policy, Event details
- Domain/SSL for all registration subpaths
- File storage for uploads (e.g., S3 with virus scanning) for student IDs

---

## Implementation Timeline (Example)
- Week 1:
  - Finalize UX flows and copy; define schema; set up environments
- Week 2–3:
  - Front-end build (Tickets, Account, Attendees)
  - Back-end APIs (Orders, Attendees, Pricing/Tax)
- Week 4:
  - Payment methods integration; invoice workflow; ACH webhooks
- Week 5:
  - CRM/MA integration; email templates; analytics events
- Week 6:
  - QA, accessibility audit, localization testing, load testing
- Week 7:
  - UAT with stakeholders; bug bash; go-live checklist
- Week 8:
  - Launch; monitor; rapid fixes; post-launch review

---

## References and Templates

API Endpoints (sample)
- POST /api/orders/price: returns priced cart with taxes/discounts
- POST /api/orders: creates order, locks inventory
- POST /api/payments/intent: creates PaymentIntent; returns client_secret
- POST /api/orders/confirm: finalizes order after successful payment
- GET /api/orders/{order_id}: returns order status

Email Template Variables (REG_CONFIRM_2025)
- {{buyer_name}}
- {{order_id}}
- {{total_amount}}
- {{tickets_summary}}
- {{qr_code_url}}
- {{manage_registration_url}}
- {{event_dates}}
- {{venue_address}}

Abandoned Cart Email (copy sample)
- Subject: Complete your Summit 2025 registration
- Body: Hi {{first_name}}, you’re almost done. Your {{ticket_type}} ticket is reserved for the next 24 hours. Continue here: {{resume_url}}. Need help? {{support_email}}.

Error Messages (examples)
- “This promo code is invalid or has expired.”
- “We couldn’t verify your VAT number. Please check and try again.”
- “State/Province is required for your selected country.”
- “Payment was declined by your bank. Try another method or contact your bank.”

Test Scenarios (QA)
- Ticket inventory: last seat, oversell prevention
- Promo codes: percent, fixed, usage limits, ineligible ticket type
- Student: .edu email accepted; non-.edu requires upload; missing upload blocked
- Sponsor code: invalid/expired; valid but mismatched domain
- Taxes: US taxable vs non-taxable states; EU VAT reverse charge
- Payments: card success, 3DS challenge, decline codes, ACH pending, invoice approval
- Group: 5 attendees with mixed add-ons; per-attendee emails
- Accessibility: keyboard-only flow; screen reader labels; error summaries
- Localization: FR and DE address formats; currency comma/decimal
- Abandoned cart: resume link works; inventory released properly

Sample Manage Registration Features
- View/print receipt
- Update profile/dietary/accessibility
- Transfer ticket to new attendee email (with confirmation)
- Request cancellation (policy-aware)
- Download .ics and QR code

Support Contacts
- Registration Support: reg-support@example.com
- Finance (Invoices): ap@example.com
- Accessibility Coordinator: access@example.com

---

This document provides the detailed UX, data schema, validation logic, payment rules, and operations plan necessary to implement and run the Summit 2025 registration experience end-to-end.