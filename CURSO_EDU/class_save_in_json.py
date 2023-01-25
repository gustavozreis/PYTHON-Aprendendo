import json

save_file = 'class_to_json.txt'

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
       
# save json to file 
        
gustavo = Person('Gustavo', 35)
ellen = Person('Ellen', 33)
people_list = [vars(gustavo), vars(ellen)]

with open(save_file, 'w') as file:
    json.dump(people_list, file, ensure_ascii=False, indent=2)
    
# load json from file

people_list_from_file = []

with open(save_file, 'r') as file:
    people_list_from_file = json.load(file)
    print(type(people_list_from_file))
    

gustavo2 = Person(**people_list_from_file[0])
ellen2 = Person(**people_list_from_file[1])

print(gustavo2.name, gustavo2.age, '\n', ellen2.name, ellen2.age)