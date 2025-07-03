class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
            print(f"Updated '{name}' quantity to {self.items[name]}.")
        else:
            self.items[name] = quantity
            print(f"Added '{name}' with quantity {quantity}.")

    def get_item_info(self, name):
        if name in self.items:
            print(f"Item: {name}, Quantity: {self.items[name]}")
        else:
            print(f"Item '{name}' not found in inventory.")

    def total_quantity(self):
        total = sum(self.items.values())
        print(f"Total quantity of all items: {total}")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, quantity in self.items.items():
                print(f"- {item}: {quantity}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory System Menu:")
        print("1. Add/Update Item")
        print("2. Get Item Info")
        print("3. Display Total Quantity")
        print("4. Display All Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                quantity = int(input("Enter quantity: "))
                inventory.add_item(name, quantity)
            except ValueError:
                print("Please enter a valid number for quantity.")
        elif choice == "2":
            name = input("Enter item name to search: ").strip()
            inventory.get_item_info(name)
        elif choice == "3":
            inventory.total_quantity()
        elif choice == "4":
            inventory.display_inventory()
        elif choice == "5":
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
