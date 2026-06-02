from flask import Flask, render_template
import json

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def dashboard():
    with open("data/scan_results.json", "r") as file:
        results = json.load(file)

    return render_template("dashboard.html", results=results)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)