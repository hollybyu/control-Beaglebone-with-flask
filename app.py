from flask import Flask, render_template, request
from bbio import *
app = Flask(__name__)

LED = PWMpin # replace with an actual pin
pwmFrequency(LED, freq_hz)

@app.route("/", methods=["GET", "POST"])
def toggleLED():
    if request.method == "POST":
        state = request.form["state"]
        if state == "on":
            analogWrite(LED, 50) #duty cycle = 50%
        elif state == "off":
            pwmDisable(LED)
    return render_template("led.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)