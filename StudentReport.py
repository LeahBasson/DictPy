# Design a student report system

# dictionary within a dictonary.
student = {
"name": "Daniel",
"grade": 11,
"marks": {
"Math": 88,
"Science": 79,
"English": 85
}
}

# prints the science mark
print("Science marks:", student["marks"]["Science"])

# adds history and math to marks
student["marks"]["History"] = 78
student["marks"]["Math"] = 92

# removes english marks
student["marks"].pop("English")

# loops through key and values in marks dictionary.
for subject, mark in student["marks"].items():
    print(f"Subject: {subject}, Mark: {mark}")


student02 = {"name": "Faithlyn",
"grade": 10,
"marks": {
"Math": 81,
"Science": 88,
"English": 90}
}            

# 3 dictionaries in total.
# 2 dictionaries in a dictionary.
students = {
"student1": student,
"student2": student02
}

print("Math mark of second student:", students["student2"]["marks"]["Math"])