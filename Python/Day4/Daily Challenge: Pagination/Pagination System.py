import math

# ===============================
# Step 1 & 2: Pagination Class
# ===============================
class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # Internal page index (0-based)
        self.total_pages = math.ceil(len(self.items) / page_size)

    # ===============================
    # Step 3: Get Visible Items
    # ===============================
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # ===============================
    # Step 4: Navigation Methods
    # ===============================
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} is out of range.")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # ===============================
    # Step 5: Custom __str__ Method
    # ===============================
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


# ===============================
# Step 6: Test Your Code
# ===============================
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Page 1 items:", p.get_visible_items())  # ['a', 'b', 'c', 'd']

    p.next_page()
    print("Page 2 items:", p.get_visible_items())  # ['e', 'f', 'g', 'h']

    p.last_page()
    print("Last page items:", p.get_visible_items())  # ['y', 'z']

    try:
        p.go_to_page(10)  # Out of range → should raise ValueError
    except ValueError as e:
        print("Error:", e)

    p.go_to_page(7)
    print("Current page index:", p.current_idx + 1)  # 7

    try:
        p.go_to_page(0)  # Out of range → should raise ValueError
    except ValueError as e:
        print("Error:", e)

    # Print using __str__
    p.first_page()
    print("\nCurrent Page View:")
    print(p)
