from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DATAAA.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Set a secret key for flashing messages
db = SQLAlchemy(app)


#------------------------------------------------------------------------ tables --------------------------------------------------------
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)


#--------------------------------------------------------------------- contacts -------------------------------------------------------------------

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Create a new Contact object
        new_contact = Contact(name=name, email=email, message=message)
        
        # Add the object to the database
        db.session.add(new_contact)
        db.session.commit()
        
        
        # Fetch all contacts from the database
        contacts = Contact.query.all()
        
        
        return redirect(url_for('index', contacts=contacts))

@app.route('/delete_contact/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('contacts'))



@app.route('/contacts')
def contacts():
    # Fetch all contacts from the database
    contacts = Contact.query.all()
    
    return render_template('contacts.html', contacts=contacts)
   
   
#-------------------------------------------------------------------- login and signup ------------------------------------------------------------------
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin_username = request.form['admin_username']
        admin_password = request.form['admin_password']
        
        # Check if the entered credentials match the hardcoded values
        if admin_username == 'avi' and admin_password == 'avi':
             # Store admin username in the session
            return redirect(url_for('contacts'))  # Redirect to admin dashboard
        else:
            return render_template('adminlogin.html', message='Invalid admin username or password.')
    else:
        return render_template('adminlogin.html')
     
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['txt']
    email = request.form['email']
    password = request.form['pswd']
    reenter_password = request.form['reenter_pswd']

    if password != reenter_password:
        flash("Passwords do not match. Please try again.", 'error')
        return redirect(url_for('login'))

    if User.query.filter_by(email=email).first():
        flash("Email already exists. Please use another email.", 'error')
        return redirect(url_for('login'))

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    flash("Signup successful!", 'success')
    return redirect(url_for('login'))

@app.route('/login2', methods=['POST'])
def login2():
    email = request.form['email']
    password = request.form['pswd']

    user = User.query.filter_by(email=email, password=password).first()

    if user:
        flash("Login successful!", 'success')
        return redirect(url_for('main'))
    else:
        flash("Invalid email or password.", 'error')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

#----------------------------------------------------------------DDD------------------------------------------------------------------------
@app.route('/ddd')
def ddd():
    return render_template('ddd.html')

@app.route('/rd')
def rd():
    return render_template('ddd/rdkit.html')
@app.route('/ad')
def ad():
    return render_template('ddd/autodoc.html')
@app.route('/avg')
def ag():
    return render_template('ddd/Avogadro.html')
@app.route('/bc')
def bc():
    return render_template('ddd/Bioconductor.html')
@app.route('/bp')
def bp():
    return render_template('ddd/Biopython.html')
@app.route('/cd')
def cd():
    return render_template('ddd/ChemDraw.html')
@app.route('/ob')
def ob():
    return render_template('ddd/openBarel.html')
@app.route('/py')
def py():
    return render_template('ddd/PyRx.html')

#-----------------------------------------------------------------------------------CTDA--------------------------------------------------------------
@app.route('/ctda')
def ctda():
    return render_template('ctda.html')

@app.route('/r')
def r():
    return render_template('ctda/R.html')
@app.route('/pnm')
def pnm():
    return render_template('ctda/pnm.html')
@app.route('/oc')
def oc():
    return render_template('ctda/OpenClinica.html')
@app.route('/rc')
def rc():
    return render_template('ctda/REDCap.html')
@app.route('/oe')
def oe():
    return render_template('ctda/OpenEHR.html')
@app.route('/kap')
def kap():
    return render_template('ctda/kap.html')
@app.route('/jn')
def jn():
    return render_template('ctda/jn.html')
@app.route('/o')
def o():
    return render_template('ctda/Oracle.html')
@app.route('/sas')
def sas():
    return render_template('ctda/sas.html')
@app.route('/de')
def de():
    return render_template('ctda/de.html')

#----------------------------------------------------------------  PDS ------------------------------------------------------------------------

@app.route('/pds')
def pds():
    return render_template('pds.html')

@app.route('/agg')
def agg():
    return render_template('pds/ag.html')
@app.route('/ov')
def ov():
    return render_template('pds/ov.html')
@app.route('/oas')
def oas():
    return render_template('pds/oas.html')
@app.route('/vf')
def vf():
    return render_template('pds/vf.html')

#----------------------------------------------------------------  PP ------------------------------------------------------------------------

@app.route('/pp')
def pp():
    return render_template('pp.html')

@app.route('/bm')
def bm():
    return render_template('pp/bm.html')
@app.route('/gp')
def gp():
    return render_template('pp/gp.html')
@app.route('/nn')
def nn():
    return render_template('pp/nn.html')
@app.route('/pw')
def pw():
    return render_template('pp/pw.html')
@app.route('/sc')
def sc():
    return render_template('pp/sc.html')

#----------------------------------------------------------------  DMML ------------------------------------------------------------------------

@app.route('/dmml')
def dmml():
    return render_template('dmml.html')

@app.route('/h2o')
def h2o():
    return render_template('dmml/h2o.html')
@app.route('/orn')
def orn():
    return render_template('dmml/orn.html')
@app.route('/rm')
def rm():
    return render_template('dmml/rm.html')
@app.route('/sl')
def sl():
    return render_template('dmml/sl.html')
@app.route('/ts')
def ts():
    return render_template('dmml/ts.html')
@app.route('/w')
def w():
    return render_template('dmml/w.html')

#----------------------------------------------------------------  TMNLP ------------------------------------------------------------------------

@app.route('/tmnlp')
def tmnlp():
    return render_template('tmnlp.html')

@app.route('/gs')
def gs():
    return render_template('tmnlp/gs.html')
@app.route('/nltk')
def nltk():
    return render_template('tmnlp/nltk.html')
@app.route('/pt')
def pt():
    return render_template('tmnlp/pt.html')
@app.route('/ss')
def ss():
    return render_template('tmnlp/ss.html')
@app.route('/sp')
def sp():
    return render_template('tmnlp/sp.html')
@app.route('/tl')
def tl():
    return render_template('tmnlp/tl.html')

#----------------------------------------------------------------  DM ------------------------------------------------------------------------

@app.route('/dm')
def dm():
    return render_template('dm.html')

@app.route('/apache')
def apache():
    return render_template('dm/apache.html')
@app.route('/couch')
def couch():
    return render_template('dm/couch.html')
@app.route('/mongo')
def mongo():
    return render_template('dm/mongo.html')
@app.route('/mssql')
def mssql():
    return render_template('dm/mssql.html')
@app.route('/mysql')
def mysql():
    return render_template('dm/mysql.html')
@app.route('/neo')
def neo():
    return render_template('dm/neo.html')
@app.route('/post')
def post():
    return render_template('dm/post.html')
@app.route('/sqlite')
def sqlite():
    return render_template('dm/sqlite.html')

#----------------------------------------------------------------  AI TOOLS ------------------------------------------------------------------------

@app.route('/ai')
def ai():
    return render_template('ai/ai.html')



#----------------------------------------------------------------  Plagiarism detectors and Citation softwares ------------------------------------------------------------------------

@app.route('/pc')
def pc():
    return render_template('pc.html')

@app.route('/e')
def e():
    return render_template('cs/e.html')
@app.route('/mrm')
def mrm():
    return render_template('cs/mrm.html')
@app.route('/z')
def z():
    return render_template('cs/z.html')
@app.route('/g')
def g():
    return render_template('pd/g.html')
@app.route('/i')
def i():
    return render_template('pd/i.html')
@app.route('/t')
def t():
    return render_template('pd/t.html')
@app.route('/u')
def u():
    return render_template('pd/u.html')




with app.app_context():
    db.create_all()
    
if __name__ == "__main__":

    app.run(debug=True)

