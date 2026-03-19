import re
import os
# ==============================
# PROGRAM DATABASES
# ==============================

# ==============================
# CUSTOMER DATABASE
# ==============================
customer_database = {
    "123456": {"auto_id": 1, "name": "Jesus Lucena", "email": "jesus@gmail.com", "phone": "3011234567", "state": True},
    "654321": {"auto_id": 2, "name": "Ana Torres", "email": "ana@gmail.com", "phone": "3017654321", "state": True},
    "112233": {"auto_id": 3, "name": "Pedro Perez", "email": "pedro@gmail.com", "phone": "3021122334", "state": True},
    "445566": {"auto_id": 4, "name": "Maria Gomez", "email": "maria@gmail.com", "phone": "3024455667", "state": True},
    "778899": {"auto_id": 5, "name": "Luis Sanchez", "email": "luis@gmail.com", "phone": "3037788990", "state": True},
    "123455": {"auto_id": 6, "name": "Luis Sanchez", "email": "lus@gmail.com", "phone": "307788990", "state": True}
}

# ==============================
# PRODUCT DATABASE
# ==============================
product_database = {
    1: ("Pan", 12.0, 100, "Groceries"),
    2: ("Queso", 20.0, 50, "Groceries"),
    3: ("Jugo", 10.0, 80, "Groceries"),
    4: ("Leche", 15.0, 60, "Groceries"),
    5: ("Zapatos", 120.0, 30, "Footwear"),
    6: ("Camiseta", 35.0, 40, "Clothing"),
    7: ("Laptop", 2500.0, 10, "Electronics"),
    8: ("Teclado", 150.0, 25, "Electronics"),
    9: ("Silla", 200.0, 15, "Home & Furniture"),
    10: ("Libro", 50.0, 40, "Stationery")
}

# ==============================
# ORDER DATABASE
# ==============================
order_database = {}

# Order 1 for Jesus
order_database[1] = {
    "cc": "123456",
    "name": "Jesus Lucena",
    "producto1": (1, "Pan", 5, 60.0),
    "producto2": (2, "Queso", 2, 40.0),
}

# Order 2 for Ana
order_database[2] = {
    "cc": "654321",
    "name": "Ana Torres",
    "producto1": (3, "Jugo", 3, 30.0),
    "producto2": (4, "Leche", 4, 60.0),
}

# Order 3 for Jesus again
order_database[3] = {
    "cc": "123456",
    "name": "Jesus Lucena",
    "producto1": (5, "Zapatos", 1, 120.0),
    "producto2": (6, "Camiseta", 2, 70.0),
}

# Order 4 for Pedro
order_database[4] = {
    "cc": "112233",
    "name": "Pedro Perez",
    "producto1": (1, "Pan", 10, 120.0),
    "producto2": (4, "Leche", 5, 75.0),
}

# Order 5 for Maria
order_database[5] = {
    "cc": "445566",
    "name": "Maria Gomez",
    "producto1": (7, "Laptop", 1, 2500.0),
    "producto2": (8, "Teclado", 1, 150.0),
}

# Order 6 for Luis
order_database[6] = {
    "cc": "778899",
    "name": "Luis Sanchez",
    "producto1": (9, "Silla", 2, 400.0),
    "producto2": (10, "Libro", 3, 150.0),
}

product_categories = (
    "Electronics",
    "Appliances",
    "Groceries",
    "Clothing",
    "Footwear",
    "Health & Beauty",
    "Home & Furniture",
    "Stationery",
    "Toys",
    "Sports",
    "Automotive",
    "Hardware & Tools"
)

# ==============================
# ERROR VALIDATION
# ==============================

def validate_not_empty(field_value, field_name):

    if not str(field_value).strip():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} cannot be empty. Please enter a valid value." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_duplicate_id(field_value, database):

    if field_value in database:
        return ("\n\033[1;31m" + "-"*60 + "\nError: This ID already exists. Please enter a different ID." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_duplicate_data(field_value, database, key, field_name):
    
    for data in database.values():

        if field_value == data.get(key):
            return ("\n\033[1;31m" + "-"*60 + f"\nError: This {field_name} is already registered. Please use a different one." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_email_format(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(pattern, email):
        return ("\n\033[1;31m" + "-"*60 + "\nError: Invalid email format. Please enter a valid email (e.g., user@gmail.com)." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_numeric_length(field_value, field_name, min_len, max_len):

    if not field_value.isdigit():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only numbers." + "\n" + "-"*60 + "\033[0m")

    if len(field_value) < min_len or len(field_value) > max_len:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must be between 6 and 8 digits." + "\n" + "-"*60 + "\033[0m")

    return None

def validate_only_letters(field_value, field_name):

    if not field_value.replace(" ", "").isalpha():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only letters (no numbers)." + "\n" + "-"*60 + "\033[0m")

    return None

def validate_only_numbers(field_value, field_name):

    if not field_value.isdigit():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only numbers." + "\n" + "-"*60 + "\033[0m")

    return None

def validate_cuantiti_negative(field_value):
    if field_value < 0:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: The entered value cannot be negative." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_stock_above_minimum(field_value, num):
    if field_value <= num:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Stock must be greater than the minimum allowed (3 units). Please enter a value above 3." + "\n" + "-"*60 + "\033[0m")
    
    return None

def validate_category_option(field_value, min, max):

    if field_value < min or field_value > max:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Value out of allowed range." + "\n" + "-"*60 + "\033[0m")

    return None

def validate_sale(stock, min_stock, quantity):
    
    available_stock = stock - min_stock
    
    if quantity > available_stock:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Only {available_stock} units available for sale." + "\n" + "-"*60 + "\033[0m")
    
    return None
# ==============================
# 1) FUNCTION TO REGISTER CUSTOMERS
# ==============================

def customer_registration(customer_id, customer_name, customer_email, customer_phone):

    id_customer = len(customer_database)+1
    
    customer_database[customer_id] = {
        "auto_id": id_customer,
        "name": customer_name,
        "email": customer_email,
        "phone" : customer_phone,
        "state" : True
    }

    customer_history[customer_id] = {
        "auto_id": id_customer,
        "name": customer_name,
        "email": customer_email,
        "phone" : customer_phone,
        "state" : True
    }

    return True

def register_product(product_name, product_price, product_stock, product_categorie):

    id_product = len(product_database) + 1
    product_database [id_product] = (product_name,product_price,product_stock,product_categories[product_categorie-1])
    Products_history [id_product] = (product_name,product_price,product_stock,product_categories[product_categorie-1])

def create_order(customer_id):
    
    id_order = len(order_database) + 1

    customer_name = customer_database[customer_id]["name"]
    
    order_database[id_order] = {
        "cc" : customer_id,
        "name": customer_name,
    }
    Order_history[id_order]  = {
        "cc" : customer_id,
        "name": customer_name,
    }

    return id_order

def add_products_order(id_order, product_id, quantity_order, cont):
    
    product_name = product_database[product_id][0]

    total = quantity_order * product_database[product_id][1]
    
    order_database[id_order]["producto"+str(cont)] = (product_id,product_name,quantity_order,total)
    Order_history[id_order]["producto"+str(cont)] = (product_id,product_name,quantity_order,total)

def orders_consult(order_db,field_value):
        
        for pedido in order_db.values():
                
            cc = pedido.get("cc"," ")

            if cc == field_value:
                print("\n\033[34m" + "-"*60)
                print("ORDER CREATION HISTORY")
                print("\033[34m" + "-"*60)
                cc = pedido.get("cc", "")
                nombre = pedido.get("name", "")
                
                print(f"CC: {cc} - Nombre: {nombre}")
                print("\033[34m" + "-"*60)
                print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")

            else:
                print("\n\033[1;31m" + "-"*60 + f"\nError: There are no orders from this user." + "\n" + "-"*60 + "\033[0m")
                break

        

        for pedido in order_db.values():
                
            cc = pedido.get("cc"," ")

            if cc == field_value:
                
                if pedido:

                    # Recorremos todos los productos del pedido
                    productos = [pedido[k] for k in sorted(pedido.keys()) if k.startswith('producto') and isinstance(pedido[k], tuple)]
                    
                    if productos:
                        for p in productos:
                            _, producto_nombre, cantidad, total = p
                            print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")
                            print("\033[34m" + "-"*60)
                    else:
                        print("No tiene productos.")
                        print("\033[34m" + "-"*60)
                
                


def display_order(order_db):
    
    for pedido in order_db.values():

        print("\n\033[34m" + "-"*60)
        print("ORDER CREATION HISTORY")
        print("\033[34m" + "-"*60)
        cc = pedido.get("cc", "")
        nombre = pedido.get("name", "")
        
        print(f"CC: {cc} - Nombre: {nombre}")
        print("\033[34m" + "-"*60)
        print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")
        
        # Recorremos todos los productos del pedido
        productos = [pedido[k] for k in sorted(pedido.keys()) if k.startswith('producto') and isinstance(pedido[k], tuple)]
        
        if productos:
            for p in productos:
                _, producto_nombre, cantidad, total = p
                print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")
                print("\033[34m" + "-"*60)
        else:
            print("No tiene productos.")
            print("\033[34m" + "-"*60)
# ==============================
# FUNCTION TO DISPLAY TITLES
# ==============================

def title(title):
    # Centers the title with dashes on the sides
    if len(title) % 2 == 0:
        side = (58 - len(title)) // 2
        print("\033[34m" + "-"*side + " " + title + " " + "-"*side + "\033[0m")
    else:
        side = ((58 - 1) - len(title) + 1) // 2
        print("\n\033[34m" + "-"*side + " " + title + " -" + "-"*side + "\033[0m")

def confirm_exit(message="Do you want to continue? (Y/N): "):

    option = input(f"\n\033[31m >> \033[0m{message}").strip().lower()
        
    if option == "n":
        return True     

def iterate_list(list):

    title("List Categories")
    for Cont , categorie in enumerate(list):
        print (f"{Cont+1}. {categorie}")

def display_order_summary(order_db):

    for pedido in order_db.values():

        print("\n\033[34m" + "-"*60)
        print("ORDER CREATION HISTORY")
        print("\033[34m" + "-"*60)
        cc = pedido.get("cc", "")
        nombre = pedido.get("name", "")
        
        print(f"CC: {cc} - Nombre: {nombre}")
        print("\033[34m" + "-"*60)
        print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")
        
        # Recorremos todos los productos del pedido
        productos = [pedido[k] for k in sorted(pedido.keys()) if k.startswith('producto') and isinstance(pedido[k], tuple)]
        
        if productos:
            for p in productos:
                _, producto_nombre, cantidad, total = p
                print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")
                print("\033[34m" + "-"*60)
        else:
            print("No tiene productos.")
            print("\033[34m" + "-"*60)

def Daily_Income_Calculation(order_db):

    total_sum = 0
    cont = 1
    
    for pedido in order_db.values():

        print("\n\033[34m" + "-"*60)
        print(f"ORDER - N{cont}")
        print("\033[34m" + "-"*60)

        cont += 1
        cc = pedido.get("cc", "")
        nombre = pedido.get("name", "")
        
        print(f"CC: {cc} - Nombre: {nombre}")
        print("\033[34m" + "-"*60)
        print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")
        
        # Recorremos todos los productos del pedido
        productos = [pedido[k] for k in sorted(pedido.keys()) if k.startswith('producto') and isinstance(pedido[k], tuple)]
        
        if productos:
            for p in productos:
                _, producto_nombre, cantidad, total = p
                print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")
                total_sum += total
                print("\033[34m" + "-"*60)
        else:
            print("No tiene productos.")
            print("\033[34m" + "-"*60)


        print("\n\033[34m" + "-"*60)
        print(f">> Total profit for the day : ${total_sum}")
        print("\033[34m" + "-"*60 + "\033[0m")

            
# ==============================
# MAIN OPTIONS MENU
# ==============================

def main():
    title("Menu Options")

    print("""
\033[34m    1.\033[0m Customer Registration
\033[34m    2.\033[0m Product Registration
\033[34m    3.\033[0m Order Creation
\033[34m    4.\033[0m View Registered Orders
\033[34m    5.\033[0m Daily Income Calculation
\033[34m    6.\033[0m Final Report Generation
            
\033[31m    7.\033[0m Exit
    """)

    print("\033[34m" + "-"*60 + "\033[0m\n")

ws = True 

while ws:

    
    main()

    option = input("\033[34m >> \033[0mEnter an Option: ")

    os.system("cls" if os.name == "nt" else "clear")

    print("\n\033[34m" + "-"*60 + "\033[0m")

    if option == "1":

        customer_history = {}

        # Control variable to keep the registration active
        cr_act = True

        # Main loop for customer registration
        while cr_act:

            # Show section title
            title(f"Customer Registration {len(customer_database)+1}")
                    
            # ===== INPUT: CUSTOMER ID =====
            while True:

                # Ask for CC (ID)
                user_id_document = input("\n\033[34m >> \033[0mEnter your CC number: ")

                # Validate empty field
                error = validate_not_empty(user_id_document, "CC Number")
                if error:
                    print(error)
                    continue

                error = validate_only_numbers(user_id_document, "CC Number")
                if error:
                    print(error)
                    continue

                # Validate duplicate ID
                error = validate_duplicate_id(user_id_document, customer_database)
                if error:
                    print(error)
                    continue  

                # Validate numeric and length (6–10 digits)
                error = validate_numeric_length(user_id_document, "CC Number", 6, 10)
                if error:
                    print(error)
                    continue

                # Exit loop if all validations pass
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: FULL NAME =====
            while True:

                # Ask for full name
                user_full_name = input("\n\033[34m >> \033[0mEnter your full name: ")

                # Validate empty field
                error = validate_not_empty(user_full_name, "Full Name")
                if error:
                    print(error)
                    continue  

                error = validate_only_letters(user_full_name, "Full Name")
                if error:
                    print(error)
                    continue
                    
                # Exit loop if valid
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: EMAIL =====
            while True:

                # Ask for email
                user_email = input("\n\033[34m >> \033[0mEnter your email: ")
                    
                # Validate empty field
                error = validate_not_empty(user_email, "Email")
                if error:
                    print(error)
                    continue  

                # Validate email format
                error = validate_email_format(user_email)
                if error:
                    print(error)
                    continue

                # Validate duplicate email
                error = validate_duplicate_data(user_email, customer_database, "email", "Email")
                if error:
                    print(error)
                    continue  
                    
                # Exit loop if valid
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: PHONE NUMBER =====
            while True:

                # Ask for phone number
                user_phone = input("\n\033[34m >> \033[0mEnter your phone number: ")
                    
                # Validate empty field
                error = validate_not_empty(user_phone, "Phone Number")
                if error:
                    print(error)
                    continue  

                error = validate_only_numbers(user_phone, "Phone Number")
                if error:
                    print(error)
                    continue

                # Validate duplicate phone
                error = validate_duplicate_data(user_phone, customer_database, "phone", "Phone Number")
                if error:
                    print(error)
                    continue
                    
                # Exit loop if valid
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== CREATE CUSTOMER =====
            customer_registration(user_id_document, user_full_name, user_email, user_phone)


            exit = confirm_exit()
            if exit == True:
                cr_act = False
            else:
                continue
            
            # ===== CUSTOMER CREATION HISTORY =====

            print("\n\033[34m" + "-"*80)
            print("CUSTOMER CREATION HISTORY")
            print("\033[34m" + "-"*80)
            print(f"{'ID':<5} {'CC':<12} {'NAME':<15} {'EMAIL':<25} {'PHONE':<10}")
            print("-"*80 + "\033[0m")

            for cc, data in customer_history.items():
                print(
                    f"\033[1;32m{data['auto_id']:<5} {cc:<12} {data['name']:<15} {data['email']:<25} {data['phone']:<10}\033[0m"
                )
                print("\033[34m" + "-"*80 + "\033[0m")

            # Final separator
            print("\033[34m" + "-"*60 + "\033[0m\n")

    elif option == "2":

        Products_history = {}

        pr_act = True

        while pr_act:

            title(f"Product Registration N{len(product_database)+1}")
    
            # ===== INPUT: PRODUCT NAME =====
            while True:
                product_name = input("\n\033[34m >> \033[0mEnter the product name: ")

                error = validate_not_empty(product_name, "Name")
                if error:
                    print(error)
                    continue

                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: PRODUCT PRICE =====
            while True:

                try:
                    product_price = float(input("\n\033[34m >> \033[0mEnter the product price: "))
                except ValueError:
                    print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                    continue

                error = validate_not_empty(product_price, "Product Price")
                if error:
                    print(error)
                    continue

                error = validate_cuantiti_negative(product_price)
                if error:
                    print(error)
                    continue

                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: PRODUCT STOCK =====
            while True:
                    
                try:
                    product_stock = int(input("\n\033[34m >> \033[0mEnter the product stock (must be greater than 3): "))
                except ValueError:
                    print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                    continue

                error = validate_not_empty(product_stock, "Product Stock")
                if error:
                    print(error)
                    continue

                error = validate_cuantiti_negative(product_stock)
                if error:
                    print(error)
                    continue

                error = validate_stock_above_minimum(product_stock, 3)
                if error:
                    print(error)
                    continue
            
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")


            # ===== INPUT: PRODUCT CATEGORY =====
            while True:
                iterate_list(product_categories)

                try: 
                    product_categorie = int(input(f"\n\033[34m >> \033[0mEnter the number of the option for the product category: "))
                except ValueError:
                    print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                    continue

                error = validate_not_empty(product_categorie, "The option of the product")
                if error:
                    print(error)
                    continue

                error = validate_category_option(product_categorie, 1, len(product_categories))
                if error:
                    print(error)
                    continue

                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            register_product(product_name, product_price, product_stock, product_categorie)

            exit = confirm_exit()
            if exit == True:
                pr_act = False
            else:
                continue

            # ===== PRODUCTS CREATION HISTORY =====

            print("\n\033[34m" + "-"*80)
            print("PRODUCTS CREATION HISTORY")
            print("\033[34m" + "-"*80)
            print(f"{'ID':<5} {'NAME':<22} {'CATEGIRIE':<20} {'STOCK':<10} {'PRICE':<10}")
            print("-"*80 + "\033[0m")

            for cc, data in Products_history.items():
                print(
                    f"\033[1;32m{cc:<5} {data[0]:<22} {data[3]:<20} {data[2]:<10} {data[1]:<10}\033[0m"
                )
                print("\033[34m" + "-"*80 + "\033[0m")

            # Final separator
            print("\033[34m" + "-"*60 + "\033[0m\n")
        
    elif option == "3":

        Order_history = {}

        or_act = True

        if product_database == {} or customer_database == {}:
            print("\n\033[1;31m" + "-"*60 + f"\nError: No data was found to create an order." + "\n" + "-"*60 + "\033[0m\n")
            continue

        title(f"Order Creation N{len(order_database)+1}")

        while True:

            customer_id = input("\n\033[34m >> \033[0mEnter your CC number: ")

            # Validate empty field
            error = validate_not_empty(customer_id, "CC Number")
            if error:
                print(error)
                continue

            error = validate_only_numbers(customer_id, "CC Number")
            if error:
                print(error)
                continue

            # Validate numeric and length (6–10 digits)
            error = validate_numeric_length(customer_id, "CC Number", 6, 10)
            if error:
                print(error)
                continue

            # Validate duplicate ID
            error = validate_duplicate_id(customer_id, customer_database)
            if not error:
                print("\n\033[1;31m" + "-"*60 + f"\nError: CC Number of the Customer was not found." + "\n" + "-"*60 + "\033[0m")
                continue  

            id_order = create_order(customer_id)

            # Exit loop if all validations pass
            break

        cont = 1

        print("\n\033[34m" + "-"*80)
        print("PRODUCTS")
        print("\033[34m" + "-"*80)
        print(f"{'ID':<5} {'NAME':<22} {'CATEGIRIE':<20} {'STOCK':<10} {'PRICE':<10}")
        print("-"*80 + "\033[0m")

        for cc, data in product_database.items():
            print(
                f"\033[1;32m{cc:<5} {data[0]:<22} {data[3]:<20} {data[2]:<10} {data[1]:<10}\033[0m"
                )
            print("\033[34m" + "-"*80 + "\033[0m")

        while or_act:
            title(f"Product Order N{cont}")
    
            # ===== INPUT: PRODUCT ID =====
            while True:

                try: 
                    product_id = int(input(f"\n\033[34m >> \033[0mEnter the number of the option for the products: "))
                except ValueError:
                    print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                    continue

                error = validate_not_empty(product_id, "The option of the product")
                if error:
                    print(error)
                    continue

                error = validate_category_option(product_id, 1, len(product_database))
                if error:
                    print(error)
                    continue

                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            # ===== INPUT: quantity order =====
            while True:
                                   
                try:
                    quantity_order = int(input("\n\033[34m >> \033[0mEnter the quantity of products to order : "))
                except ValueError:
                    print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                    continue

                error = validate_not_empty(quantity_order, "Products to order")
                if error:
                    print(error)
                    continue

                error = validate_cuantiti_negative(quantity_order)
                if error:
                    print(error)
                    continue

                stock = product_database[product_id][2]

                error = validate_sale(stock, 3, quantity_order)
                if error:
                    print(error)
                    continue
            
                break

            # Visual separator
            print("\n\033[34m" + "-"*60 + "\033[0m")

            add_products_order(id_order, product_id, quantity_order, cont)

            exit = confirm_exit()
            if exit == True:
                or_act = False
            else:
                cont += 1
                continue

            # ===== PRODUCTS CREATION HISTORY =====
            display_order_summary(Order_history)

            # Final separator
            print("\033[34m" + "-"*60 + "\033[0m\n")

    elif option == "4":
        or_act = True

        if product_database == {} or customer_database == {} or order_database == {}:
            print("\n\033[1;31m" + "-"*60 + f"\nError: No data was found to create an order." + "\n" + "-"*60 + "\033[0m\n")
            continue

        title(f"Order")

        while True:

            customer_id = input("\n\033[34m >> \033[0mEnter your CC number: ")

            # Validate empty field
            error = validate_not_empty(customer_id, "CC Number")
            if error:
                print(error)
                continue

            error = validate_only_numbers(customer_id, "CC Number")
            if error:
                print(error)
                continue

            # Validate numeric and length (6–10 digits)
            error = validate_numeric_length(customer_id, "CC Number", 6, 10)
            if error:
                print(error)
                continue

            # Validate duplicate ID
            error = validate_duplicate_id(customer_id, customer_database)
            if not error:
                print("\n\033[1;31m" + "-"*60 + f"\nError: CC Number of the Customer was not found." + "\n" + "-"*60 + "\033[0m")
                continue  

            orders_consult(order_database,customer_id)

            # Exit loop if all validations pass
            break

    elif option == "5":
        Daily_Income_Calculation(order_database)
    elif option == "6":
        print()
    elif option == "7":
        ws = False
    else:
        print("\n\033[1;31m" + "-"*60)
        print("Error: Invalid Value Entered. Enter an option between 1 and 7")
        print("-"*60 + "\033[0m")
