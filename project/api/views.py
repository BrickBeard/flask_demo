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