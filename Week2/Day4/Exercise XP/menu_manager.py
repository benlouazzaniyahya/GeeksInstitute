"""
menu_manager.py
Contains MenuManager class with classmethods get_by_name and all_items.
"""
from menu_item import MenuItem, get_conn
from psycopg2.extras import RealDictCursor




class MenuManager:
@classmethod
def get_by_name(cls, name: str) -> MenuItem | None:
"""Return a MenuItem object for the first row that matches `name` or None if not found."""
try:
with get_conn() as conn:
with conn.cursor(cursor_factory=RealDictCursor) as cur:
cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_name=%s LIMIT 1", (name,))
row = cur.fetchone()
if row:
return MenuItem(row['item_name'], row['item_price'], row['item_id'])
return None
except Exception as e:
print(f"Error fetching by name: {e}")
return None


@classmethod
def all_items(cls) -> list[MenuItem]:
"""Return a list of MenuItem objects for all rows in the Menu_Items table."""
items: list[MenuItem] = []
try:
with get_conn() as conn:
with conn.cursor(cursor_factory=RealDictCursor) as cur:
cur.execute("SELECT item_id, item_name, item_price FROM Menu_Items ORDER BY item_id")
rows = cur.fetchall()
for row in rows:
items.append(MenuItem(row['item_name'], row['item_price'], row['item_id']))
except Exception as e:
print(f"Error fetching all items: {e}")
return items