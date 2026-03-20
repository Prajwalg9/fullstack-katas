from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Registration():
    return render_template("registration.html")

@app.route("/welcome", methods=["POST"])
def Welcome():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        phone = request.form.get("phone")
        email = request.form.get("email")
    return render_template("display_details.html",name=name,age=age,phone=phone,email=email)


if __name__ == "__main__":
    app.run(debug=True)