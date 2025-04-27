from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Feedback, Menu,Complaint


# Create the Blueprint
main = Blueprint('main', __name__)
# Natural weekday order
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Home route
@main.route('/')
def index():
    return render_template('index.html')

# Feedback route
@main.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedback_entry = Feedback(name=name, message=message)
        db.session.add(feedback_entry)
        db.session.commit()
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('main.feedback'))
    return render_template('feedback.html')

@main.route('/menu')
def menu():
    menus = Menu.query.all()
    # sort by our WEEKDAYS list
    menus_sorted = sorted(menus, key=lambda m: WEEKDAYS.index(m.day))
    return render_template('menu.html', menus=menus_sorted)


@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))

    menu_items = Menu.query.all()
    menu_items = sorted(menu_items, key=lambda m: WEEKDAYS.index(m.day))
    
    feedbacks = Feedback.query.all()
    complaints = Complaint.query.all()

    return render_template(
        'admin_dashboard.html',
        menu_items=menu_items,
        feedbacks=feedbacks,
        complaints=complaints
    )


# Add Menu Item route
@main.route('/admin/add-menu', methods=['POST'])
@login_required
def add_menu():
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))  # Redirect if not an admin

    day = request.form['day']
    items = request.form['items']
    
    # Add new menu item to the database
    new_menu_item = Menu(day=day, items=items)
    db.session.add(new_menu_item)
    db.session.commit()

    flash('New menu item added!', 'success')
    return redirect(url_for('main.admin_dashboard'))  # Redirect back to admin dashboard

# Edit Menu Item route
@main.route('/admin/edit-menu/<int:menu_id>', methods=['GET', 'POST'])
@login_required
def edit_menu(menu_id):
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))  # Redirect if not an admin

    menu_item = Menu.query.get_or_404(menu_id)

    if request.method == 'POST':
        menu_item.day = request.form['day']
        menu_item.items = request.form['items']
        
        db.session.commit()
        flash('Menu item updated successfully!', 'success')
        return redirect(url_for('main.admin_dashboard'))
    
    return render_template('edit_menu.html', menu_item=menu_item)

# Delete Menu Item route
@main.route('/admin/delete-menu/<int:menu_id>', methods=['POST'])
@login_required
def delete_menu(menu_id):
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))  # Redirect if not an admin

    menu_item = Menu.query.get_or_404(menu_id)
    db.session.delete(menu_item)
    db.session.commit()

    flash('Menu item deleted!', 'danger')
    return redirect(url_for('main.admin_dashboard'))
@main.route('/complaints', methods=['GET', 'POST'])
@login_required
def complaints():
    if request.method == 'POST':
        room = request.form['room']
        issue = request.form['issue']
        # Create and store the complaint
        c = Complaint(user_id=current_user.id, room=room, issue=issue)
        db.session.add(c)
        db.session.commit()
        flash("Your complaint has been submitted.", "success")
        return redirect(url_for('main.complaints'))

    return render_template('complaints.html')


@main.route('/admin/complaints')
@login_required
def admin_complaints():
    # only admins can view
    if current_user.role != 'admin':
        return redirect(url_for('main.index'))

    complaints = Complaint.query.order_by(Complaint.date_created.desc()).all()
    return render_template('admin_complaints.html', complaints=complaints)