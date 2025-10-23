from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def tip_app():
    final_amount = None

    if request.method == "POST":
        bill = float(request.form["bill"])
        tip = float(request.form["tip"])
        people = float(request.form["people"])
        tip_as_percent = tip / 100
        total_tip_amount = bill * tip_as_percent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 2)

    return render_template("index.html", final_amount=final_amount)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)