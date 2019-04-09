from flask import jsonify, Blueprint
from project.models import User, Company


# Blueprint Declaration
v2 = Blueprint(
    'v2',
    __name__
)

# V2 API Endpoints
@v2.route('/companies')
def get_companies():
    company_list = Company.query.order_by(Company.id).all()
    company_list = [company.serialize for company in company_list]
    for company in company_list:
        company['users_count'] = len(User.query.filter_by(company_id=company['id']).all())
        company['company_revenue'] = float(company['company_revenue'])
    return  jsonify(company_list), 200