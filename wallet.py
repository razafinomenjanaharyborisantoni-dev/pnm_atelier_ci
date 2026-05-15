class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, val):
        self.balance = self.balance + val

    def get_balance(self):
        return self.balance

    def remove_balance(self, val):
        """
        Substracts a value from balance

        Args:
            val (float): Value to be substracted from balance.

        Returns:
            float: The substraction of balance and val
        """
        self.balance = self.balance - val
