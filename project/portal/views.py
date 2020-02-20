from flask import render_template, jsonify, request, redirect, Blueprint
from project.models import User, Company, db
from project.forms import CreateUser, UpdateUser, CreateCompany, UpdateCompany

# Blueprint Declaration
portal_bp = Blueprint(
    'portal',
    __name__,
    template_folder='templates'
)

# Portal Routes
@portal_bp.route('/')
def index():
    # --- Only used to insert data into an empty database
    companies = Company.query.all()
    if not companies:
        initial_company = Company('Flask Demo Company', 'Oklahoma City, OK')
        db.session.add(initial_company)
        db.session.commit()
        initial_user = User('Flask Demo User', initial_company.id)
        db.session.add(initial_user)
        db.session.commit()
    # --- End of initial data block - Delete as needed
    return render_template('index.html')

# --- Users
@portal_bp.route('/users')
def users():
    users = User.query.order_by(User.id).all()
    data = {"users": users}
    return render_template('users.html', data=data)

@portal_bp.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = CreateUser(request.form)
    companies = [(c.id, c.company_name) for c in Company.query.all()]
    form.company_id.choices = companies
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.name.data, form.company_id.data)
                db.session.add(new_user)
                db.session.commit()
                return redirect('/users')
            except ValueError: 
                db.session.rollback()    
    users = User.query.order_by(User.id).all()
    data = {"form": form, "users": users, "companies": companies}
    return render_template('users.html', data=data)

@portal_bp.route('/users/update', methods=['GET', 'POST'])
def update_user():
    form = UpdateUser(request.form)
    id_ = request.args.get('id')
    user = User.query.filter_by(id=id_).first()
    form.company_id.choices = [(c.id, c.company_name) for c in Company.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            try:    
                for key, value in form.data.items():
                    if not key == 'csrf_token':
                        if not value == "":
                            setattr(user, key, value)
                            pass
                db.session.commit()
                return redirect('/users')
            except ValueError: 
                db.session.rollback()
    users = User.query.order_by(User.id).all()
    data = {"form": form, "users": users, "user": user}
    return render_template('users.html', data=data)

@portal_bp.route('/users/delete/<id>')
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')


# --- Companies
@portal_bp.route('/companies')
def companies():
    companies = Company.query.order_by(Company.id).all()
    for company in companies:
        company.company_revenue = f"{company.company_revenue:,.2f}" if company.company_revenue else ''
        company.company_address = company.company_address if company.company_address else ''
    data = {"companies": companies}
    return render_template('companies.html', data=data)

@portal_bp.route('/companies/add', methods=['GET', 'POST'])
def add_company():
    form = CreateCompany(request.form)
    companies = Company.query.order_by(Company.id).all()
    if request.method == 'POST':
        print(f"Form Data (Pre Validate): {form.data}")
        if form.validate_on_submit():
            print(f"Form Data (Post Validate): {form.data}")
            try:
                new_company = Company(form.company_name.data, form.company_city.data)
                if not form.company_address.data == '':
                    setattr(new_company, 'company_address', form.company_address.data)
                if not form.company_revenue.data == '':
                    setattr(new_company, 'company_revenue', form.company_revenue.data)
                db.session.add(new_company)
                db.session.commit()
                return redirect('/companies')
            except ValueError: 
                db.session.rollback()    
    for company in companies:
        # This loop formats revenue column with thousand separators
        company.company_revenue = f"{company.company_revenue:,.2f}"
    data = {"form": form, "companies": companies}
    return render_template('companies.html', data=data)

@portal_bp.route('/companies/update', methods=['GET', 'POST'])
def update_company():
    form = UpdateCompany(request.form)
    id_ = request.args.get('id')
    company = Company.query.filter_by(id=id_).first()
    if request.method == 'POST':
        print(form.company_revenue.data)
        if form.validate_on_submit():
            try:    
                for key, value in form.data.items():
                    if not key == 'csrf_token':
                        if not value == "":
                            print(f"Key: {key}, Value: {value}")
                            setattr(company, key, value)
                db.session.commit()
                return redirect('/companies')
            except ValueError: 
                db.session.rollback()
    companies = Company.query.order_by(Company.id).all()
    from copy import copy       # 'copy' is used so the for loop won't
    company = copy(company)     # override the company variable's value
    for c in companies:
        # This loop formats revenue column with thousand separators
        c.company_revenue = f"{c.company_revenue:,.2f}"
    data = {"form": form, "companies": companies, "company": company}
    return render_template('companies.html', data=data)