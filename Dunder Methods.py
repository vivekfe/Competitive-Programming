

class Person:
    def __init__(self, name, age, country, speed, dist_cov, cost):
        self.name = name
        self.age= age
        self.country = country #property/attribute/ class varible
        self.speed = speed
        self.cost = cost
        self.dist_cov= dist_cov
    # def __del__(self):
    #     print("Object has been deconstructed")

    def say_hello_to_person(self): #method and method works on attributes
        print(f"Hello {self.name}")

    def apply_brakes(self):
        self.speed =0

    # def calculateCost(self):
    #     if self.dist_cov <=50000:
    #         self.cost = 50%*self.cost
    #     if self.dist_cov >=50000 and self.cost<=100000:
    #         self.cost = 40%*self.cost
    #     if self.dist_cov >100000 and self.cost<=200000:
    #         self.cost = 30%*self.cost

    def calculateCost(self):
        if self.dist_cov <=50000:
            self.cost = .5*self.cost
        elif self.dist_cov >=50000 and self.cost<=100000:
            self.cost = .4*self.cost
        elif self.dist_cov >100000 and self.cost<=200000:
            self.cost = .3*self.cost
        else:
            self.cost = .7*self.cost

    def getCost(self):
        return self.cost

P= Person("Mike",25, "IN",100, 100000, 100000)
# No need to call a deconstructer as it will be called when the variable goes out of scope

P.calculateCost()
