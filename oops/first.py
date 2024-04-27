# map
class House:
    def __init__(self, personName):
        self.tvRoom = personName + " tv room"
        self.roomWidth = 100
        self.roomHieght = 200
        # print(tvRoom)
        

    def room(self, door):
        print(door)
        print("Identifer", self.tvRoom)
        print("room width", self.roomWidth)
        print("room height", self.roomHieght)


ibadHouse = House("ibad")
ibadHouse.room("woodend door")
gulalamHouse = House("gul")
gulalamHouse.room("metalic door")
