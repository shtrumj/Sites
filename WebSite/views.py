from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/success')
def test():
    return render_template('Success.html')