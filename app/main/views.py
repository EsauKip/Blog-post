from . import main
from flask_login import login_required
from flask import render_template

@main.route('/')
@login_required
def index():


    return render_template('index.html')