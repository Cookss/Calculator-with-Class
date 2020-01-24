
class Trigger:
    def __init__(self, time, displacement, speed):
        self.time = time
        self.displacement = displacement
        self.speed = speed

    def myworkspeed(self):
        print("time (" + str(self.time) + ") displacement (" + str(self.displacement) + ") = speed (" + str(self.speed) + ")" )


class Weight:
    def __init__(allforces, gravity, mass):
        allforces.gravity = gravity
        allforces.mass = mass

    def mywork(aaa):
        aaa.weight = float(aaa.gravity) * int(aaa.mass)
        print("gravity (" + str(aaa.gravity) + ") * mass (" + str(aaa.mass) + ") = " + "weight (" + str(aaa.weight) + ")")


class Friction:
    def __init__(allfrict, frict, weight):
        allfrict.frict = frict
        allfrict.weight = weight

    def mywork(bbb):
        bbb.friction = int(bbb.frict) * float(bbb.weight)
        print("weight (" + str(bbb.weight) + ") * friction (" + str(bbb.frict) + ") = " + str(bbb.friction) + "")


class Velocity:
    def __init__(self, velocity, speed, time, xplacement, acceleration, initVelocity, initxplacement):
        self.velocity = velocity
        self.speed = speed
        self.time = time
        self.xplacement = xplacement
        self.acceleration = acceleration
        self.initVelocity = initVelocity
        self.initxplacement = initxplacement

    def myworkonvel(self):
        Velocity = int(self.velocity) + int(self.acceleration) * int(self.time)
        print("Initial Velocity (" + str(self.initVelocity) + ") * Speed (" + str(self.speed) + ") * Time(" + str(time) + ") = Velocity (" + str(Velocity) + ")")


gravity = 9.8

print("Hello im the calculator what would you like to solve?")
decision1 = input("What do you want to find\n 1. Normal Forces\n 2. Normal Velocity\n")
if decision1 == '1':

    mass = input("What is the mass of the object: ")
    g1 = Weight(gravity, mass)
    g1.mywork()
    weight = float(gravity) * int(mass)
    answer1 = input("Is there a friction?: ").lower()
    if answer1 == 'y' or 'yes':
        frict = input("what is the friction: ")
        g2 = Friction(frict, weight)
        g2.mywork()
        
    if answer1 == 'n' or 'no':
        pass

if decision1 == '2':
    decision2 = input("Velocity or Speed?: ").lower()
    if decision2 == "velocity":
        time = input("Time: ")
        speed = input("speed: ")
        initialVelocity = input("Initial Velocity: ")
        velocity = int(initialVelocity) + int(speed) * int(time)
        xplacement = 0
        acceleration = 0
        initxplacement = 0
        e1 = Velocity(velocity, speed, time, xplacement, acceleration, initialVelocity, initxplacement)
        e1.myworkonvel()
    if decision2 == "speed":
        time = input("Time: ")
        displacement = input("displacement: ")
        speed = int(time) * int(displacement)
        e2 = Trigger(time, displacement, speed)
        e2.myworkspeed()

else:
    print("Not a valid option")
