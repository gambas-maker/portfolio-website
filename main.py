from flask import Flask, render_template, request
# from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        pass
    return render_template("landing_page.html")

if __name__ == "__main__":
    app.run(debug=True)