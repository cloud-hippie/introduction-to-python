# Lists

# lists are used to store multiple values in a single variable
to_do_list = []


# add items to the list
to_do_list.append("walk the dog")
to_do_list.append("buy groceries")
to_do_list.append("finish homework")

# # Show the list
# print(to_do_list)

for list_item in to_do_list:
    if list_item == "buy groceries":
        print("OH NO I FORGOT TO BUY GROCERIES")
    print(list_item)

