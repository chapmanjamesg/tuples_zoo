my_zoo = ("Red Panda", "Otter", "Shark", "Polar Bear", "Elephant", "Tiger", "Lion", "Kangaroo", "Panda", "Wolf") 

print(my_zoo.index("Shark"))

animal_to_find = "Lion"

if animal_to_find in my_zoo:
    print(f"I found the {animal_to_find}")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = my_zoo

print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)



zoo_list = list(my_zoo)
print(zoo_list)


zoo_list.extend(["Moose", "Squirrel"])
print(zoo_list)

new_zoo = tuple(zoo_list)

print(new_zoo)
