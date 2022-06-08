from flask import Blueprint, render_template, request, flash
from .models import Sites, Servers
from . import db
views = Blueprint('views', __name__)


@views.route('/create-server', methods=['GET', 'POST'])
def createerver():
    return render_template('AddServer.html')


@views.route('/sites-view', methods=['GET'])
def sitesView():
    siteVar = Sites.query.all()
    return render_template('SitesView.html', title="SitesView", siteName=siteVar )


@views.route('/create-aSite', methods=['GET', 'POST'])
def CreateASite():
    Sites= Sites.query(siteName)
    if request.method == 'POST':
        siteName = request.form.get('siteName')
        SysAdminName = request.form.get('SysAdminName')
        SysAdminPhone = request.form.get('SysAdminPhone')
        if len(siteName)< 3:
            flash('Site name must be larger than 3 characters', category='error')
        elif len(SysAdminName)< 2:
            flash('SysAdmin name must be greater than 2 characters', category='error')
        else:
            new_site = Sites(siteName=siteName,SysAdminName= SysAdminName,SysAdminPhone=SysAdminPhone)
            db.session.add(new_site)
            db.session.commit()
    return render_template('AddSite.html', title="AddSite", Sites=Sites)
"""

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