#June-12,2026
"""
# key - value pairs
# mutable, ordered, unique keys
studentData = {
    "name":"ramya",
    "email":"ramya@gmail.com",
    "mobile":597694567,
    "isActive":True
}

print(studentData)
print(type(studentData))
print(len(studentData))

print(studentData["email"])
print(studentData.get("email"))

print(studentData.keys())
print(studentData.values())

studentData["total"] = 500
print(studentData)

studentData.update({"mobile":1234567890})
print(studentData)

# studentData.pop("isActive")

studentData.pop("isActive")
print(studentData,"pop")

studentData["name"] = "mithra"
print(studentData)

studentData["marks"] = [100,89,78,72,99]
print(studentData)

# for i in studentData:
#     print(i)

# for i in studentData.values():
#     print(i)

for key, val in studentData.items():
    print(f"{key} = {val}")
"""
#June-15,2026
"""
students_data = [
    {
        "name" : "Alex",
        "email" : "alex78@gmail.com",
        "marks" : [90,96,55,89,88]
    },
    {
        "name" : "Bob",
        "email" : "bob69@gmail.com",
        "marks" : [90,96,65,79,88]
    },
    {
        "name" : "Karen",
        "email" : "karencc@gmail.com",
        "marks" : [90,86,65,69,98]
    },
    {
        "name" : "Donald",
        "email" : "donald67@gmail.com",
        "marks" : [89,96,55,69,48]
    },
    {
        "name" : "Eugene",
        "email" : "eugene789@gmail.com",
        "marks" : [90,80,78,51,73]
    }
]

#print specific student value
print(students_data[1])

#Using Loops                                #Using Built in Funtions
result = []                                 #result = []
for a in students_data:                     #for x in students_data:
    total = 0                               #   result.append({})
    for i in a["marks"]:                    #        "name": x["name"],
        total+=i                          #        "email": x["email"],  
    result.append({                         #         "marks": sum(x["marks"])
        "name": a["name"],                  #    })
        "email": a["email"],                #print(result)
        "marks": total
    })
print(result)

# sorting from highest to lowest

n = len(result)

for i in range(n):
    for j in range(i + 1, n):
        if result[i]["marks"] < result[j]["marks"]:
            result[i], result[j] = result[j], result[i]
print(result)

# adding remarks based on marks
for y in result:
        if 450<=y["marks"]<=500:
            y['remarks']= "Superb, You nailed it!"
        elif 400<=y["marks"]<=449:
            y['remarks']= "Good, Keep it up!"
        else:
            y['remarks']= "Can do better!"
print(result)
"""
