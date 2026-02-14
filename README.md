# KC Local SEO Financial Blueprint

A dedicated financial management and forecasting tool for KC Local SEO, built as a standalone Flask Blueprint. This tool provides "anxiety-free" financial clarity, focusing on Agency Gross Income (AGI), project profitability, and tax compliance.

## Key Features

### 1. Project Profitability & Time Tracking
- **Live AHR**: Track Average Hourly Rate in real-time as hours are logged.
- **Delivery Margin**: Monitor project health (Revenue vs. Labor Cost).
- **Project Details**: Deep dive into historical transactions and recurring templates for every client.

### 2. Financial Forecasting
- **13-Week Cash Forecast**: A rolling Chart.js visualization of projected cash flow.
- **Recurring Transactions**: Set up templates (Software, Payroll, Retainers) that automatically populate the ledger on their due date.
- **AGI Gauge**: Real-time tracking of Agency Gross Income (Total Revenue minus Pass-Throughs).

### 3. Compliance & ROI
- **Kansas Property Tax**: Asset ledger that flags items exceeding the $1,500 threshold for personal property rendition.
- **Tax Deadlines**: Countdown to critical dates (W2/1099, Property Rendition).
- **Software ROI**: Link SaaS expenses to projects to analyze spend efficiency relative to supported AGI.

### 4. Data Entry & UX
- **CSV Import**: Bulk upload transactions with a manual review/categorization stage.
- **Mobile First**: Zinc/Slate/Neutral color palette optimized for thumb-driven use.
- **HTMX Powered**: Seamless, no-refresh interactions for all data entry.

## Tech Stack
- **Backend**: Flask, SQLAlchemy (SQLite)
- **Frontend**: Tailwind CSS, HTMX, Jinja2, Chart.js
- **Security**: Werkzeug password hashing, environment-based configuration.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r budget_tool/requirements.txt
   ```

2. **Configuration**:
   Copy `.env.example` to `.env` and set your `FLASK_SECRET_KEY` and `ADMIN_PASSWORD_HASH`.
   You can generate a password hash using:
   ```bash
   python budget_tool/hash_password.py yourpassword
   ```

3. **Initialize Database**:
   The database will be automatically initialized on first run.

4. **Run Application**:
   To run as a standalone service:
   ```bash
   python budget_tool/run_standalone.py
   ```
   Access the dashboard at `http://127.0.0.1:5000/admin/budget`.

## Development Logic
- **Signage**: Income is always stored and displayed as positive (+). Expenses (Payroll, Software, etc.) are stored as negative (-) but displayed with absolute values and appropriate coloring (Zinc/Black).
- **Pass-Throughs**: Expenses flagged as "Pass-Through" are deducted from Total Revenue to calculate AGI.
- **Assets**: Kansas-specific logic flags any individual asset with a value > $1,500.
