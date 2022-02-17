"""
BDA350-
Workshop 1
student name: Victoria Villani
Student id: 124307208
Total: /10 pts
Weight: 3%
"""


class Transaction(object):
    """ Represents a transaction. """

    def __init__(self, num, ty, bal):
        """ Initializes the instance variables num, ty, and bal with the supplied arguments: account number, type
        and balance. """
        self.num = num
        self.ty = ty
        self.bal = bal

    def get_ac(self):
        """ Returns the account number. """
        return self.num

    def get_ty(self):
        """ Returns the account type. """
        return self.ty

    def get_bal(self):
        """ Returns the account balance. """
        return self.bal

    def withdraw(self, amount):
        """ Withdraws a given amount from the account, assuming sufficient balance limit. Return True if withdraw was
        processed; False otherwise. """
        if amount < 0:
            raise ValueError('Withdraw amount should not be less than 0')

        if self.bal > amount:
            self.bal -= amount
            print(True)
        else:
            self.bal -= amount
            print(False)

    def deposit(self, amount):
        """ Deposit given amount to the account, and make relevant updates. """
        if amount < 0:
            raise ValueError('Deposit amount should not be less than 0')

        self.bal += amount
        return self.bal


def main():
    statement = []
    statement.append(Transaction(1111, "Saving", 1200))
    statement.append(Transaction(2222, "Checking", 3900))
    statement.append(Transaction(3333, "Saving", 4500))

    for obj in statement:
        print(obj.num, obj.ty, obj.bal, sep=" ")

    for obj2 in statement:
        obj2.deposit(300)
        print(f"Customers' new balance is: {obj2.get_bal()}")

    for obj3 in statement:
        obj3.withdraw(1501)
        print(f"Customers' new balance is: {obj3.get_bal()}")


if __name__ == '__main__':
    main()
