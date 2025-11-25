def process_sale(inventory, sku, qty_sold):
    updated_inventory = []
    sku_found = False

    for current_sku, current_qty in inventory:
        if current_sku == sku:
            sku_found = True
            if current_qty >= qty_sold:
                updated_inventory.append((current_sku, current_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                updated_inventory.append((current_sku, current_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {current_qty}")
        else:
            updated_inventory.append((current_sku, current_qty))

    if not sku_found:
        print(f"SKU {sku} not found in inventory.")

    return updated_inventory



def identify_zero_stock(inventory):
    zero_stock_list = [sku for sku, qty in inventory if qty == 0]

    if zero_stock_list:
        print(f"Zero stock SKUs: {zero_stock_list}")
    else:
        print("No zero stock items found.")

    return zero_stock_list




def main():
    inventory = []

    print("----- Inventory Stock Manager (Task 2) -----")

  
    n = int(input("Enter number of items in inventory: "))

    for i in range(n):
        print(f"\nEnter details for item {i + 1}:")
        sku = int(input("Enter SKU: "))
        qty = int(input("Enter Quantity: "))
        inventory.append((sku, qty))

    while True:
        print("\n--- MENU ---")
        print("1. Process Sale")
        print("2. Identify Zero Stock Items")
        print("3. Display Inventory")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            sku = int(input("Enter SKU to sell: "))
            qty_sold = int(input("Enter quantity sold: "))
            inventory = process_sale(inventory, sku, qty_sold)

        elif choice == 2:
            identify_zero_stock(inventory)

        elif choice == 3:
            print("\nCurrent Inventory:")
            for s, q in inventory:
                print(f"SKU: {s}, Quantity: {q}")

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")



main()
