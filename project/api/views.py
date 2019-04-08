from flask import jsonify, render_template, Blueprint
from project.models import User, Company

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


# V1 API Endpoints
@api_bp.route('/users')
def all_users():
    users = User.query.order_by(User.id)
    user_list = [user.serialize for user in users]
    return jsonify(user_list), 200

@api_bp.route('/users/<id>')
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({"error": "user not found"})
    return jsonify(user.serialize), 200

@api_bp.route('/companies')
def get_companies():
    company_list = Company.query.order_by(Company.id).all()
    company_list = [company.serialize for company in company_list]
    for company in company_list:
        company['users_count'] = len(User.query.filter_by(company_id=company['id']).all())
        company['company_revenue'] = float(company['company_revenue'])
    return  jsonify(company_list), 200