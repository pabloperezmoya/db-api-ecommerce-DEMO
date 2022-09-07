
import _db_classes

class Users(_db_classes.Tables):
    def __init__(self):
        super().__init__('users')

class Passwords(_db_classes.Tables):
    def __init__(self):
        super().__init__('passwords')

class Purchases(_db_classes.Tables):
    def __init__(self):
        super().__init__('purchases')

class Carts(_db_classes.Tables):
    def __init__(self):
        super().__init__('carts')

class Invoices(_db_classes.Tables):
    def __init__(self):
        super().__init__('invoices')

class Products(_db_classes.Tables):
    def __init__(self):
        super().__init__('products')
