from flask import jsonify, Blueprint

trips_routes_bp = Blueprint("trop_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"ola":"mundo"}), 200

