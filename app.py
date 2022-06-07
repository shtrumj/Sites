from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import ServersForm
from sqlalchemy.sql import func
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SECRET_KEY'] = "5e3469a40799e919dc6e47ee9d9ea17e"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Servers(db.Model):
    id = db.Column( db.Integer, primary_key=True)
    SiteName = db.Column(db.String(30))
    serverName = db.Column(db.String(30))
    IPAddress = db.Column(db.String(30))
    OS = db.Column(db.String(30))
    HOST_IP = db.Column(db.String(30))
    HOSTType = db.Column(db.String(30))
    HOST_ILOM_IP = db.Column(db.String(20))

    def __init__(self, SiteName, serverName, IPAddress, OS, HOST_IP, HOSTType, HOST_ILOM_IP):
        self.SiteName = SiteName
        self.serverName = serverName
        self.IPAddress = IPAddress
        self.os = OS
        self.HOST_IP = HOST_IP
        self.HOSTType = HOSTType
        self.HOST_ILOM_IP = HOST_ILOM_IP
        

    def __repr__(self):
        return "SiteName: {} Server_Name: {} IP_Address: {} OS: {}".format(self.SiteName, self.serverName,
                                                                           self.IPAddress,
                                                                           self.os)





@app.route('/')
def serverList():  # put application's code here
    return render_template('servers.html', servers=Servers.query
                           )


@app.route('/create', methods= ['GET', 'POST'])
def createserver():
    form = ServersForm()

    if form.validate_on_submit():

        new_reg = Servers(request.form['SiteName'], request.form['serverName'], request.form['IPAddress'], request.form['OS'],\
                          request.form['HOST_IP'], request.form['HOSTType'], request.form['HOST_ILOM_IP'])
        db.session.add(new_reg)
        db.session.commit()

        flash("Registration was succussfull")
        return redirect(url_for('success'))
    return render_template('CreateServer.html', form=form)



@app.route('/serverview')
def results():
    return Servers.query.filter_by(serverName="Exchange").one()


@app.route('/success')
def success():
    return render_template('Success.html')

if __name__ == '__main__':
    app.run()
