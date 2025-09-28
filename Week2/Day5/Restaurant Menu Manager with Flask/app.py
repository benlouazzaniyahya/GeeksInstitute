# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()  # loads .env if present

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret-change-me")

DATABASE_URL = os.getenv("DATABASE_URL")  # ex: postgresql://user:pass@host:5432/dbname

def get_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL env var not set. Example: postgresql://user:pass@localhost:5432/restaurant_db")
    return psycopg2.connect(DATABASE_URL)


@app.route("/")
def home():
    return redirect(url_for("show_menu"))


@app.route("/menu")
def show_menu():
    """Show all menu items."""
    try:
        with get_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items ORDER BY item_id;")
                items = cur.fetchall()
    except Exception as e:
        flash(f"Error fetching menu: {e}", "danger")
        items = []
    return render_template("menu.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def add_item():
    """Form to add a new item (GET) and process addition (POST)."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        price = request.form.get("price", "").strip()

        if not name:
            flash("Item name is required.", "warning")
            return redirect(url_for("add_item"))

        try:
            price_int = int(price)
        except ValueError:
            flash("Price must be an integer.", "warning")
            return redirect(url_for("add_item"))

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                        (name, price_int),
                    )
            flash(f"Item '{name}' added.", "success")
            return redirect(url_for("show_menu"))
        except Exception as e:
            flash(f"Error adding item: {e}", "danger")
            return redirect(url_for("add_item"))

    # GET
    return render_template("item_form.html", action="Add", item=None)


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    """Delete item by id (POST only)."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM Menu_Items WHERE item_id = %s", (item_id,))
                if cur.rowcount == 0:
                    flash("Item not found.", "warning")
                else:
                    flash("Item deleted.", "success")
    except Exception as e:
        flash(f"Error deleting item: {e}", "danger")
    return redirect(url_for("show_menu"))


@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update_item(item_id):
    """GET: show form pre-filled, POST: apply update to name/price."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        price = request.form.get("price", "").strip()

        if not name:
            flash("Item name is required.", "warning")
            return redirect(url_for("update_item", item_id=item_id))

        try:
            price_int = int(price)
        except ValueError:
            flash("Price must be an integer.", "warning")
            return redirect(url_for("update_item", item_id=item_id))

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_id = %s",
                        (name, price_int, item_id),
                    )
                    if cur.rowcount == 0:
                        flash("Item not found or not updated.", "warning")
                    else:
                        flash("Item updated.", "success")
            return redirect(url_for("show_menu"))
        except Exception as e:
            flash(f"Error updating item: {e}", "danger")
            return redirect(url_for("update_item", item_id=item_id))

    # GET: fetch item and show form
    try:
        with get_conn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_id = %s LIMIT 1", (item_id,))
                row = cur.fetchone()
                if not row:
                    flash("Item not found.", "warning")
                    return redirect(url_for("show_menu"))
    except Exception as e:
        flash(f"Error fetching item: {e}", "danger")
        return redirect(url_for("show_menu"))

    return render_template("item_form.html", action="Update", item=row)


if __name__ == "__main__":
    # For development only; use gunicorn/uwsgi for production
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
