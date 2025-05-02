from flask import Blueprint, jsonify
from .models import Expert, Community
from . import db

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/experts", methods=["GET"])
def get_experts():
    experts = Expert.query.all()
    return jsonify([{"id": e.id, "name": e.name, "expertise": e.expertise} for e in experts])

@api_blueprint.route("/communities", methods=["GET"])
def get_communities():
    communities = Community.query.all()
    return jsonify([{"id": c.id, "name": c.name, "region": c.region} for c in communities])
