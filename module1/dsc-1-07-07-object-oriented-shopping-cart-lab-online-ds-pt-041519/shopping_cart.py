import statistics

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total=0
        self.employee_discount=emp_discount
        self.items=[]
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
    
    def mean_item_price(self):
        list_values = [i["price"] for i in self.items]
        print (list_values)
        return statistics.mean(list_values)

    def median_item_price(self):
        list_values = [i["price"] for i in self.items]
        print (list_values)
        return statistics.median(list_values)

    def apply_discount(self):
        if self.employee_discount:
            new_total = self.total - (self.total*20/100)
            return new_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
            
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= removed_item["price"]
            return f"No problem! Your last item was removed. Your total now is {self.total}." 
        else:
            return "There are no items in your cart!"