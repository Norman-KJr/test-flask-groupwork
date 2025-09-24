from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        
        time = request.form.get('time')
        location = request.form.get('location')
    
        message = 'Waiting time will be shown here'
        
        flash(message)
        
    return render_template('home.html')

