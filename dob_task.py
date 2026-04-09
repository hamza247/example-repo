# Read From the file
with open("DOB.txt", "r") as file:
    lines = file.readlines()

names = []
birthdates = []

# get the data
for line in lines:
    line = line.strip()

    if "," in line:
        name, dob = line.split(",",1)
        names.append(name.strip())
        birthdates.append(dob.strip())

# print in names and birthdates.
print("Name")
for name in names:
    print(name)

print("\nBirthdate")
for dob in birthdates:
    print(dob)