utensils = {"fork", "spoon", "knife"} #unordered, unindexed her compile ettiğimde output farklı sırada
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils) #iki seti birleştirme
#dinner_table = utensils.union(dishes) #iki seti farklı bir değişkende birleştirme

#print(utensils.difference(dishes)) #utensils'da olup dishes'da olmayan elemanlar
print(utensils.intersection(dishes)) #ortak elemanı bulma

#for x in dinner_table:
    #print(x)