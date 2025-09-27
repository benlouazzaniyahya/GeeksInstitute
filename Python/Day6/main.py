"""
main.py

Flask REST API for managing student records (CRUD).
Run: python main.py
The server runs in debug mode on port 5001 by default.

Author: Your Name
"""
from __future__ import annotations
import os
from typing import Dict, List, Optional, Tuple

from dotenv import load_dotenv
from flask import Flask, jsonify, request, make_response

load_dotenv()  # loads environment variables from .env if present

app = Flask(__name__)

# Use environment variables if provided, otherwise defaults
DEBUG = os.getenv("FLASK_DEBUG", "true").lower() in ("1", "true", "yes")
PORT = int(os.getenv("PORT", "5001"))

# -------------------------
# In-memory data (initial)
# -------------------------
students: List[Dict] = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 20,
        "gender": "male",
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "age": 21,
        "gender": "female",
    },
    {
        "id": 3,
        "name": "Jim Doe",
        "email": "jim.doe@example.com",
        "age": 22,
        "gender": "male",
    },
    {
        "id": 4,
        "name": "Jill Doe",
        "email": "jill.doe@example.com",
        "age": 23,
        "gender": "female",
    },
    {
        "id": 5,
        "name": "Jack Doe",
        "email": "jack.doe@example.com",
        "age": 24,
        "gender": "male",
    },
]


# -------------------------
# Helpers
# -------------------------
def find_student(student_id: int) -> Optional[Dict]:
    """
    Return student dict by id or None if not found.
    """
    return next((s for s in students if s["id"] == student_id), None)


def validate_student_payload(payload: Dict, require_all: bool = True) -> Tuple[bool, str]:
    """
    Validate incoming student payload.

    Args:
        payload: parsed JSON payload
        require_all: if True, all fields must be present (for POST).
                     If False, partial updates allowed (for PUT).

    Returns:
        (is_valid, message)
    """
    required_fields = {"name": str, "email": str, "age": int, "gender": str}
    if not isinstance(payload, dict):
        return False, "Payload must be a JSON object."

    # Check required presence
    if require_all:
        missing = [f for f in required_fields if f not in payload]
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"

    # Type checks for provided fields
    for field, expected_type in required_fields.items():
        if field in payload:
            val = payload[field]
            if expected_type is int:
                # allow numeric strings that can convert to int?
                if not isinstance(val, int):
                    return False, f"Field '{field}' must be an integer."
            else:
                if not isinstance(val, expected_type):
                    return False, f"Field '{field}' must be a string."

    # Basic email validation (very simple)
    if "email" in payload:
        if "@" not in payload["email"] or "." not in payload["email"]:
            return False, "Field 'email' does not appear to be a valid email address."

    # Age sanity check
    if "age" in payload:
        if not (0 < int(payload["age"]) < 150):
            return False, "Field 'age' must be a positive integer less than 150."

    # Gender simple check
    if "gender" in payload:
        if payload["gender"].lower() not in ("male", "female", "other"):
            return False, "Field 'gender' must be 'male', 'female', or 'other'."

    return True, "OK"


def paginate(items: List[Dict], page: int = 1, limit: int = 10) -> Dict:
    """
    Return dict with paginated slice and meta.
    """
    if page < 1:
        page = 1
    if limit < 1:
        limit = 10

    start = (page - 1) * limit
    end = start + limit
    sliced = items[start:end]
    return {"students": sliced, "page": page, "limit": limit, "total": len(items)}


# -------------------------
# API Endpoints
# -------------------------
@app.get("/students")
def get_students():
    """
    GET /students
    Returns paginated list of students.
    Query params:
      - page (int, default=1)
      - limit (int, default=10)
    """
    try:
        page = int(request.args.get("page", 1))
    except ValueError:
        page = 1
    try:
        limit = int(request.args.get("limit", 10))
    except ValueError:
        limit = 10

    data = paginate(students, page=page, limit=limit)
    return jsonify({"students": data["students"], "page": data["page"], "limit": data["limit"], "total": data["total"]}), 200


@app.get("/students/<int:student_id>")
def get_student(student_id: int):
    """
    GET /students/<id>
    Return student object or 404 if not found.
    """
    student = find_student(student_id)
    if not student:
        # Return 200 with null? The spec said "student object or null if not found"
        # But better REST practice: 404. We'll return 404 with JSON error as required.
        return not_found_error(None)
    return jsonify(student), 200


@app.post("/students")
def create_student():
    """
    POST /students
    Create a new student. Expects JSON body with name, email, age, gender.
    Returns created student with assigned id.
    """
    payload = request.get_json(silent=True)
    valid, msg = validate_student_payload(payload, require_all=True)
    if not valid:
        return jsonify({"error": "Invalid payload", "message": msg}), 400

    # generate new id
    new_id = max((s["id"] for s in students), default=0) + 1
    new_student = {
        "id": new_id,
        "name": payload["name"],
        "email": payload["email"],
        "age": int(payload["age"]),
        "gender": payload["gender"].lower(),
    }
    students.append(new_student)
    return jsonify(new_student), 201


@app.put("/students/<int:student_id>")
def update_student(student_id: int):
    """
    PUT /students/<id>
    Update the student with provided id. Expects JSON body (can be partial).
    Returns updated student or 404 if not found.
    """
    student = find_student(student_id)
    if not student:
        return not_found_error(None)

    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid payload", "message": "JSON body required"}), 400

    valid, msg = validate_student_payload(payload, require_all=False)
    if not valid:
        return jsonify({"error": "Invalid payload", "message": msg}), 400

    # apply updates
    if "name" in payload:
        student["name"] = payload["name"]
    if "email" in payload:
        student["email"] = payload["email"]
    if "age" in payload:
        student["age"] = int(payload["age"])
    if "gender" in payload:
        student["gender"] = payload["gender"].lower()

    return jsonify(student), 200


@app.delete("/students/<int:student_id>")
def delete_student(student_id: int):
    """
    DELETE /students/<id>
    Delete and return the deleted student or 404 if not found.
    """
    student = find_student(student_id)
    if not student:
        return not_found_error(None)

    students.remove(student)
    return jsonify(student), 200


# -------------------------
# Error Handlers
# -------------------------
@app.errorhandler(404)
def not_found_error(error):
    """
    Global 404 handler returning JSON.
    """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(Exception)
def global_exception_handler(error):
    """
    Global exception handler. Returns JSON with basic details.
    """
    # In production, avoid returning error details. For this assessment we include message.
    message = str(error)
    return make_response(jsonify({"error": "An error occurred", "message": message}), 500)


# -------------------------
# Run server
# -------------------------
if __name__ == "__main__":
    # Running directly with python main.py
    app.run(debug=DEBUG, port=PORT)
