from flask import Blueprint, render_template, request, flash
from .models import Sites, Servers, Employees
from . import db
views = Blueprint('views', __name__)


@views.route('/add-server', methods=['GET', 'POST'])
def addServer():
    siteVar= Sites.query.all()
    return render_template('AddServer.html',title="AddServer",sites=siteVar)


@views.route('/sites-view', methods=['GET'])
def sitesView():
    siteVar = Sites.query.all()
    return render_template('SitesView.html', title="SitesView", siteName=siteVar )

@views.route('/create-aSite', methods=['GET', 'POST'])
def CreateASite():
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

@views.route('/Employees', methods=['GET','POST'])
def AddEmployees():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        cellPhone = request.form.get('cellPhone')
        birthDay = request.form.get('birthDay')
        new_employee = Employees(firstName=firstName, lastName=lastName, email=email, cellPhone=cellPhone,birthDay=birthDay)
        db.session.add(new_employee)
        db.session.commit()
    return render_template('AddEmployee.html',title='AddEmployee')