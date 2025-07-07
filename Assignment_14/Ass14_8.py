class vehicle:
    def start(self):
        print("In parent vehicle ")

class car(vehicle):
    def start(self):
        print("in child car")

    def stop(self):
        print("in child stop")

vobj = car()
vobj.start()



#methood overriding start method override zali and start child method mdhla anser display zla