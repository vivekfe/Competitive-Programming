

from dataclasses import dataclass, field
#field is useful when you call the representation function , cash will not be included
@dataclass (order=True, frozen= False)
class Investor:
    sort_index: float= field(init=False, repr=False)
    name: str
    age : int
    cash: int =field(repr=False, compare= False, init=True, default=0.0)
    #using init you can't specify constructer value for cash
    def __post_init__(self):
        self.sort_index = self.cash


    def __eq__(self, other):
        if self.name==other.name and self.age ==other.age and self.cash == other.cash :
            return "It's True"
        return "It's False"

p=Investor("Tim",20,1000)
q=Investor("Qim",30,2000)
z=Investor("Geo", 30)
p>q
