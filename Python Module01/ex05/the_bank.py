# in the_bank.py
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
            return False
        
    

