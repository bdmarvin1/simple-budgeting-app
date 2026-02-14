# KC Local SEO Financial Blueprint (Flask Edition)

A specialized Flask Blueprint for agency financial tracking, optimized for mobile-first "Anxiety-Free" management.

## Features (Phase 1)
- **Manual Entry Ledger**: Quickly log income and expenses.
- **AGI Calculation**: Automatically calculates Agency Gross Income (Revenue - Pass-Through).
- **Secure Entry**: Protected by password hashing.
- **Kansas Tax Calendar**: Persistent widget for upcoming state deadlines.
- **Mobile First**: Designed for thumb-driven use with Tailwind CSS and HTMX.

## Installation & Integration

### 1. Requirements
Ensure your Flask environment has the following dependencies:
```bash
pip install -r requirements.txt
```

### 2. Integration with Existing Flask App
Copy the `blueprint/` folder into your project and register it in your main application:

```python
from blueprint import budget_bp, db

app = Flask(__name__)
# ... your app config ...

# Initialize DB with your app
db.init_app(app)

# Register the blueprint
app.register_blueprint(budget_bp, url_prefix='/admin/budget')
```

### 3. Environment Setup
Create a `.env` file (or add to your existing one) using the values from `.env.example`:

1.  **Generate a password hash**:
    ```bash
    python hash_password.py your_password
    ```
2.  **Add to `.env`**:
    ```env
    FLASK_SECRET_KEY=your_secret_key
    ADMIN_PASSWORD_HASH=the_hash_you_generated
    DATABASE_URL=sqlite:///budget.db
    ```

## Running Standalone (For Testing)
To test the tool in isolation:
```bash
python run_standalone.py
```
Then visit `http://127.0.0.1:5000/admin/budget`.

## Directory Structure
- `blueprint/`: The core logic, models, and templates.
- `hash_password.py`: Utility to generate the secure password hash.
- `run_standalone.py`: Test runner for local development.
- `requirements.txt`: Necessary Python packages.
