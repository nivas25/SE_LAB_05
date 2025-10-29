"""
A simple inventory management system.

"""

import json
from datetime import datetime


def add_item(stock, item="default", qty=0, logs=None):
    """Adds a given quantity of an item to the stock."""
    if logs is None:
        logs = []  # Fix: Using a new list every time

    if not item:
        return

    stock[item] = stock.get(item, 0) + qty
    # Fix: Using an f-string for cleaner formatting
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(stock, item, qty):
    """Removes a given quantity of an item from the stock."""
    try:
        stock[item] -= qty
        if stock[item] <= 0:
            del stock[item]
    except KeyError:
        # Fix: Only catch the specific error for a missing item
        pass


def get_qty(stock, item):
    """Gets the current quantity of a specific item."""
    try:
        return stock[item]
    except KeyError:
        return 0  # Return 0 if item doesn't exist


def load_data(file="inventory.json"):
    """Loads the inventory data from a JSON file."""
    try:
        # Fix: Use 'with' to auto-close files and specify encoding
        with open(file, "r", encoding="utf-8") as f:
            # Fix: Return data instead of using 'global'
            return json.loads(f.read())
    except FileNotFoundError:
        return {}  # Return an empty dictionary if no file
    except json.JSONDecodeError:
        return {}  # Return empty if file is corrupt


def save_data(stock, file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    # Fix: Use 'with' to auto-close files and specify encoding
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock, indent=4))  # Added indent for readability


def print_data(stock):
    """Prints a report of all items and their quantities."""
    print("--- Items Report ---")
    if not stock:
        print("Inventory is empty.")
        return
    for i in stock:
        print(f"{i} -> {stock[i]}")
    print("--------------------")


def check_low_items(stock, threshold=5):
    """Returns a list of items that are below a given threshold."""
    result = []
    for i in stock:
        if stock[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to run the inventory system operations."""
    # Fix: No more global variable. We create and pass 'stock'
    stock = load_data()  # Load existing data at start
    print("--- Initial Data ---")
    print_data(stock)

    add_item(stock, "apple", 10)
    add_item(stock, "banana", 2)
    remove_item(stock, "apple", 3)
    remove_item(stock, "orange", 1)  # This will safely fail
    print("Apple stock:", get_qty(stock, "apple"))
    print("Low items:", check_low_items(stock))

    save_data(stock)  # Save all changes

    print("--- Final Data (from file) ---")
    stock = load_data()  # Load back into the 'stock' variable
    print_data(stock)    # Print from the 'stock' variable


# Standard practice to run main() only when script is executed
if __name__ == "__main__":
    main()
