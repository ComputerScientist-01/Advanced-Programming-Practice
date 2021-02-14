class Employee:
    def __init__(self, name, age,basic,grade):
        self.name = name
        self.age = age
        self.basic = basic
        self.grade = grade


    def set(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
    
    def ComputeSalary(self): 
        hra = 0.2 * self.basic 
        da = 0.5 * self.basic 
        pf = 0.11 * self.basic
        ta = 0.075 * self.basic 
        
        # Condition to compute the 
        # allowance for the person
        if self.grade == 'A': 
            allowance = 1700.0
        elif self.grade == 'B':  
            allowance = 1500.0
        else: 
            allowance = 1300.0; 
        gross = round(self.basic+ ta + hra + da + allowance - pf) 
        print(gross)


emp = Employee("Sam", 36,1000,"A")
emp.set()
emp.ComputeSalary()