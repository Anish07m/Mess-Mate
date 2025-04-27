from app import create_app
from app.models import db, User
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

# Create the admin user
admin_user = User(
    username='admin',
    email='admin@example.com',
    password=bcrypt.generate_password_hash('admin123').decode('utf-8'),  # Use bcrypt here
    role='admin'  # This gives the user the admin role
)

# Add and commit the admin user to the database
with app.app_context():
    db.session.add(admin_user)
    db.session.commit()

print("✅ Admin user created successfully!")
