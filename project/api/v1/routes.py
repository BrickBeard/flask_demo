from flask import jsonify, Blueprint, request
from project.models import User


# Blueprint Declaration
v1 = Blueprint(
    'v1',
    __name__
)

# V1 Endpoints
@v1.route('/users')
def all_users():
    users = User.query.order_by(User.id)
    user_list = [user.serialize for user in users]
    return jsonify(user_list), 200

@v1.route('/user')
def get_user():
    id = request.args.get('id')
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({"error": "user not found"})
    return jsonify(user.serialize), 200