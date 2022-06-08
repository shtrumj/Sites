from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    siteName = db.Column(db.String(30))
    SysAdminName = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Servers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SiteName = db.Column(db.String(30))
    serverName = db.Column(db.String(30))
    IPAddress = db.Column(db.String(30))
    OS = db.Column(db.String(30))
    HOST_IP = db.Column(db.String(30))
    Hypervisor_IP = db.Column(db.String(30))
    Hypervisor_ILOM_IP = db.Column(db.String(20))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

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


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))
    sites = db.relationship('Sites')

    def __init__(self, firstName, password, email):
        self.firstName = firstName
        self.email = email
        self.password = password
