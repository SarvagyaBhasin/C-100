class Car(object):
    def __init__(self, model, colour, company, speedlimit):
        self.colour=colour
        self.model=model
        self.company=company
        self.speedlimit=speedlimit
    def start(self):
        print("car started")

    def accelerate(self):
        print("car accelerated")

    def stop(self):
        print("car stopped")

    def gearchange(self, gear):
        print("gear changed to ", gear)

Henessy=Car("VenomF5", "Black", "Henessy", 200)
print(Henessy.colour)
Henessy.start()
Henessy.accelerate()
Henessy.gearchange(5)
Henessy.stop()