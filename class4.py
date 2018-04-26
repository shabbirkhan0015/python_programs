class pagal:
    def __init__(self):
        self.s=""
    def get_string(self):
       self.s=input("enter you name ")
        
    def print_string(self):
        print(self.s.upper())
p=pagal()
p.get_string()
p.print_string()