class Product:
    def __init__(self, id_code, title, description, price, quantity):
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity = quantity
    
    """Getter Methods"""
    def get_id_code(self):
        return self._id_code
    
    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def get_quantity(self):
        return self._quantity
    
    """Decrease quantity available"""    
    def decrease_quantity(self):
        if self._quantity < 0:
            raise ValueError('Nothing left in the cart')
        else:
            return self._quantity - 1
    

class Customer:
    def __init__(self, name, account_ID, premium_member):
        self._name = name
        self._account_ID = account_ID
        self._premium_member = premium_member
        self._customer_cart = []
        self._customer_product = None
    
    """Getter Methods"""
    def get_name(self):
        return self._name
    
    def get_account_id(self):
        return self._account_ID
    
    def set_premium_member(self, premium_member):
        if self._premium_member == 0 or self._premium_member == 1:
            self._premium_member = premium_member
    
    """Check if customer is a premium member by using 0's or 1's for identification"""
    def is_premium_member(self):
        if self._premium_member == 1:
            self._premium_member = True
        if self._premium_member == 0:
            self._premium_member = False
        return self._premium_member
    
    """Add product to to cart"""
    def add_product_to_cart(self, customer_product):
        if customer_product == "":
            self._customer_cart = None
        else:
            self._customer_cart.append(customer_product)
    
    """Clear cart"""
    def empty_cart(self):
        if len(self._customer_cart) == 0:
            print('Cart is already empty')
        else:
            self._customer_cart.clear()
    
    def get_cart(self):
        return self._customer_cart

class Store:
    def __init__(self):
        self._inventory = []
        self._members = []
        self._product_id = None
        self._member_id = None
        self._product_name = None
    
    def add_product(self, Product):
        """check if item is already in inventory"""
        for item in self._inventory:
            if Product.get_id_code() == item.get_id_code():
                print('Product already in inventory')
        self._inventory.append(Product)
        
    def add_member(self, Customer):
        """check if member already exists"""
        for member in self._members:
            if Customer.get_account_id() == member.get_account_id():
                print('Customer is already a member')
        self._members.append(Customer)
    
    def get_product_from_ID(self, product_id):
        for item in self._inventory:
            if item.get_id_code() == product_id:
                return item
        return None
    
    def get_member_from_ID(self, member_id):
        for member in self._members:
            if member.get_account_id() == member_id:
                return member
        return None
    
    def product_search(self, product):
        product_id_list = []
        for item in self._inventory:
            if product.toLower() in item.get_title().toLower() or product.toLower() in product.get_description().toLower():
                product_id_list.append(item.get_id_code())
                product_id_list = sorted(product_id_list)
        return product_id_list
    
    def add_product_to_member_cart(self, product_id, member_id):
        for product in self._inventory:
            if product.get_id_code() == product_id:
                for member in self._members:
                    if member.get_account_id() == member_id:
                        if product.get_quantity() > 0:
                            member.add_product_to_cart(product)
                            print('Product added to cart')
                        else:
                            print('Product not in stock')
                    else:
                        print('Member id not found')
        return print('Product id not found')
    
    def check_out_member(self, member_id):
        for member in self._members:
            if member.get_account_id() != member_id:
                raise InvalidCheckoutError
            else:
                checkout = []
                for item in member.get_cart():
                    if item.get_quantity() > 0:
                        checkout.append(item.get_price())
                    else:
                        checkout.append(0.0)
                """Check if member is a premium member"""
                if member.is_premium_member() is True:
                    total = float(sum(checkout))
                    member.empty_cart()
                else:
                    total = float(sum(checkout)) + (float(sum(checkout)) * 0.07)
                    member.empty_cart()
                return total

class InvalidCheckoutError:
    pass

def main():
    try:
        p1 = Product("1234", "Floss", "clean teeth", 3.25, 12)
        p2 = Product("3214", "Toothbrush", "clean your teeth", 5.50, 5)
        c1 = Customer("Paul", "5682", 0)
        c2 = Customer("Jane", "4444", 0)
        s1 = Store()
        s1.add_product(p1)
        s1.add_product(p2)
        s1.add_member(c1)
        s1.add_product_to_member_cart("1234", "5682")
        s1.add_product_to_member_cart("1234", "4444")
        s1.add_product_to_member_cart("3214", "5682")
        s1.add_product_to_member_cart("fwe", "4444")
        result = s1.check_out_member("5682")
    except InvalidCheckoutError:
        print('Member does not exist')
    else:
        print()
        print("Total cost: ${}".format(result))

if __name__ == "__main()__":main()
main()