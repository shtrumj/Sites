from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/create-server', methods=['GET', 'POST'])
def createerver():
    return render_template('AddServer.html')


@views.route('/create-aSite', methods=['GET', 'POST'])
def CreateASite():
    return render_template('AddSite.html')
"""
  if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name  must be grteater than 1 characters.',category='error')
        elif password1 != password2:
            flash('Password don\'t match.',category='error')
        elif len(password1)< 7 :
            flash('Password must be at least 7 characters',category='error')
        else:
            new_user = Users(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account has been Created!',category='success')
            return redirect(url_for('views.test'))"""