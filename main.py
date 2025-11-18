# main.py  (Railway entry point:  gunicorn main:app)
from flask import Flask, request, send_file, jsonify
import instaloader
import tempfile
import os
import uuid

app = Flask(__name__)

@app.route("/", methods=["POST"])
def download_instagram_video():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "missing url"}), 400

    try:
        L = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        if not post.is_video:
            return jsonify({"error": "post is not a video"}), 400

        tmp = tempfile.mkdtemp()
        L.download_post(post, target=tmp)

        for fname in os.listdir(tmp):
            if fname.endswith(".mp4"):
                return send_file(os.path.join(tmp, fname), as_attachment=True)

        return jsonify({"error": "mp4 not found"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# (optional) health-check
@app.route("/", methods=["GET"])
def health():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
