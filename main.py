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

    Option = input("\033[34m >> \033[0mEnter an Option: ")

    print("\n\033[34m" + "-"*60 + "\033[0m")

    if Option == "1":
        print()
    elif Option == "2":
        print()
    elif Option == "3":
        print()
    elif Option == "4":
        print()
    elif Option == "5":
        print()
    elif Option == "6":
        print()
    elif Option == "7":
        ws = False
    else:
        print("\n\033[1;31m" + "-"*60)
        print("Error: Invalid Value Entered. Enter an option between 1 and 7")
        print("-"*60 + "\033[0m")