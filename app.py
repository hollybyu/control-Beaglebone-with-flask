from flask import Flask, render_template, request
from bbio import *
app = Flask(__name__)

LED = GPIO1_16
pinMode(LED, OUTPUT)

@app.route("/", methods=["GET", "POST"])
def toggleLED():
    if request.method == "GET":
        return render_template("led.html")
    if request.method == "POST":
        state = request.form["state"]
        if state == "on":
            digitalWrite(LED, HIGH)
        elif state == "off":
            digitalWrite(LED, LOW)
        return render_template("led.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)