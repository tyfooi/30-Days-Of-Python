dog = {}

dog = {"name": "",
       "color":"", 
       "breed":"",
       "legs":"",
       "age":""}

student = {"first_name": "",
           "last_name": "",
           "gender":"",
           "age":"",
           "marital_status":"",
           "skills": "none",
           "country": "",
           "city":"",
           "address":""}

print(len(student))

print(student["skills"])

print("skills data type: " +str(type(student["skills"])))

student["skills"] = ["typing","learning"]
print(student["skills"])

print(student.keys())

print(student.values())

student = student.items()

print("dict items deletion is not supported??")

del dog