orders = {}
order_auto_id = 1

def create_order(clients, products, orders, order_auto_id):
    print("\n--- CREATE ORDER ---")

    #VALIDATE CLIENT
    while True:
        client_id = input("Enter client CC: ")

        if client_id in clients:
            break
        else:
            print("Error: client does not exist. Try again.")

    #Create order structure
    order_detail = {}

    while True:
        #VALIDATE PRODUCT ID
        while True:
            try:
                product_id = int(input("Enter product ID: "))

                if product_id in products:
                    break
                else:
                    print("Error: product does not exist. Try again.")
            except ValueError:
                print("Error: enter a valid number.")

    #VALIDATE QUANTITY
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    break
                else:
                    print("Error: quantity must be greater than 0.")
            except ValueError:
                print("Error: enter a valid number.")

        #Get product data
        product_data = products[product_id]

        #Save without using lists
        order_detail[product_id] = {
            "name": product_data[0],
            "price": product_data[1],
            "quantity": quantity
        }

        #VALIDATE CONTINUE OPTION
        while True:
            more = input("Add another product? (y/n): ").lower()

            if more in ["y", "n"]:
                break
            else:
                print("Error: enter 'y' or 'n'.")

        if more == "n":
            break

    #Save order
    orders[order_auto_id] = {
        "client_id": client_id,
        "products": order_detail
    }

    print(f"\nOrder {order_auto_id} created successfully.")
    order_auto_id += 1

order_auto_id = create_order (clients, products, orders, order_auto_id)