import os
from functools import wraps
from flask import session, redirect, url_for, flash
from decimal import Decimal
from .models import Transaction

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('budget.login'))
        return f(*args, **kwargs)
    return decorated_function

def calculate_agi():
    """AGI (Agency Gross Income): Always subtract 'Pass-Through' expenses before calculating margins."""
    # This is a placeholder for a more complex calculation if needed
    # AGI = Total Revenue - Total Pass-Through

    # Revenue is usually positive transactions, but we should distinguish categories
    # For now, let's assume all transactions are either Income or Expense
    # and AGI = (Sum of Income) - (Sum of Pass-Through Expenses)

    transactions = Transaction.query.all()
    total_income = sum(t.amount for t in transactions if t.amount > 0)
    total_pass_through = sum(abs(t.amount) for t in transactions if t.is_pass_through and t.amount < 0)

    return total_income - total_pass_through

def get_kansas_tax_deadlines():
    return [
        {"date": "Jan 31", "event": "W2/1099 Deadlines"},
        {"date": "Mar 15", "event": "Personal Property Rendition"},
        {"date": "Mar 16", "event": "S-Corp Tax Return"},
        {"date": "Apr 15", "event": "Kansas State Tax"},
    ]
