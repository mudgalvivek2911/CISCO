from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/MY_LocalDB'
db = SQLAlchemy(app)


class Routers(db.Model):
    '''
    sno, sapid, hostname, loopback, MacAddress
    '''
    sno = db.Column(db.Integer, primary_key=True)
    sapid = db.Column(db.String(80), nullable=False,unique=True)
    host_name = db.Column(db.String(12), nullable=False,unique=True)
    loopback = db.Column(db.String(120), nullable=False,unique=True)
    MacAddress = db.Column(db.String(12), nullable=True,unique=True)



@app.route("/", methods = ['GET', 'POST'])
def router():
    if(request.method=='POST'):
        '''Add entry to the database
            sno, name phone_num, msg, date, email
        '''
        sapid = request.form.get('sapid')
        hostname = request.form.get('hostname')
        loopback = request.form.get('loopback')
        MacAddress = request.form.get('MacAddress')
        entry = Routers(sap_id=sapid, host_name = hostname, loop_back = loopback, Macaddress= MacAddress )
        db.session.add(entry)
        db.session.commit()
    return render_template('add_route.html')

@app.route("/update_route", methods=["POST"])
def update():
    '''
    sno = db.Column(db.Integer, primary_key=True)
    sapid = db.Column(db.String(80), nullable=False,unique=True)
    host_name = db.Column(db.String(12), nullable=False,unique=True)
    loopback = db.Column(db.String(120), nullable=False,unique=True)
    MacAddress = db.Column(db.String(12), nullable=True,unique=True)
    '''
    newsapid = request.form.get("sapid")
    newhostname = request.form.get("hostname")
    newloopback = request.form.get("loopback")
    newMacAddress = request.form.get("MacAddress")
    oldsapid = request.form.get("oldsapid")
    rou = Routers.query.filter_by(sapid=oldsapid).first()
    rou.sapid = newsapid
    rou.host_name = newhostname
    rou.loopback = newloopback
    rou.MacAddress = newMacAddress
    db.session.commit()
    return render_template("/update_routers.html")

@app.route("/delete_route", methods=["POST"])
def delete():
    sap_n = request.form.get("sapid")
    rou = Routers.query.filter_by(sapid=sap_n).first()
    db.session.delete(rou)
    db.session.commit()
    return render_template("/delete_route.html")

app.run(debug=True)