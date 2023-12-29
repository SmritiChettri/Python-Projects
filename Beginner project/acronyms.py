value = input("Enter a phrase: ")
list = value.split()
acronym = ""
for i in list:
    first_letter = i[0] #extract first characters
    cap_first_letter = first_letter.upper() #convert them to uppercase
    acronym += cap_first_letter #combine them to form acronym
print(f"The acronym of '{value}' is '{acronym}'")
