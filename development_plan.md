Development Plan: KC Local SEO Financial Blueprint (Flask Edition)

1. Core Architecture (The Isolated "Clean" Financials)

Integration: To be built as a Flask Blueprint registered at /admin/budget.

Database (Dedicated SQLite/MySQL):

Clean Start: Initialize a fresh database schema specifically for financials to avoid entanglement with main site user data.

Models:

Transaction: id, date, description, amount, category, is_pass_through (Boolean).

TimeEntry: id, date, hours (Decimal/Float), description, project_id.

Project: id, name, monthly_retainer, status (Fixed to 'ACTIVE').

AGI Logic: AGI = Total Revenue - (Sum of Pass-Through Transactions).

2. Phase 1: Blueprint Foundation & Mobile Security

Secure Entry: Protect all /admin/budget routes with the existing site authentication (Founder-only).

Mobile-First Layout: Use a clean, thumb-friendly Tailwind CSS layout.

Manual Entry Ledger: A fast-loading form to log every expense and income item. This is the "Primary Source of Truth."

3. Phase 3: Time Tracking (AppSheet Migration)

Log Hours: A simple decimal input for hours (e.g., 0.5, 1.75).

Active Projects Only: Dropdowns must strictly filter for 'ACTIVE' status projects.

Live AHR Calculation: Show the "Average Hourly Rate" ($Retainer / TotalHours$) for the project immediately upon saving a time entry via HTMX.

4. Phase 4: The "Anxiety-Free" Dashboard

Theme: Neutral palette (Zinc/Slate) to keep things calm. Use Red only for "Danger" zones (Margin < 50%).

KPI Display: - AGI Gauge: The big number.

Delivery Margin: Per-project profitability.

13-Week Cash Forecast: A predictive chart (Chart.js) showing upcoming retainers vs. known software/payroll costs.

5. Phase 5: Kansas Compliance & Asset Tracking

Asset Ledger: Specifically for tracking equipment >$1,500 for the March 15 Personal Property Rendition.

Tax Calendar: A persistent widget showing the next 2026 Kansas deadline (e.g., Mar 16 S-Corp, Apr 15 K-120S).

Software ROI: A view to see which SaaS tools are actually "earning their keep" based on AGI.

6. Phase 6: CSV Import (Flexibility)

Mapping Engine: Allow for uploading CSV statements. Start with a generic mapper for "Date, Desc, Amount" and flag imports as "Pending Review" until a manual is_pass_through check is done.
