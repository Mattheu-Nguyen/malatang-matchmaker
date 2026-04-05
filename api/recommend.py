"""Vercel WSGI app: static SPA from frontend/dist + POST /recommend."""

import os
import sys

from flask import Flask, jsonify, request, send_file, send_from_directory

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from recommendation.engine import get_recommendations  # noqa: E402

DIST = os.path.join(_ROOT, "frontend", "dist")

app = Flask(__name__)


@app.after_request
def _cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


def _handle_recommend():
    if request.method == "OPTIONS":
        return "", 204
    if not request.data:
        return jsonify({"error": "No preferences provided"}), 400
    try:
        preferences = request.get_json(force=True, silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400
    if preferences is None:
        return jsonify({"error": "No preferences provided"}), 400
    try:
        results = get_recommendations(preferences)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/recommend", methods=["POST", "OPTIONS"])
@app.route("/api/recommend", methods=["POST", "OPTIONS"])
def recommend():
    return _handle_recommend()


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(DIST, "index.html")


@app.route("/assets/<path:path>", methods=["GET"])
def dist_assets(path):
    return send_from_directory(os.path.join(DIST, "assets"), path)


@app.route("/<path:path>", methods=["GET"])
def dist_public(path):
    """Root-level files from Vite `public/` (e.g. favicon) and similar."""
    if path.startswith("recommend") or path.startswith("api/"):
        return jsonify({"error": "Method Not Allowed"}), 405
    candidate = os.path.join(DIST, path)
    if os.path.isfile(candidate):
        return send_file(candidate)
    return send_from_directory(DIST, "index.html")
