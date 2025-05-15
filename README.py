from flask import Flask, render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@localhost/dm'
db = SQLAlchemy(app)

class ClassifiedSubmission(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    classified_website = db.Column(db.String(30), unique=False, nullable=False)
    homepage_url = db.Column(db.String(20), unique=False, nullable=False)
    ad_category = db.Column(db.String(100), unique=False, nullable=False)
    client_page_url = db.Column(db.String(30), unique=False, nullable=False)
    primary_keyword = db.Column(db.String(30), unique=False, nullable=False)
    related_keywords = db.Column(db.String(30), unique=False, nullable=False)
    company_address = db.Column(db.String(30), unique=False, nullable=False)
    ad_title = db.Column(db.String(30), unique=False, nullable=False)
    description = db.Column(db.String(30), unique=False, nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    classified_ad_url = db.Column(db.String(30), unique=False, nullable=False)
    submission_status = db.Column(db.String(30), unique=False, nullable=False)
    live_url = db.Column(db.String(30), unique=False, nullable=False)
    time_taken = db.Column(db.String(30), unique=False, nullable=False)
    time = db.Column(db.String(30), unique=False, nullable=True)
    





@app.route("/", methods=["GET", "POST"])
def form():
    if request.method=='POST':
        name = request.form.get("employee_name")
        classified_website = request.form.get("classified_website")
        homepage_url = request.form.get("homepage_url")
        ad_category = request.form.get("ad_category")
        client_page_url = request.form.get("client_page_url")
        primary_keyword = request.form.get("primary_keyword")
        related_keywords = request.form.get("related_keywords")
        company_address = request.form.get("company_address")
        ad_title = request.form.get("ad_title")
        ad_description = request.form.get("ad_description")
        phone_number = request.form.get("phone_number")
        email=request.form.get('email')
        classified_ad_url = request.form.get("classified_ad_url")
        submission_status = request.form.get("submission_status")
        live_url = request.form.get("live_url")
        time_taken= request.form.get("time_taken")
        
        
        cs=ClassifiedSubmission(username=name,classified_website=classified_website,homepage_url=homepage_url,
                                ad_category=ad_category,client_page_url=client_page_url,primary_keyword=primary_keyword,
                                related_keywords=related_keywords,company_address=company_address,ad_title=ad_title,
                                description=ad_description,phone_no=phone_number,email=email, classified_ad_url=classified_ad_url,submission_status=submission_status,
                                live_url=live_url,time_taken=time_taken,time=datetime.now())
        db.session.add(cs)
        db.session.commit()
        return redirect('/')


    return render_template("form.html")


app.run(debug=True)
