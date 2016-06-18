from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        state = request.form["state"]
        print(state)
        if state == "on":
            print("ON")
        elif state == "off":
            print("OF")
    return render_template("ledmac.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)