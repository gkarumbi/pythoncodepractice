class Parent:
    def __init__(self,eye_color = " ", Height =0):
        self.eye_color = eye_color
        self.Height = Height

    def getAge(self,current_year,birth_year):
        age = current_year - birth_year
        return age

p = Parent("Hazel", 6)
p.getAge(2019,1988)
print(str(p.getAge(2019,1988)))

class Child(Parent):

    def __init__(self, eye_color = " ", Height= 0, skin_color=" "):
        # super.__init__(self,eye_color= " ", Height = 0)
        self.skin_color = skin_color


c = Child("Brown", 5)
c.getAge(2019,2000)
print(str(c.getAge(2019,2000)))