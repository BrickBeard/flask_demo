from flask import render_template, jsonify, request, redirect
import json
from project import app, db
from project.models import User
from project.forms import CreateUser, UpdateUser


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    users = User.query.order_by(User.id)
    data = {"users": users}
    return render_template('users.html', data=data)

@app.route('/api')
def api():
    users = User.query.order_by(User.id)
    users = [user.serialize for user in users]
    data = {"users": users, "json": json}
    return render_template('api.html', data=data)

@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = CreateUser(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.name.data, form.company.data, form.city.data)
                db.session.add(new_user)
                db.session.commit()
                return redirect('/users')
            except ValueError: 
                db.session.rollback()    
    users = User.query.order_by(User.id)
    data = {"form": form, "users": users}
    return render_template('users.html', data=data)

@app.route('/users/update', methods=['GET', 'POST'])
def update_user():
    form = UpdateUser(request.form)
    id_ = request.args.get('id')
    user = User.query.filter_by(id=id_).first()
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
    users = User.query.order_by(User.id)
    data = {"form": form, "users": users, "user": user}
    return render_template('users.html', data=data)

@app.route('/users/delete/<id>')
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')


# API Endpoints

@app.route('/api/users')
def all_users():
    users = User.query.order_by(User.id)
    user_list = [user.serialize for user in users]
    return jsonify(user_list)

@app.route('/api/users/<id>')
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({"error": "user not found"})
    return jsonify(user.serialize)

@app.route('/api/companies')
def get_companies():
    users = User.query.all()
    company_list = {u.company: {"users": []} for u in users}
    for c in company_list.items():
        c_users = User.query.filter_by(company=c[0])
        c[1]['users'] = [user.serialize for user in c_users]
    return jsonify([company_list])