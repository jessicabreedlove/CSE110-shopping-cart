#For this project, the user will be given a menu and have the ability to choose items from the menu.
#Menu: 1. Add a new item 2. Display Contents of cart 3. Remove item 4. Compute the total 5. Quit

print('Welcome to your personal shopper! Please select one of the menu options')

ask = True

items = []
costs = []
item = ''
cost = ''
remove_index = 0


while ask == True:

    option = input('What would you like to do? 1. ADD ITEM, 2. DISPLAY CART, 3. REMOVE ITEM, 4. COMPUTE TOTAL, or 5. QUIT? ')

    if option == '1':
        add_item = input('What item would you like to add? ')
        item_price = float(input(f'What is the price of the {add_item}? '))
        items.append(add_item)
        costs.append(item_price)
        print(f'{add_item} for ${item_price:.2f} has been added to your cart. ')
        ask = True


    elif option == '2':
        print('Your Cart:')
        for i in range(len(items)):
            item = items[i]
            cost = costs[i]
            print(f'{i+1}. {item} - ${cost:.2f}')
        ask = True

    elif option == '3':
        remove_item_ask = int(input('Which item would you like to remove? Please enter the item number: '))
        if remove_item_ask <= len(items):
            remove_index = remove_item_ask - 1
            items.pop(remove_index)
            costs.pop(remove_index)
            print(f'Item number {remove_item_ask} has been removed')
            ask = True
        else:
            print('Sorry that is not a valid item number')
    
    elif option == '4':
        total = sum(costs)
        print(f'The total price of the items in your cart is: ${total:.2f}')
        ask = True

    elif option == '5':
        ask = False

    else: 
        print('Sorry that is not a valid input')
        ask = True

if ask == False:
    print('Thank you! Goodbye!')

