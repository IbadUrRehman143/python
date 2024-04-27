class fan: 
      def __init__(self, name , quality, quantity, price, model):
            self.name     = name 
            self.quality  = quality 
            self.quantity = quantity
            self.price    = price
            self.model    = model
      def fan_details(self):
            print("="*50)
            print(f"name of fan     :{self.name    }")
            print(f"quality of fan  :{self.quality }")
            print(f"quantity of fan :{self.quantity}")
            print(f"price of fan    :{self.price   }")
            print(f"model of fan    :{self.model   }")
ali = fan (" Ik fan"," A one "," 600"," 9999"," 105 model")


ali.fan_details()