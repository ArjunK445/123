# class animal:
#     def dog(self):
#         print ("Dog is barking")
#     def cow(self):
#         print("National animal")
#     def elephant(self):
#         print("Biggest animal on land")
#     def giraffe(self):
#         print("Tallest animal")
#     snake = "Poisonous "

# d = animal()
# s = animal()
# e = animal()
# c = animal()
# g = animal() 

# print(s.snake)
# print(d.dog())
# c.cow()
# e.elephant()
# g.giraffe()

class school:
    S_name = "Shree Secondary school"   # class attributes
    S_add = "Ktm"
    
    def std_info(self,name,address,roll,grade,S_name="Shree Secondary school" ): # object attributes
        self.name = name
        self.address = address
        self.roll = roll
        self.grade = grade
        self.S_name = S_name
a = school()
a.std_info("Ram","ktm",6,10)
print("School name:",a.S_name)
print("School address:",a.S_add)
print(a.name)
print(a.address)
print(a.roll)
print(a.grade)
print(a.S_name)

b = school()
b.std_info("Krish","MNR",14,12,"Satyawoti school")
print(b.name)
print(b.address)
print(b.roll)
print(b.S_name)

c = school()
print(c.S_name)
c.std_info("Kamal","Jhapa",4,5,"Mindrisers Academy")
print(c.name)
print(c.address)
print(c.roll)
print(c.grade)
print(c.S_name)