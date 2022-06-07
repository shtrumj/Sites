from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servers.sqlite3'
app.config['SECRET_KEY'] = "5e3469a40799e919dc6e47ee9d9ea17e"
db = SQLAlchemy(app)


class Servers(db.Model):
    id = db.Column('server_id', db.Integer, primary_key=True)
    SiteName = db.Column(db.String(30))
    serverName = db.Column(db.String(30))
    IPAddress = db.Column(db.String(30))
    OS = db.Column(db.String(30))
    HOST_IP = db.Column(db.String(30))
    HOSTType = db.Column(db.String(30))
    HOST_ILOM_IP = db.Column(db.String(20))
    Date_Added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return "SiteName: {} Server_Name: {} IP_Address: {} OS: {}".format(self.SiteName, self.serverName,
                                                                           self.IPAddress,
                                                                           self.os)


def __init__(self, SiteName, serverName, IPAddress, OS, HOST_IP, HOSTType, HOST_ILOM_IP, Date_Added):
    self.SiteName = SiteName
    self.serverName = serverName
    self.IPAddress = IPAddress
    self.os = OS
    self.HOST_IP = HOST_IP
    self.HOSTType = HOSTType
    self.HOST_ILOM_IP = HOST_ILOM_IP
    self.Date_Added = Date_Added



@app.route('/')
def serverList():  # put application's code here
    return render_template('servers.html', servers=Servers.query
                           )


@app.route('/create', methods= ['GET', 'POST'])
def createserver():
    if request.method == ['POST']:
        if not request.form['SiteName'] or not request.form['serverName']:
            flash('Please enter all the fields', 'error')
        else:
            serverOB = Servers(request.form['SiteName'], request.form['serverName'], request.form['IPAddress'],
                             request.form['OS'],
                             request.form['HOST_IP'], request.form['HOSTType'], request.form['HOST_ILOM_IP'])
            db.session.add(serverOB)
            db.session.commit()

            flash('Record was successfully Created')
            return redirect(url_for('show_all'))
    return render_template('CreateServer.html')


@app.route('/serverview')
def results():
    return Servers.query.filter_by(serverName="Exchange").one()


if __name__ == '__main__':
    app.run()
