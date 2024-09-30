from flask import Blueprint, request, jsonify
from flask_security import auth_required
from flask_api.models import db, User, Role
from flask_api.extensions import user_datastore
from flask_security.utils import hash_password, verify_password

main = Blueprint('main', __name__)

@main.route('/user-signup', methods=['POST'])
def user_signup():
    data = request.json

    # Validate that required fields are present
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify(message="Missing required fields (username, email, or password)"), 400

    # Check if user already exists (by email or username)
    if user_datastore.find_user(email=data['email']):
        return jsonify(message="Email is already registered"), 400
    if user_datastore.find_user(username=data['username']):
        return jsonify(message="Username is already taken"), 400

    # Create user
    try:
        hashed_password = hash_password(data['password'])
        user = user_datastore.create_user(
            username=data['username'], 
            email=data['email'], 
            password=hashed_password,
            active=True,  # New user should be active by default
            fs_uniquifier=data['email']
        )
        user_datastore.add_role_to_user(user, 'User')
        db.session.commit()
        return jsonify(message="User registered successfully"), 201

    except Exception as e:
        db.session.rollback()
        return jsonify(message="An error occurred while registering the user", error=str(e)), 500

@main.route('/user-login', methods=['POST'])
def user_login():
    data = request.json

    # Validate that required fields are present
    if not data.get('username') or not data.get('password'):
        return jsonify(message="Missing required fields (username or password)"), 400

    # Find the user by username
    user = user_datastore.find_user(username=data['username'])
    if not user:
        return jsonify(message="Invalid username or password"), 401

    # Check if the user is active
    if not user.active:
        return jsonify(message="Account is inactive"), 403

    # Verify the password
    if not verify_password(data['password'], user.password):
        return jsonify(message="Invalid username or password"), 401

    # If login is successful, return a success message or token (if using tokens)
    return jsonify(message="User login successful"), 200

@main.route('/admin/dashboard', methods=['GET'])
@auth_required('token')
def admin_dashboard():
    return jsonify(message="Welcome to the admin dashboard"), 200

@main.route('/admin/stats', methods=['GET'])
@auth_required('token')
def admin_stats():
    return jsonify(message="Admin stats"), 200