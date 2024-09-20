class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("My name is",self.name)
        print("My ID number is",self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
obj=employee("Refilwe","0123",1500,"HR")
obj.display()