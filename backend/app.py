# =============================================================================
# app.py — Person 2 (Backend Developer)
# =============================================================================
# PURPOSE:
#   This is the main entry point for the Flask web server.
#   Run this file to start the API: python app.py
#   Server will be available at: http://localhost:5000
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# TODO: from flask import Flask
# TODO: from flask_cors import CORS
#       (CORS lets the frontend HTML file talk to this server)
# TODO: from routes.restaurants import restaurants_bp
#       (import the blueprint you'll create in routes/restaurants.py)


# -----------------------------------------------------------------------------
# STEP 1: Create the Flask app
# -----------------------------------------------------------------------------
# TODO: Create the Flask app instance
#   app = Flask(__name__)


# -----------------------------------------------------------------------------
# STEP 2: Enable CORS
# -----------------------------------------------------------------------------
# TODO: Wrap the app with CORS so the browser allows frontend requests
#   CORS(app)


# -----------------------------------------------------------------------------
# STEP 3: Register route blueprints
# -----------------------------------------------------------------------------
# TODO: Register the restaurants blueprint
#   app.register_blueprint(restaurants_bp)
#
# A "blueprint" is just a group of related routes.
# We keep them in separate files to stay organized.


# -----------------------------------------------------------------------------
# STEP 4: Run the server
# -----------------------------------------------------------------------------
# TODO: Add the standard Flask run block at the bottom:
#
#   if __name__ == '__main__':
#       app.run(debug=True, port=5000)
#
# debug=True means Flask will auto-reload when you save changes — very helpful!
# =============================================================================

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

# @app.route("/restaurants")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    print(data)

    # example response
    return jsonify({
        "message": "Data received",
        "your_input": data
    })


if __name__ == "__main__":
    app.run(debug=True)