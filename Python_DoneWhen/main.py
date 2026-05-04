'''import json

#Read JSON file
with open("details.json", "r") as file:
    data = json.load(file)

#Filter : age>18
filtered = [person for person in data if person["age"] > 18]

#print result
for person in filtered:
    print(person)'''

import json

def filter_people(data, min_age):
    return [person for person in data if person["age"] > min_age]


if __name__ == "__main__":
    with open("Python_DoneWhen/details.json", "r") as file:
        data = json.load(file)

    min_age = int(input("Enter minimum age: "))
    result = filter_people(data, min_age)

    print("\nFiltered Results:")
    for person in result:
        print(f"{person['name']} ({person['age']})")