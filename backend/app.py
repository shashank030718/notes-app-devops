from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "notesdb"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
        connect_timeout=5
    )

# Initialize DB on startup only
def init_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("DB initialized successfully")
    except Exception as e:
        print(f"DB init failed: {e}")

@app.route("/health")
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy", "db": "connected"})
    except Exception as e:
        return jsonify({"status": "healthy", "db": str(e)}), 200

@app.route("/notes", methods=["GET"])
def get_notes():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, content, created_at FROM notes ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([
            {"id": r[0], "title": r[1], "content": r[2], "created_at": str(r[3])}
            for r in rows
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/notes", methods=["POST"])
def create_note():
    try:
        data = request.json
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING id",
            (data["title"], data.get("content", ""))
        )
        note_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": note_id, "message": "Note created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM notes WHERE id = %s", (note_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Note deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
