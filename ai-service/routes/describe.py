from flask import Blueprint, request
from datetime import datetime

# Import cache from extensions (NOT app)
from extensions import cache

describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
@cache.cached(timeout=60,key_prefix=lambda: request.get_data())
def describe():

    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    record_type = data.get("recordType")
    retention_period = data.get("retentionPeriod")
    risk_level = data.get("riskLevel")

    if not record_type or not retention_period or not risk_level:
        return {"error": "Missing fields"}, 400

    try:
        description = (
            f"{record_type} with {risk_level} risk should be securely retained for "
            f"{retention_period} before disposal."
        )

        return {
            "description": description,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }

    except Exception:
        return {
            "description": "AI service unavailable",
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": True
        }