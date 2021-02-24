import smtplib
from urllib import request

from flask import Flask, render_template, request

app = Flask(__name__)

clickone = []


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/cosmetic")
def cosmetic():
    return render_template('cosmetic.html')


@app.route("/invis")
def invis():
    return render_template('invis.html')


@app.route("/ortho")
def ortho():
    return render_template('ortho.html')


@app.route("/endo")
def endo():
    return render_template('endo.html')


@app.route("/clickone", )
def clickone():
    return render_template('clickone.html')


@app.route("/clicktwo")
def clicktwo():
    return render_template('clicktwo.html')


@app.route("/book", methods=["GET", "POST"])
def book():
    name = request.book.get("Name")
    email = request.book.get('Email Address')
    date = request.book.get("dd-mm-yyyy")
    message = "your appointment is booked"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("vijeshpoojary84@gmail.com", "PASSWORD")
    server.sendmail("vijeshpoojary84@gmail.com", email, message)

    if not name or not date or not email:
        error_statement = "All forms field required..."
        return render_template(book.html,
                               error_statement=error_statement,
                               name=name,
                               date=date,
                               email=email)

    clickone.append(f"{name} {date} | {email}")
    return render_template('book.html', clickone=clickone)


app.run(debug=True)
