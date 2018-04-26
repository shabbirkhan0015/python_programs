class Address:
    street_name="Massachusetts Ave"
    number=77
    def __init__(self,street,num):
        self.street_name=street
        self.number=num
class campusaddress(Address):
    def __init__(self,officeaddress):
        self.officeaddress=officeaddress
s1=campusaddress("b8-401")
print(s1.officeaddress)
print(s1.street_name)
print(s1.number)