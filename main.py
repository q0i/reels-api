from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def debug():
    # return exactly what we received
    return jsonify(
        method=request.method,
        content_type=request.headers.get("Content-Type"),
        body=request.get_data(as_text=True),
        url_root=request.url_root
    ), 200

if __name__ == "__main__":
    app.run(debug=True)
