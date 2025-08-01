class Car:
    def start(self, color, wheel):
        self.wheel = wheel
        self.color = color

tesla = Car()
tesla.start("Sky Blue", 4)
print("Tesla has " + tesla.color + " color")
print("Tesla has " + str(tesla.wheel) + " wheels")

chevrolet = Car() 
chevrolet.start("white",4)
print("chevrolet has " + chevrolet.color + " color") 
print("chevrolet has " + str(chevrolet.wheel) + " wheels")



lamborgini = Car()
bugatti = Car()
ferrari = Car() 
ferrari.start("white",4)
print("ferrari has " + ferrari.color + " color")
print("ferrari has "+ str(ferrari.wheel) + "wheels")




audii = Car()
bmw = Car()