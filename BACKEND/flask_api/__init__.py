from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, auth_required
from flask_migrate import Migrate
from flask_security.utils import hash_password, verify_password

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SECURITY_PASSWORD_SALT'] = 'some-arbitrary-salt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Roles and Users models
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Call the function to create roles
def create_roles():
    with app.app_context():
        db.create_all()  # Ensure the database tables are created
        # Create roles if they don't exist
        if not user_datastore.find_role('User'):
            user_datastore.create_role(name='User', description='Regular user role')
        if not user_datastore.find_role('Admin'):
            user_datastore.create_role(name='Admin', description='Administrator role')
        db.session.commit()
create_roles()

@app.route('/user-signup', methods=['POST'])
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


@app.route('/user-login', methods=['POST'])
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


# Admin-specific endpoints
@app.route('/admin/dashboard', methods=['GET'])
@auth_required('token')  # Require authentication for this endpoint
def admin_dashboard():
    return jsonify(message="Welcome to Admin Dashboard")

@app.route('/admin/stats', methods=['GET'])
@auth_required('token')  # Require authentication
def admin_stats():
    return jsonify(message="Admin Stats Page")

if __name__ == '__main__':
    app.run(debug=True)