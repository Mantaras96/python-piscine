
# in the_bank.py
class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

class Bank:
    """ Bank class"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            raise ValueError("Account must be an Account object")
        # self.accounts.append(account)
        if any(account.name == new_account.name for account in self.accounts):
            print("Invalid account type or name already exists in the bank.")
            return False
        if (isAccountCorrupted(new_account)):
            print("Invalid corrupted account.")
            return False
        self.accounts.append(new_account)
        
    def get_account(self, name):
        """Return account object with given name"""

        for account in self.accounts:
            print(account.name)
            if account.name == name:
                return account
        print(f"Account {name} not found in the bank.")
        return None
    
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        
        if (origin == dest):
            print("Origin and destination accounts must be different.")
            return False
        if (amount < 0):
            print("Amount must be positive.")
            return False
        if (not isinstance(amount, float)):
            print("Amount must be a float.")
            return False
        if (not isinstance(origin, str) or not isinstance(dest, str)):
            print("Origin/Destini must be a str.")
            return False
        


def isAccountCorrupted(account):
    """ Check if the account is corrupted
    @account: Account() account to check
    @return True if corrupted, False if not
    """
    corrupted = False
    
    print(len(account.__dict__) % 2 == 1 )
    print(any(key.startswith("b") for key in account.__dict__.keys()))
    print(any(key.startswith("zip") for key in account.__dict__.keys()))
    print(any(key.startswith("addr") for key in account.__dict__.keys()))
    print('name' not in list(account.__dict__.keys()))
    print(not isinstance(account.name, str))
    print('id' not in list(account.__dict__.keys()))
    print(not isinstance(account.id, int))
    print('value' not in list(account.__dict__.keys()))
    print(not isinstance(account.value, float or int))
    print(account.__dict__.keys())

    if (len(account.__dict__) % 2 == 1 or
            any(key.startswith("b") for key in account.__dict__.keys()) or
            not any(key.startswith("zip") for key in account.__dict__.keys()) or
            not any(key.startswith("addr") for key in account.__dict__.keys()) or
            'name' not in account.__dict__.keys() or
            not isinstance(account.name, str) or
            'id' not in account.__dict__.keys() or
            not isinstance(account.id, int) or
            'value' not in account.__dict__.keys() or
            not isinstance(account.value, (float, int))):
        return True
    return False

def	main( ):
    """ Main function """
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        addr='1234 Main Street',
        zip='911-745',
        value=1000.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        other='This is the vice president of the corporation'
    ))
    
    print(bank.get_account("Smith Jane").id);

if __name__ == "__main__":
    main()
