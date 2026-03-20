class Orders:
    def __init__(self,order:str,price:int):
        self.order=order
        self.price=price
        
    def __gt__(self,order2):
        return self.price>order2.price
    
order_1 = Orders("chai",30)
order_2 = Orders("Coffee",20)
print(order_1>order_2)
    