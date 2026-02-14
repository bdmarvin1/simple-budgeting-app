import os
from flask import render_template, request, redirect, url_for, session, flash, current_app
from werkzeug.security import check_password_hash
from . import budget_bp
from .models import db, Transaction, Project, TimeEntry
from .utils import login_required, calculate_agi, get_kansas_tax_deadlines
from datetime import datetime
from decimal import Decimal

@budget_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        hashed_password = os.environ.get('ADMIN_PASSWORD_HASH')

        if hashed_password and check_password_hash(hashed_password, password):
            session['logged_in'] = True
            return redirect(url_for('budget.dashboard'))
        else:
            flash('Invalid password', 'danger')

    return render_template('budget/login.html')

@budget_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('budget.login'))

@budget_bp.app_context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@budget_bp.route('/')
@login_required
def dashboard():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    agi = calculate_agi()
    deadlines = get_kansas_tax_deadlines()
    projects = Project.query.filter_by(status='ACTIVE').all()

    return render_template(
        'budget/dashboard.html',
        transactions=transactions,
        agi=agi,
        deadlines=deadlines,
        projects=projects,
        now_date=datetime.utcnow().strftime('%Y-%m-%d')
    )

@budget_bp.route('/transactions/add', methods=['POST'])
@login_required
def add_transaction():
    description = request.form.get('description')
    amount_str = request.form.get('amount')
    date_str = request.form.get('date')
    category = request.form.get('category')
    is_pass_through = 'is_pass_through' in request.form

    try:
        amount = Decimal(amount_str)
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        new_transaction = Transaction(
            description=description,
            amount=amount,
            date=date,
            category=category,
            is_pass_through=is_pass_through
        )
        db.session.add(new_transaction)
        db.session.commit()

        if request.headers.get('HX-Request'):
            # Return partial for HTMX
            transactions = Transaction.query.order_by(Transaction.date.desc()).all()
            agi = calculate_agi()
            return render_template('budget/partials/transaction_list.html', transactions=transactions) + \
                   render_template('budget/partials/agi_gauge.html', agi=agi)

        return redirect(url_for('budget.dashboard'))
    except Exception as e:
        db.session.rollback()
        if request.headers.get('HX-Request'):
            return f'<div class="text-red-500">Error: {str(e)}</div>', 400
        flash(f'Error adding transaction: {str(e)}', 'danger')
        return redirect(url_for('budget.dashboard'))

@budget_bp.route('/transactions/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()

    if request.headers.get('HX-Request'):
        transactions = Transaction.query.order_by(Transaction.date.desc()).all()
        agi = calculate_agi()
        return render_template('budget/partials/transaction_list.html', transactions=transactions) + \
               render_template('budget/partials/agi_gauge.html', agi=agi)

    return redirect(url_for('budget.dashboard'))
