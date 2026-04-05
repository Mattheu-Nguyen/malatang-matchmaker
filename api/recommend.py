"""Vercel WSGI app: POST /recommend only. Static files come from Vercel output (frontend/dist)."""

import os
import sys

from flask import Flask, jsonify, request

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from recommendation.engine import get_recommendations  # noqa: E402

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
    # Do not use request.data — on Vercel it can be empty while the JSON body is still valid.
    preferences = request.get_json(force=True, silent=True)
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
