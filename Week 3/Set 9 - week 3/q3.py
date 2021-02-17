# 3. Write a python code to implement following scenario, In a company Factory, staff
# and Office staff have certain common properties - all have a name, designation, age
# etc. Thus they can be grouped under a class called CompanyMember. Apart from
# sharing those common features, each subclass has its own characteristic - FactoryStaff
# gets overtime allowance while OfficeStaff gets traveling allowance for an office job.
# The derived classes ( FactoryStaff &amp; OfficeStaff) has its own characteristic and, in
# addition, they inherit the properties of the base class (CompanyMember).

class CompanyMember(object):
    def __init__(self, name, des, age):
        self.name = name
        self.age = age
        self.des = des
    
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nDesignation: {self.des}" )
        
class FactoryStaff(CompanyMember):
    def __init__(self, name, des, age, a):
        self.a = a
        CompanyMember.__init__(self, name, des, age)
    def allowance(self):
        print(f"Overtime Allowance: {self.a}")

class OfficeStaff(CompanyMember):
    def __init__(self, name, des, age, a):
        self.a = a
        CompanyMember.__init__(self, name, des, age)
    def allowance(self):
        print(f"Travel Allowance: {self.a}")
        

# com = CompanyMember("ABC", "Client", 32)
# com.show()
res1 = FactoryStaff("ABC", "Client", 32, 1200)
res2 = OfficeStaff("DEF", "Worker", 35, 1300)
res1.show()
res1.allowance()
res2.show()
res2.allowance()
    