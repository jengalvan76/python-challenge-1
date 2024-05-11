# Menu dictionary

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
menu = {
    "Breakfast Tacos": {
        "No.1 Potato & Egg": 2.00, 
        "No.2 Sausage & Egg": 2.50, 
        "No.3 Bacon & Egg": 2.00,
    },
    "Drinks": {
    "Small": 1.00,
    "Medium": 2.00,
    "Large": 3.00,
    }
    }
# Launch the store and present a greeting to the customer
print("**Welcome to Good Days Food Truck**")

# Prompt the customer to enter their selection from the menu
customer_selection = int (input("What would you like No. 1, 2 or 3?"))
print (customer_selection)
if customer_selection = (int["No.1 Potato & Egg", "No.2 Sausage & Egg", or "No.3 Bacon & Egg"])

else:
    print ("Error Message")

# If it is a number, convert the input to an integer and use it to check if it is int the keys
customer_selection = "No.1 Potato & Egg"
group_one = ["No.1 Potato & Egg", "No.2 Sausage & Egg", "No.3 Bacon & Egg"]
group_two = ["Small", "Medium", "Large"]
if customer_selection in group_one:
    print (customer_selection + "Is ordering a taco")
elif customer_selection in group_two:
    print (customer_selection) + "Is ordering a drink"
else:
    print (customer_selection) + "Is not ordering from the menu"

# Get the item name from the dictionary and store it as a variable
No1 = 2.00
No2 = 2.50
No3 = 2.00
Small = 1.00
Medium = 2.00
Large = 3.00

print (int(input("How many would you like?")))
quantity = (int(input("How many would you like?")))

customer_selection.append(No1 = 3.00)


# Customers may want to order multiple items, so let's create a continuous
# loop

# Check the customer's input
print (input("Would you like to keep ordering?"))
customer_response = str(input("Would you like to keep ordering y/n?"))
customer_response = "y"
customer_response = "n"

match customer_response.lower():
    case "customer_response = y":
        place_order = True
    case "customer_response = n": 
        place_order = False
        print ("Thank you for your order.")
    case _: 
        print ("I don't understand your response, please try again.")

while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order Breakfast Tacos or Drinks? ")

    # Create a variable for the menu item number
    i = 1
    i = 2
    # Create a dictionary to store the menu for later retrieval
    menu_items = {"Breakfast Tacos", "Drinks"}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            i = 2
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
                    print (int(input("What Menu Item# 1 or 2?")))
                    customer_menu_item_number = print(int(input("What Menu Item#; 1 or 2?")))
            # 3. Check if the customer typed a number

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
