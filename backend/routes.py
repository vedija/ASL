# from flask import Blueprint, jsonify, request
# from models import ASLMapping, db

# api = Blueprint("api", __name__)

# @api.route("/get_asl_video", methods=["GET"])
# def fetch_asl_video():
#     word = request.args.get("word")
#     result = ASLMapping.query.filter_by(word=word).first()

#     if result:
#         return jsonify({"video_url": result.video_url})
#     return jsonify({"error": "No ASL video found"}), 404
