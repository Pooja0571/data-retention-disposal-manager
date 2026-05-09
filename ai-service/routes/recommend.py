# Import Blueprint and request
from flask import Blueprint, request

# Create blueprint
recommend_bp = Blueprint('recommend', __name__)


# Create POST endpoint
@recommend_bp.route('/recommend', methods=['POST'])
def recommend():

    # Read JSON input
    data = request.get_json()

    # Validate request body
    if not data:
        return {"error": "Request body is required"}, 400

    # Extract values
    record_type = data.get("recordType")
    retention_period = data.get("retentionPeriod")
    risk_level = data.get("riskLevel")

    # Validate fields
    if not record_type or not retention_period or not risk_level:
        return {"error": "recordType, retentionPeriod and riskLevel are required"}, 400

    # 🔥 Dynamic logic based on risk level
    if risk_level == "High":
        recommendations = [
            {
                "action_type": "Encrypt",
                "description": f"Encrypt {record_type} to protect sensitive information.",
                "priority": "High"
            },
            {
                "action_type": "Strict Access Control",
                "description": "Limit access to authorized personnel only.",
                "priority": "High"
            },
            {
                "action_type": "Secure Deletion",
                "description": f"Ensure secure deletion after {retention_period}.",
                "priority": "High"
            }
        ]

    elif risk_level == "Medium":
        recommendations = [
            {
                "action_type": "Archive",
                "description": f"Archive {record_type} securely during retention period.",
                "priority": "Medium"
            },
            {
                "action_type": "Periodic Review",
                "description": "Review data regularly for compliance.",
                "priority": "Medium"
            },
            {
                "action_type": "Delete",
                "description": f"Delete data after {retention_period}.",
                "priority": "Low"
            }
        ]

    else:  # Low risk
        recommendations = [
            {
                "action_type": "Store",
                "description": f"Store {record_type} with basic protection.",
                "priority": "Low"
            },
            {
                "action_type": "Minimal Monitoring",
                "description": "Monitor data usage occasionally.",
                "priority": "Low"
            },
            {
                "action_type": "Delete",
                "description": f"Delete data after {retention_period}.",
                "priority": "Low"
            }
        ]

    return recommendations