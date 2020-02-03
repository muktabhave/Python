class Robot():

  def __init__(self, name, age, colour):
    self.name= name
    self.age= age
    self.colour= colour

  def introduce_self(self):
    print("My name is "+ self.name) 

# r1= Robot()
# r1.name="Tom"

# r1.introduce_self()

# r=Robot()
# r.name= "Jerry"

# r.introduce_self()

r1= Robot("Tom", 10, "Silver")

r1.introduce_self()

r2= Robot("Jerry", 5, "white")

r2.introduce_self()


