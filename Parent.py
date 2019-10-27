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