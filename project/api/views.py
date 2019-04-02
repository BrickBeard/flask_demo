from flask import jsonify, render_template, Blueprint
from project.models import User

# Blueprint Declaration
api_bp = Blueprint(
    'api',
    __name__,
    template_folder='templates',
    static_folder='static'
)


# API Page
@api_bp.route('')
def api():
    users = User.query.order_by(User.id)
    users = [user.serialize for user in users]
    data = {"users": users}
    return render_template('api.html', data=data)


# API Endpoints
@api_bp.route('/users')
def all_users():
    users = User.query.order_by(User.id)
    user_list = [user.serialize for user in users]
    return jsonify(user_list)

@api_bp.route('/users/<id>')
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({"error": "user not found"})
    return jsonify(user.serialize)

@api_bp.route('/companies')
def get_companies():
    users = User.query.all()
    company_list = {u.company: {"users_count": 0} for u in users}
    for c in company_list.items():
        c_users = User.query.filter_by(company=c[0])
        c[1]['users_count'] = c_users.count()
    return jsonify([company_list])