class ShoppingCart:

    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
        
    def add_item(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items.append([name, price, quantity])
        basket_total = []
        for i in self.items:
            basket_total.append(i[1]*i[2])
        self.total = sum(basket_total)
        return self.total

    def mean_item_price(self):
        import numpy as np
        mean_list = []
        for e in self.items:
            for i in range(e[2]):
                mean_list.append(e[1])
        return np.mean(mean_list)

    def median_item_price(self):
        import numpy as np
        median_list = []
        for e in self.items:
            for i in range(e[2]):
                median_list.append(e[1])
        return np.median(median_list)

    def apply_discount(self):
        if self.employee_discount != None:
            self.total = self.total * ((100 - self.employee_discount)/100) 
            return self.total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items == []:
            return "There are no items in your cart!"
        else:
            del self.items[-1]
            basket_total = []
            for i in self.items:
                basket_total.append(i[1]*i[2])
            self.total = sum(basket_total)
            return self.total
            