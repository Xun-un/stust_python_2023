class friedchicken:
    def __init__(self, crispy_level, spicy, size, amout, price):
        self._crispy_level = crispy_level
        self._spicy = spicy
        self._size = size
        self._amout = amout
        self._price = price

    def  getMeals(self):
        # 顯示食物資訊
        print(f"Crispy_level : {self._crispy_level}")
        print(f"spicy : {self._spicy}")
        print(f"size : {self._size}")
        print(f"amout : {self._amout}")
        print(f"price : {self._price}")
    
    def getSpicy(self):
        # 顯示辣度
        print(f"Your spicy to {self._spicy} for the fried chicken.")
    
    def getTotalPrice(self):
        # 計算並顯示總價格
        total_price = self._amout * self._price
        print(f"TotalPrice = ${total_price}")
    
# 建立四個物件    
list1 = friedchicken(3,"not","small",1,100)
list2 = friedchicken(1,"not","big",3,200)
list3 = friedchicken(2,"small","small",2,100)
list4 = friedchicken(3,"big","big",1,200)

list1.getMeals()
list1.getSpicy()
list1.getTotalPrice()
list2.getMeals()
list2.getSpicy()
list2.getTotalPrice()
list3.getMeals()
list3.getSpicy()
list3.getTotalPrice()
list4.getMeals()
list4.getSpicy()
list4.getTotalPrice()