#create a dictionary

class fruit:
    def __init__(self,name_of_fruit,colour):
        self.name_of_fruit=name_of_fruit
        self.colour=colour
    def print_(self):
        print("the colourof the fruit:{} is {}".format(self.name_of_fruit,self.colour))
d1={"apple":"red","banana":"yellow"}
fruit1=fruit(d1.keys(),d1.values())
print(fruit1)