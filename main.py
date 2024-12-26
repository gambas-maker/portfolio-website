from flask import Flask, render_template, request
# from mail import mail, Message, Config
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app=app)

@app.route('/', methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        msg = Message(
            sender= request.form.get("email"),
            subject= request.form.get("title"),
            body= request.form.get("message"),
            reply_to=request.form.get('email'),
            recipients=['guibaud.clement@gmail.com']
        )
        mail.send(msg)
        print('Mail sent succesfully!')
    return render_template("landing_page.html")

@app.route('/webhook', methods=["GET", "POST"])
def webhook():
    return render_template("")

if __name__ == "__main__":
    app.run(debug=True)