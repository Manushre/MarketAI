from flask import Flask, render_template, request, jsonify
from agentic import marketing_agent

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    client_name = data.get("client")

    result = marketing_agent(client_name)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)