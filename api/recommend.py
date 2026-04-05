"""Vercel serverless handler for POST /api/recommend (also routed as /recommend via vercel.json)."""

from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Project root (parent of /api)
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from recommendation.engine import get_recommendations  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Quieter logs on Vercel
        pass

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b""
            if not raw:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self._cors_headers()
                self.end_headers()
                self.wfile.write(
                    json.dumps({"error": "No preferences provided"}).encode("utf-8")
                )
                return

            preferences = json.loads(raw.decode("utf-8"))
            results = get_recommendations(preferences)
            body = json.dumps(results).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.end_headers()
            self.wfile.write(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.end_headers()
            self.wfile.write(
                json.dumps({"error": "Invalid JSON body"}).encode("utf-8")
            )
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self._cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
