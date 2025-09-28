"""
(self.name, self.price),
)
self.item_id = cur.fetchone()[0]
else:
cur.execute(
"UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_id=%s",
(self.name, self.price, self.item_id),
)
return True
except Exception as e:
print(f"Error saving item: {e}")
return False


def delete(self) -> bool:
"""Delete the item from the DB. Uses item_id if available, otherwise uses name.
Returns True if a row was deleted.
"""
try:
with get_conn() as conn:
with conn.cursor() as cur:
if self.item_id is not None:
cur.execute("DELETE FROM Menu_Items WHERE item_id=%s", (self.item_id,))
else:
cur.execute("DELETE FROM Menu_Items WHERE item_name=%s", (self.name,))
deleted = cur.rowcount
return deleted > 0
except Exception as e:
print(f"Error deleting item: {e}")
return False


def update(self, new_name: str | None = None, new_price: int | None = None) -> bool:
"""Update the item's name and/or price in the DB. Returns True on success.
If item_id is unknown, tries to find the item by current name.
"""
try:
if new_name is None:
new_name = self.name
if new_price is None:
new_price = self.price


with get_conn() as conn:
with conn.cursor(cursor_factory=RealDictCursor) as cur:
if self.item_id is None:
# try to fetch by current name
cur.execute("SELECT item_id FROM Menu_Items WHERE item_name=%s", (self.name,))
row = cur.fetchone()
if not row:
return False
self.item_id = row['item_id']


cur.execute(
"UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_id=%s",
(new_name, int(new_price), self.item_id),
)


# update local values on success
self.name = new_name
self.price = int(new_price)
return True
except Exception as e:
print(f"Error updating item: {e}")
return False


def __repr__(self) -> str:
return f"MenuItem(id={self.item_id!r}, name={self.name!r}, price={self.price!r})"