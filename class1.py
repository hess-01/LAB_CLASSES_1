class panda: 
    def __init__(self,name,age,gender,wight):
        self.name = name
        self.age = age
        self.gender = gender
        self.wight = wight
    def eat(self, food):
        print(f"{self.name} is eating {food}...")
    def sleep (self):
        print(f"{self.name}) is sleeping..")







panda1 = panda("kiki", 3,"female",150)
print (panda1.age)
panda1.eat("suger cane")
panda1.sleep()


panda2 = panda("bao bao" , 5,"female",150)
print (panda2.age)
panda2.eat("bamboo")
panda2.sleep()

panda3 = panda("mei mei", 2,"male",150)
print (panda1.age)
panda3.eat("apple")
panda3.sleep()

panda4 = panda("lingo" , 4,"female",150)
print (panda1.age)
panda4.eat("watermelon")
panda4.sleep()

