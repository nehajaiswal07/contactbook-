name=[]
contactno=[]
num=int(input("Enter total number you want to add contact: "))
for i in range (num):
    names=input("Enter name: ")
    
    contact=int(input("Enter number: "))
    name.append(names)
    contactno.append(contact)
print("\n Name \t\t\t Contact")
for i in range(num):
    print("\n{}\t\t\t{}".format(name[i],contactno[i]))


searchitem=input("Enter search term: ")
print("Search result is here!\n")
if searchitem in name:
    index=name.index(searchitem)
    contacts=contactno[index]
    print("Name: {} ,Phone-number: {}".format(searchitem,contacts))

else:
    print("no record!")