class LibraryItem:
    def __init__(self, id_code, title, location = "ON_SHELF", checked_out_by = None, requested_by = None):
        self._id_code = id_code
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = 0
    
    """Setter Methods"""
    def set_id_code(self, id_code):
        self._id_code = id_code
    
    def set_title(self, title):
        self._title = title
    
    def set_location(self, location):
        if location == "ON_SHELF":
            self._location = "ON_SHELF"
        elif location == "ON_HOLD_SHELF":
            self._location = "ON_HOLD_SHELF"
        elif location == "CHECKED_OUT":
            self._location = "CHECKED_OUT"
    
    def set_checked_out_by(self, patron_id):
        self._checked_out_by = patron_id
    
    def set_requested_by(self, patron_id):
        self._requested_by = patron_id
    
    def set_date_checked_out(self, lib_date):
        self._date_checked_out = lib_date
    
    """Getter Methods"""
    def get_id_code(self):
        return self._id_code
    
    def get_title(self):
        return self._title
    
    def get_location(self):
        return self._location
    
    def get_checked_out_by(self):
        return self._checked_out_by
    
    def get_requested_by(self):
        return self._requested_by
    
    def get_date_checked_out(self):
        return self._date_checked_out

class Book(LibraryItem):
    def __init__(self, id_code, title, author, location='ON_SHELF', checked_out_by=None, requested_by=None):
        super().__init__(id_code, title, location=location, checked_out_by=checked_out_by, requested_by=requested_by)
        self._author = author
        self._check_out_length = 21
    
    def get_check_out_length(self):
        return self._check_out_length

class Album(LibraryItem):
    def __init__(self, id_code, title, artist, location='ON_SHELF', checked_out_by=None, requested_by=None):
        super().__init__(id_code, title, location=location, checked_out_by=checked_out_by, requested_by=requested_by)
        self._artist = artist
        self._check_out_length = 14
    
    def get_check_out_length(self):
        return self._check_out_length

class Movie(LibraryItem):
    def __init__(self, id_code, title, director, location='ON_SHELF', checked_out_by=None, requested_by=None):
        super().__init__(id_code, title, location=location, checked_out_by=checked_out_by, requested_by=requested_by)
        self._director = director
        self._check_out_length = 7
    
    def get_check_out_length(self):
        return self._check_out_length

class Patron:
    def __init__(self, id_num, name):
        self._id_num = id_num
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0
    
    """Setter Methods"""
    def set_id_num(self, id_num):
        self._id_num = id_num
    
    def set_title(self, title):
        self._title = title
    
    """Getter Methods"""
    def get_id_num(self):
        return self._id_num 
    
    def get_title(self):
        return self._title
    
    def get_checked_out_items(self):
        return self._checked_out_items
    
    def get_fine_amount(self):
        return self._fine_amount
    
    def add_library_item(self, LibraryItem):
        self._checked_out_items.append(LibraryItem)
    
    def remove_library_item(self, LibraryItem):
        for item in self.get_checked_out_items():
            if item.get_id_code() != LibraryItem.get_id_code():
                print("error")
            else:
                self._checked_out_items.remove(LibraryItem)
    
    def amend_fine(self, fine):
        self._fine_amount += fine

class Library:
    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0
        self._item_id = None
        self._patron_id = None
        self._fine_amount = 0
    
    """Getter Methods"""
    def get_libaray_item(self, item_id):
        for item in self._holdings:
            if len(self._holdings) == 0:
                return None
            else:
                if item.get_id_code() == item_id:
                    return item
        return None
    
    def get_patron(self, patron_id):
        for patron in self._members:
            if len(self._members) == 0:
                return None
            else:
                if patron.get_id_num() == patron_id:
                    return patron
        return None
    
    def get_holdings(self):
        return self._holdings
    
    def get_members(self):
        return self._members
    
    def get_current_date(self):
        return self._current_date
    
    #Other Methods
    
    def add_library_item(self, LibraryItem):
        self._holdings.append(LibraryItem)
    
    def add_patron(self, Patron):
        self._members.append(Patron)
    
    def check_out_library_item(self, item_id, patron_id):
        for item in self._holdings:
            #check if item exists
            if item.get_id_code() == item_id:
                #loop through members to check out item in correspondence of patron_id being passed
                for patron in self._members:
                    #check if member exists
                    if patron.get_id_num() == patron_id:
                        #check if item is checked out
                        if item.get_id_code() == item_id and item.get_checked_out_by() is not None:
                            if item.get_checkout_by() != patron_id and item.get_location() == "CHECKED_OUT":
                                return "item already checked out"
                        #check if item is on hold
                        if item.get_id_code() == item_id and patron_id is not None:
                            if item.get_requested_by() != patron_id and item.get_location() == "ON_HOLD_SHELF":
                                return "item is on hold"
                        #if item if on hold by the patron set requested by to None
                        if item.get_id_code() == item_id and item.get_request_by() == patron_id:
                            item.set_requested_by(None)
                        
                        item.set_checked_out_by(patron_id)
                        
                        item.set_date_checked_out(self._current_date)
                        
                        item.set_location("CHECKED_OUT")
                        
                        patron.add_library_item(item)
                        
                        return "checkout successful"
                return "patron not found"
        return "item not found"
    
    def return_library_item(self, item_id, patron_id):
        for item in self._holdings:
            #check if item exists
            if item.get_id_code() == item_id:
                #let the user know if the item is already checked out or not
                if item.get_location() != "CHECK_OUT":
                    return "item already in the library"
                #loop through members
                for patron in self._members:
                    if patron.get_id_num() == item.get_checked_out_by():
                        patron.remove_library_item(item)
                        #check if someone else has requested this item to place on hold shelf
                        if item.get_requested_by() is not None and item.get_requested_by() != patron.get_id_num():
                            item.set_location("ON_HOLD_SHELF")
                        else:
                            #otherwise place on shelf
                            item.set_location("ON_SHELF")
                        item.set_checked_out_by(None)
                        return "return successful"
        return "item not found"
    
    def request_library_item(self, item_id, patron_id):
        for item in self._holdings:
            if item.get_id_code() == item_id:
                for patron in self._members:
                    if patron.get_id_num == patron_id:
                        if item.get_requested_by() is not None:
                            return "item on hold"
                        item.set_request_by(patron.get_id_num())
                        if item.get_location() == "ON_SHELF":
                            item.set_location("ON_HOLD_SHELF")
                        return "item on hold successfully"
                return "patron not found"
        return "item not found"
    
    def increment_current_date(self):
        self._current_date += 1
        
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if self._current_date > (item.get_checked_out_date() + item.get_check_out_length()):
                    late_fees = 0.10
                    patron.amend_fine(late_fees)
    
    def pay_fine(self, patron_id, fine_amount):
        for patron in self._members:
            if patron.get_id_num() == patron_id:
                patron.amend_fine(fine_amount * -1)
                return "payment successful"
        return "patron not found"

def main():
    b1 = Book("123", "War and Peace", "Tolstoy")
    b2 = Book("234", "Moby Dick", "Melville")
    b3 = Book("345", "Phantom Tollbooth", "Juster")
    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")
    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(b2)
    lib.add_library_item(b3)
    lib.add_patron(p1)
    lib.add_patron(p2)
    lib.check_out_library_item("bcd", "234")
    for i in range(7):
        lib.increment_current_date()
    lib.check_out_library_item("bcd", "123")
    lib.check_out_library_item("abc", "345")
    for i in range(24):
        lib.increment_current_date()
    lib.pay_fine("bcd", 0.4)
    p1Fine = p1.get_fine_amount()
    print(p1Fine)
    p2Fine = p2.get_fine_amount()
    print(p2Fine)

if __name__=="__main()__":main()
main()