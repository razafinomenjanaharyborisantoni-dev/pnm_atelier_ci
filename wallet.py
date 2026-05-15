class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        """
        Subtracts a value from balance.

        Args:
            val (float): Value to be subtracted from balance.

        Returns:
            float: The subtraction of balance and val.
        """
        self.balance = self.balance - val
        return self.balance