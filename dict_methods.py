"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    cart = current_cart
    i = 0
    for i in range(len(items_to_add)):
        if items_to_add[i] in cart:
            cart[items_to_add[i]] += 1
        else:
            cart.setdefault(items_to_add[i], 1)
    return cart

# cart = {"Apple": 1, "Banana": 4}

# add_item(cart, ("Apple", "Banana", "Orange"))

# print(cart)

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    i = 0
    for i in range(len(notes)):
        if notes[i] in cart:
            cart[notes[i]] += 1
        else:
            cart.setdefault(notes[i], 1)
    return cart
    
# note = ["Broccoli", "Kiwi", "Melon", "Apple", "Banana"]
# note2 = ("Orange", "Raspberry", "Blueberries")

# read_notes(note)
# read_notes(note2)

# print(note)
# print(note2)

# cart = {}
# cart.setdefault("Orange", 1)
# cart.setdefault("Raspberry", 1)
# print(cart)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)


    return ideas

# ideas = {
#             "Banana Bread": {
#                 "Banana": 1,
#                 "Apple": 1,
#                 "Walnuts": 1,
#                 "Flour": 1,
#                 "Eggs": 2,
#                 "Butter": 1,
#             },
#             "Raspberry Pie": {
#                 "Raspberry": 1,
#                 "Orange": 1,
#                 "Pie Crust": 1,
#                 "Cream Custard": 1,
#             },
#         }

# keylist = list(ideas)

# print(ideas.get("Banana Bread"))

# # ideas.pop("Banana Bread")

# print(ideas.keys())


# update = (
#             "Banana Bread",
#             {
#                 "Banana": 4,
#                 "Walnuts": 2,
#                 "Flour": 1,
#                 "Butter": 1,
#                 "Milk": 2,
#                 "Eggs": 3,
#             },
#          )

# # update_recipes(ideas, update)

# print("Results;")
# print(ideas)


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))

        

          
          
    return sorted_cart



def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_dict={}   
    for item in cart.keys():
        aisle_mapping[item].insert(0,cart[item])
        fulfillment_dict[item]=aisle_mapping[item]
    new_dict={}
    new_dict |= reversed(sorted(fulfillment_dict.items()))
    return new_dict
    


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key in fulfillment_cart.keys():  
        store_inventory[key][0] -= fulfillment_cart[key][0]
        if store_inventory[key][0]<=0:
            store_inventory[key][0]="Out of Stock"

    return store_inventory

        
    
