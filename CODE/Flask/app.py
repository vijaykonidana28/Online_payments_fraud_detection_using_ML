from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/abhi")
def predict():
    return render_template("predict.html")

@app.route("/pred", methods=["POST"])
def pred():

    step = float(request.form["step"])
    amount = float(request.form["amount"])
    oldOrg = float(request.form["oldbalanceOrg"])
    newOrg = float(request.form["newbalanceOrig"])
    oldDest = float(request.form["oldbalanceDest"])
    newDest = float(request.form["newbalanceDest"])

    # -------- RULE BASED CHECK (from dataset behavior) -------- #

    # Check balance consistency
    org_ok = abs((oldOrg - amount) - newOrg) < 1
    dest_ok = abs((oldDest + amount) - newDest) < 1

    if org_ok and dest_ok and amount < 100000:
        result = "is not Fraud"
    else:
        result = "is Fraud"

    return render_template("result.html", pred=result)
if __name__ == "__main__":
    app.run(debug=True)
