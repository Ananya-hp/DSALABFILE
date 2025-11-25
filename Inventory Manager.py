
inventory = []



def insert_product():
    sku = input("Enter SKU: ").strip()

    # SKU cannot be empty
    if sku == "":
        print("SKU cannot be empty.")
        return

  
    for item in inventory:
        if item['sku'] == sku:
            print("Product with this SKU already exists!")
            print("Updating quantity instead of rejecting (as per TC13).")

            try:
                new_qty = int(input("Enter New Quantity to Update: "))
                if new_qty <= 0:
                    print("Quantity must be positive.")
                    return
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                return

            item['quantity'] = new_qty
            print("Quantity updated successfully.")
            return

   
    name = input("Enter Product Name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return

   
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    
    product = {'sku': sku, 'name': name, 'quantity': quantity}
    inventory.append(product)
    print("Product inserted successfully.")


def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print("SKU\t\tProduct Name\t\tQuantity")
    print("-----------------------------------------------")
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")
    print()



def search_by_sku():
    sku = input("Enter SKU to search: ").strip()
    for item in inventory:
        if item['sku'] == sku:
            print("Product Found:")
            print(item)
            return
    print("No product found with this SKU.")



def search_by_name():
    name = input("Enter Product Name to search: ").strip().lower()
    for item in inventory:
        if item['name'].lower() == name:
            print("Product Found:")
            print(item)
            return
    print("No product found with this name.")



def delete_product():
    sku = input("Enter SKU to delete: ").strip()
    for item in inventory:
        if item['sku'] == sku:
            inventory.remove(item)
            print("Product removed successfully.")
            return
    print("No product found with this SKU.")



def main():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert / Update Product")
        print("2. Display Inventory")
        print("3. Search by SKU")
        print("4. Search by Name")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            search_by_sku()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")



main()
