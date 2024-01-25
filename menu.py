class Menu:
    def __init__(self):
        self.items = {
            'Norin': {'price': 15.00, 'description': 'go\'sht va hamirli ovqat'},
            'Chuchvara': {'price': 05.00, 'description': 'go\'sht va hamirli'},
            'KFC': {'price': 08.00, 'description': 'tovuqli'},
            'Osh': {'price': 15.00, 'description': 'Beshqozon osh'},
            'Shashlik': {'price': 15.00, 'description': 'go\'shtli'},
            'Mastava': {'price': 15.00, 'description': 'guruch va suvli'},
            'Makaron': {'price': 15.00, 'description': 'To\'xtaniyoz otani makaroni'},
            'Lag\'mon': {'price': 15.00, 'description': 'xamirli'},
            'Manti': {'price': 15.00, 'description': 'go\'sht va hamirli'},
            'Choy': {'price': 02.00, 'description': 'Oshxonadagi qora choy'},
        }

    def add_item(self, name, price, description=''):
        self.items[name] = {'price': price, 'description': description}

    def update_item(self, name, new_name, new_price, new_description):
        if name in self.items:
            self.items[new_name] = {'price': new_price,'description': new_description}
            if new_name != name:
                del self.items[name]

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def print_menu(self):
        for name, details in self.items.items():
            print(f"{name}: ${details['price']} - {details['description']}")

    def is_item_available(self, item):
        return item.lower() in (key.lower() for key in self.items)