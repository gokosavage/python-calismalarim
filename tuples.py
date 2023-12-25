student = ("Göks", 22, "male") #list gibi ama değiştirilemiyor

print(student.count("Göks")) #kaç adet olduğunu
print(student.index("male"))

for x in student:
    print(x)

if "Göks" in student:
    print("Göks is here!")