class BankAccount:
    total_accounts = 0  # Class variable to track total accounts

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        BankAccount.total_accounts += 1
        pass

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")
        pass

    def withdraw(self, amount):
        transaction_fee = 2
        if BankAccount.validate_amount(amount) and self.balance >= (amount + transaction_fee):
            self.balance -= (amount + transaction_fee)
            self.transaction_history.append(f"Withdrew: {amount} (Fee: {transaction_fee})")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
        pass

    def transfer(self, recipient, amount):
        if isinstance(recipient, BankAccount) and BankAccount.validate_amount(amount):
            transaction_fee = 2
            if self.balance >= (amount + transaction_fee):
                self.balance -= (amount + transaction_fee)
                recipient.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to {recipient.account_holder} (Fee: {transaction_fee})")
                recipient.transaction_history.append(f"Received: {amount} from {self.account_holder}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid recipient account or transfer amount.")        pass

    def check_balance(self):
        return self.balance
        pass

    def get_transaction_history(self):
        return self.transaction_history
        pass

    @classmethod
    def total_bank_accounts(cls):
        return cls.total_accounts
        pass

    @staticmethod
    def validate_amount(amount):
        if isinstance(amount, (int, float)) and amount > 0:
            return True
        return False

        pass
