class Bank:
    def __init__(self,cash):
        self.cash=cash
    @property
    def cash(self):
        return self.__cash
    @cash.setter
    def cash(self,val):
        if val<0:
            raise ValueError("cash cannot be negative")
        self.__cash=val
bcash=Bank(30)
print(bcash.cash)
