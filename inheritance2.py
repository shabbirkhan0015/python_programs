class shirt:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
        print("color:",self.color)
        print('brand:',self.brand)
class formalwear(shirt):
    def __init__(self,color,brand,slimfit,dottedOrNot):
        shirt.__init__(self,color,brand)
        self.slimfit=slimfit
        self.dottedOrNot=dottedOrNot
class causalwear(shirt):
    def __init__(self,color,brand,sleeve,multicolor):
        shirt.__init__(self,color,brand)
        self.sleeve=sleeve
        self.multicolor=multicolor
class partywear(shirt):
    def __init__(self,color,brand,shining,collar):
        shirt.__init__(self,color,brand)
        self.shining=shining
        self.collar=collar
        print("shining or not:",self.shining)
        print('collar type:',self.collar)
p1=partywear("RED","louis phillipe","YES","round")  
