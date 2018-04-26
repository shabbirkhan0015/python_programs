class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        a=0.0
        a=3.14*self.r**2
        print(a)
    def per(self):
        p=0.0
        p=2*self.r*3.14
        print(p)
c=circle(4)
c.area()
c.per()