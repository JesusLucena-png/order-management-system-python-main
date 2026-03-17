# Client management system
# This module allows registering clients with validation

clients = {}
auto_id = 1  # contador global

#----FUNCTION----
def register_client(clients, client_id, name, email, auto_id):
    """
    Register a new client in the system.

    Parameters:
        clients (dict): Dictionary where clients are stored
        client_id (str): Client identification (CC)
        name (str): Client name
        email (str): Client email

    Returns:
        tuple: (message, updated auto_id)
    """

    # VALIDATIONS

    # Validate empty fields
    if not client_id or not name or not email:
        return "Error: empty fields.", auto_id
    
     # Validate duplicate client
    if client_id in clients:
        return "Error: client already exists.", auto_id
    
    #Validate duplicate email
    for client in clients.values(): # Get all client data (ignore IDs)
        if client['email'] == email:
            return "Error: email already exists.", auto_id
    
    # Validate email format
    if "@" not in email or "." not in email: 
        return "Error: invalid email.", auto_id
    

    # SAVE CLIENT

    # Save client in dictionary
    clients[client_id] = {
        "auto_id": auto_id,
        "name": name,
        "email": email
    }

    # Increase auto-increment ID
    auto_id += 1

    return "Client registered successfully.", auto_id

#----MAIN PROGRAM----

#Ask user for data

while True:
    client_id = input("Enter CC: ")
    name = input("Enter full name: ")
    email = input("Enter email: ")

#Call function

    result, auto_id = register_client(clients, client_id, name, email, auto_id)

#Show result    

    print(result)

# Show saved client data of succssesful

    if result == "Client registered successfully.":
        print(f"\nClient registered:")
        print(f"System ID: {clients[client_id]['auto_id']}")
        print(f"CC: {client_id}")
        print(f"Name: {clients[client_id]['name']}")
        print(f"Email: {clients[client_id]['email']}\n")