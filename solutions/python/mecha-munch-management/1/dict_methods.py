"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1 
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
        
    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas
    pass


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_cart=dict(sorted(cart.items()))
    return sorted_cart
    pass


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    sorted_items = sorted(cart.keys(), reverse=True)
    
    for item in sorted_items:
        quantity = cart[item]
        
        # Extract location info from aisle_mapping
        if item in aisle_mapping:
            aisle = aisle_mapping[item][0]
            refrigerated = aisle_mapping[item][1]
        else:
            aisle, refrigerated = 'Unknown Aisle', False
            
        # Combine data into the requested list schema
        fulfillment_cart[item] = [quantity, aisle, refrigerated]
        
    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for item, order_details in fulfillment_cart.items():
        if item in store_inventory:
            ordered_quantity = order_details[0]
            current_stock = store_inventory[item][0]
            
            # Deduct the ordered quantity from stock
            new_stock = current_stock - ordered_quantity
            
            # Handle out of stock boundary condition
            if new_stock <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_stock
                
    return store_inventory
