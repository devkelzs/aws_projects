from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        # Simulate DB write
        return f"Appointment booked for {name}"
    return render_template('book.html')
