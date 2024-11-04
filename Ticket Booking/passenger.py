class Passenger:
    id = 1
    def __init__(self,name,age,berth_preference):
        self.name = name
        self.age = age
        self.berth_preference = berth_preference
        self.passenger_id = Passenger.id
        self.alloted = ""
        self.number = -1
        Passenger.id += 1
        
        
    