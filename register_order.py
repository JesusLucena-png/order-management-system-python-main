####----RECORD ORDERS----
orders = {}
order_auto_id = 1

def create_order(clients, products, orders, order_auto_id):
    print("\n--- CREATE ORDER ---")
    
    # VALIDATE CLIENT
    while True:
        client_id = input("Enter client CC: ")
        if client_id in clients:
            break
        else:
            print("Error: client does not exist. Try again.")

    # Diccionario para guardar el pedido completo
    order_detail = {"client_id": client_id}
    product_count = 1

    while True:
        # VALIDATE PRODUCT ID
        while True:
            try:
                product_id = int(input("Enter product ID: "))
                if product_id in products:
                    break
                else:
                    print("Error: product does not exist. Try again.")
            except ValueError:
                print("Error: enter a valid number.")

        # VALIDATE QUANTITY
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                else:
                    print("Error: quantity must be greater than 0.")
            except ValueError:
                print("Error: enter a valid number.")

        # Crear tupla del producto
        product_data = products[product_id]
        product_tuple = (product_data[0], product_data[1], quantity)

        # Guardar tupla directamente en el diccionario
        order_detail[f"p{product_count}"] = product_tuple
        product_count += 1

        # VALIDATE CONTINUE OPTION
        while True:
            more = input("Add another product? (y/n): ").lower()
            if more in ["y", "n"]:
                break
            else:
                print("Error: enter 'y' or 'n'.")
        if more == "n":
            break

    # Guardar pedido completo en orders
    orders[order_auto_id] = order_detail
    print(f"\nOrder {order_auto_id} created successfully.")
    order_auto_id += 1

    return order_auto_id

order_auto_id = create_order(clients, products, orders, order_auto_id)
print(orders)