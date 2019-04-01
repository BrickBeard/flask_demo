from flask import render_template, jsonify, request, redirect, Blueprint
from project.models import User, db
from project.forms import CreateUser, UpdateUser

# Blueprint Declaration
portal_bp = Blueprint(
    'portal',
    __name__,
    template_folder='templates'
)

# Portal Routes

@portal_bp.route('/')
def index():
    return render_template('index.html')

@portal_bp.route('/users')
def users():
    users = User.query.order_by(User.id)
    data = {"users": users}
    return render_template('users.html', data=data)

# @portal_bp.route('/api')
# def api():
#     users = User.query.order_by(User.id)
#     users = [user.serialize for user in users]
#     data = {"users": users}
#     return render_template('api.html', data=data)

@portal_bp.route('/users/add', methods=['GET', 'POST'])
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

@portal_bp.route('/users/update', methods=['GET', 'POST'])
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

@portal_bp.route('/users/delete/<id>')
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')